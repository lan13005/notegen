import os
from rich.console import Console
import re

console = Console()

def sanitize_filename(filename: str) -> str:
    """
    Sanitize a filename by removing special characters and normalizing whitespace/underscores/dashes.
    - Removes all characters except letters, numbers, whitespace, and dash.
    - Replaces multiple whitespace/underscore/dash with a single dash.
    Args:
        filename (str): The filename to sanitize.
    Returns:
        str: The sanitized filename.
    """
    filename = re.sub(r"[^\w\s-]", "", filename)  # Remove special chars except letters, numbers, whitespace and dash
    filename = re.sub(r"[\s_-]+", "-", filename)  # Replace multiple whitespace/underscore/dash with single dash
    return filename 

def get_unsynced_transcripts():
    """
    Get a list of transcripts in the 'transcripts/' directory that do not have a corresponding note in 'notes/'.
    Returns:
        dict: {
            'success': bool,           # True if operation succeeded
            'paths': list[str],        # List of note paths (notes/*.md) that need to be generated
            'error': str | None        # Error message if success is False
        }
    """
    try:
        # Get list of unsynced transcripts
        unsynced_transcripts = []
        for file in os.listdir("transcripts"):
            if file.endswith(".txt"):
                file = file.strip('.txt')
                if not os.path.exists(f"notes/{file}.md"):
                    unsynced_transcripts.append(file)
        os.makedirs("notes", exist_ok=True)      
        note_paths = []
        for transcript in unsynced_transcripts:            
            transcript = transcript.split('/')[-1]            
            note_paths.append(os.path.join("notes", f"{transcript}.md"))
        return {
            "success": True,
            "paths": note_paths
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error getting unsynced transcripts: {str(e)}"
        }

def read_websites_md():
    """
    Read the 'websites.md' file and return a list of URLs (one per line, stripped of whitespace).
    If the file does not exist, it is created with a header and an empty list is returned.
    Returns:
        dict: {
            'success': bool,           # True if operation succeeded
            'urls': list[str],         # List of URLs (may be empty)
            'error': str | None        # Error message if success is False
        }
    """
    try:
        if not os.path.exists("websites.md"):
            with open("websites.md", "w") as f:
                f.write("# Websites to process\n")
            return {
                "success": True,
                "urls": []
            }
        with open("websites.md", "r") as f:
            url_list = f.readlines()
        for i in range(len(url_list)):
            url_list[i] = url_list[i].strip()
        return {
            "success": True,
            "urls": url_list
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error reading websites.md: {str(e)}"
        } 