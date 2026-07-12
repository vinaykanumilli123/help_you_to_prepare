from langchain_core.messages import HumanMessage
from agent.agents import get_research_agent
from agent.llm import llm
from .prompts import RESEARCH_NOTES_PROMPT
from agent.storage_client import StorageClient
from agent.database_client import DatabaseClient

db = DatabaseClient()
storage = StorageClient()


async def research_node(state):

    research_agent = await get_research_agent()

    topic = state["topic"]
    weak_concepts = state.get("weak_concepts", [])
    print("$$$$$$$$$$$$$")
    print(weak_concepts)

    if weak_concepts:
        search_topic = f"{topic}: {'; '.join(weak_concepts)}"
    else:
        search_topic = topic
    print("$$$$$$$$$$$$$$$$$")

    print(search_topic)

    print("@@@@@@@@@@@@@@@@@@@@")

    result = await research_agent.ainvoke(
        {
            "messages": [
                HumanMessage(
                    content=f"""
            Research the following topic in detail.

            Topic:
            {search_topic}

            Generate complete study material.
            """
                            )
                        ]
                    }
                )

    return {
        "raw_content": result["messages"][-1].content
    }

async def notes_node(state):

    print(state["raw_content"])

    prompt = RESEARCH_NOTES_PROMPT.format(
        research=state["raw_content"]
    )

    response = await llm.ainvoke(prompt)

    return {
        "markdown_notes": response.content
    }


async def storage_node(state):

    filename = (
        state["topic"]
        .replace(" ", "_")
        .lower()
        + ".md"
    )

    md_path = await storage.save_markdown(
        content=state["markdown_notes"],
        filename=filename,
    )

    pdf_path = await storage.markdown_to_pdf(
        md_file=md_path
    )

    return {
        "markdown_path": md_path,
        "pdf_path": pdf_path,
    }


async def database_node(state):

    topic_id = await db.create_topic(
        user_id=state["user_id"],
        topic_name=state["topic"],
    )
    # topic_id = topic["topic_id"]

    await db.save_note(
        topic_id=topic_id,
        markdown_path=state["markdown_path"],
        pdf_path=state["pdf_path"],
    )
    return {
        "topic_id": topic_id,
        "status": "SUCCESS",
    }
    return {"status":"success"}