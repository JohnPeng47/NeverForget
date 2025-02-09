from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from typing import Optional
from datetime import datetime

from config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

# Initialize FastAPI app
app = FastAPI(title="My FastAPI App")

# Example model
class Item(SQLModel, table=True):
    id: Optional[int] = None
    name: str
    description: str
    created_at: datetime = datetime.now()

# Create tables on startup
@app.on_event("startup")
async def startup():
    SQLModel.metadata.create_all(engine)

# Example route
@app.get("/items/", response_model=list[Item])
async def get_items():
    # This is just a fake response for demonstration
    return [
        Item(
            id=1,
            name="Test Item",
            description="This is a test item",
            created_at=datetime.now()
        )
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True) 