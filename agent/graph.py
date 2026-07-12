# import asyncio
# import os
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_mcp_adapters.client import MultiServerMCPClient
# from langgraph.prebuilt import create_react_agent
# from dotenv import load_dotenv
# from langgraph.checkpoint.memory import InMemorySaver

# memory = InMemorySaver()
# load_dotenv()

# async def main():
#     client = MultiServerMCPClient(
#         {
#             "study_tools": {
#                 "transport": "streamable_http",
#                 "url": "http://127.0.0.1:8000/mcp",
#             }
#         }
#     )

#     tools = await client.get_tools()

#     print("Connected MCP tools:")
#     for tool in tools:
#         print(f" - {tool.name}")

#     llm = ChatGoogleGenerativeAI(
#         model="gemini-2.0-flash",
#         google_api_key=os.getenv("GOOGLE_API_KEY"),
#         temperature=0,
#     )

#     agent = create_react_agent(
#     model=llm,
#     tools=tools,
#     checkpointer=memory,
#     )

#     print("\nStudy Assistant Ready!")
#     print("Type 'exit' to quit.\n")

#     while True:
#         query = input("You: ")

#         if query.lower() in {"exit", "quit"}:
#             break

#         result = await agent.ainvoke(
#         {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": query,
#             }
#         ]
#         },
#         config={
#             "configurable": {
#                 "thread_id": "user-2"
#             }
#         }
#     )

#         print("\nAssistant:")
#         print(result["messages"])
#         print()

# if __name__ == "__main__":
#     asyncio.run(main())