def extract_video_id(video_url: str) -> str:
    """
    Extract the video ID from the YouTube URL
    """
    try:
        video_id = str(video_url).split('=')[1]
    except IndexError:
        raise ValueError("Invalid YouTube URL")
    return video_id