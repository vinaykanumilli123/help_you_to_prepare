from mcpservers.databaseserver.database import engine
from mcpservers.databaseserver.models import Base


print("Creating tables...")

Base.metadata.create_all(
    bind=engine
)

print("Done")