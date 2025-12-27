from fastapi import FastAPI
from app.api import events

app = FastAPI(title="YUI Assistant Backend")
app.include_router(events.router)


@app.get("/health")
def health():
    return {"status": "Working"}
