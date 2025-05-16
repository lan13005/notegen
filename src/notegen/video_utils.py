from urllib.parse import parse_qs, urlparse
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
import re
import os
from rich.console import Console
from notegen.file_utils import sanitize_filename

console = Console()

def extract_video_id(url):
    """Extract video ID from various YouTube URL formats."""
    parsed_url = urlparse(url)
    if parsed_url.hostname == 'youtu.be':
        return parsed_url.path[1:]
    if parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed_url.path == '/watch':
            return parse_qs(parsed_url.query)['v'][0]
    return None

def process_video_metadata(url: str):
    """Process video metadata and return formatted information."""
    # Validate URL
    if not url.startswith(("https://www.youtube.com/watch?v=", "https://youtu.be/")):
        return {
            "success": False,
            "error": "Invalid YouTube URL format"
        }
    
    try:
        # Extract video ID
        video_id = extract_video_id(url)
        if not video_id:
            return {
                "success": False,
                "error": "Could not extract video ID from URL"
            }
        
        # Get metadata
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            duration_seconds = info_dict['duration']
            
            # Convert seconds to HH:MM:SS format
            hours = duration_seconds // 3600
            minutes = (duration_seconds % 3600) // 60
            seconds = duration_seconds % 60
            
            duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            metadata = {
                'title': info_dict['title'],
                'link': f'https://www.youtube.com/watch?v={video_id}',
                'duration': duration_formatted,
                'views': info_dict.get('view_count', 'N/A'),
                'uploader': info_dict.get('uploader', 'N/A')
            }
        
        return {
            "success": True,
            "metadata": metadata
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error processing metadata: {str(e)}"
        }

def process_video_transcript(url: str):
    """Process video transcript and save it to the transcripts directory."""
    # Validate URL
    if not url.startswith(("https://www.youtube.com/watch?v=", "https://youtu.be/")):
        return {
            "success": False,
            "error": "Invalid YouTube URL format"
        }
    
    try:
        # Extract video ID
        video_id = extract_video_id(url)
        if not video_id:
            return {
                "success": False,
                "error": "Could not extract video ID from URL"
            }
        
        # Create transcripts directory if it doesn't exist
        os.makedirs('transcripts', exist_ok=True)
        
        # Get video title for filename
        ydl_opts = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            video_title = info_dict['title']
        
        # Get transcript
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            # Join all transcript pieces and clean up formatting
            transcript_text = ' '.join([entry['text'].strip() for entry in transcript])
            # Remove multiple spaces and newlines
            transcript_text = re.sub(r'\s+', ' ', transcript_text)
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to get video transcript: {str(e)}"
            }
        
        # Save transcript to file
        video_title = sanitize_filename(video_title)
        output_filename = f"{video_title}.txt"
        output_path = os.path.join('transcripts', output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(transcript_text)
        
        return {
            "success": True,
            "sanitized_title": video_title,
            "transcript_path": output_path,
            "transcript_text": transcript_text
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error processing transcript: {str(e)}"
        }

def get_sanitized_title_from_url(url: str):
    """Quickly extract and sanitize the video title from a YouTube URL."""
    # Validate URL
    if not url.startswith(("https://www.youtube.com/watch?v=", "https://youtu.be/")):
        return {
            "success": False,
            "error": "Invalid YouTube URL format"
        }
    try:
        video_id = extract_video_id(url)
        if not video_id:
            return {
                "success": False,
                "error": "Could not extract video ID from URL"
            }
        ydl_opts = {'quiet': True, 'skip_download': True, 'forcejson': True, 'simulate': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            video_title = info_dict['title']
        sanitized_title = sanitize_filename(video_title)
        return {
            "success": True,
            "sanitized_title": sanitized_title,
            "raw_title": video_title
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error extracting title: {str(e)}"
        }

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=f19bfHpCths"
    # process_video_metadata(youtube_url)
    # process_video_transcript(youtube_url)
    print(get_sanitized_title_from_url(youtube_url))
