from fastapi import FastAPI, HTTPException
from models import VideoRequest, SummaryResponse
from services import fetch_and_summarize_transcript

app = FastAPI()

@app.post("/summarize", response_model=SummaryResponse)
async def summarize_video(request: VideoRequest):
    try:
        summary = fetch_and_summarize_transcript(request.url)
        return SummaryResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def get_health():
    return {"status": "ok"}
