from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int,text: str):
    return {"item_id": item_id,"text": text}
