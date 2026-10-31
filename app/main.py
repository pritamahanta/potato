from fastapi import FastAPI

app = FastAPI(
    title="POTATO",
    description="A lightweight, multi-provider LLM gateway.",
    version="0.1.0"
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {
        "status": "ok",
        "service": "potato"
    } 