from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from utils import extract_video_id

def fetch_and_summarize_transcript(video_url: str) -> str:
    video_id = extract_video_id(video_url)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        raise Exception(f"Error fetching transcript: {e}")
    
    result = ''
    for i in transcript:
        result += ' ' + i['text']
        print(len(result))

    summarizer = pipeline('summarization')

    num_iters = int(len(result)/1000)
    summarized_text = []
    for i in range(0, num_iters + 1):
        start = i * 1000
        end = (i + 1) * 1000
        out = summarizer(result[start:end])
        out = out[0]
        out = out['summary_text']
        summarized_text.append(out)

    return "".join(str(summarized_text).replace('[','').replace(']','').split(','))