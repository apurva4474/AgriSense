from fastapi import FastAPI

app = FastAPI(
    title="AgriSense API",
    description="Smart Agriculture Decision Support System",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "message": "AgriSense backend is running",
    }