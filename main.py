from fastapi import FastAPI
from src.contacts.routers import router as contacts_router
app = FastAPI()

app.include_router(contacts_router, prefix = "/contacts", tags = ["contacts"])

@app.get("/ping")
async def ping():
    return {"message":"ping is ok"}
