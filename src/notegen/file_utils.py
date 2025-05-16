import os
from rich.console import Console
import re

console = Console()

def sanitize_filename(filename: str) -> str:
    """Sanitize a filename by removing special characters."""
    filename = re.sub(r"[^\w\s-]", "", filename)  # Remove special chars except letters, numbers, whitespace and dash
    filename = re.sub(r"[\s_-]+", "-", filename)  # Replace multiple whitespace/underscore/dash with single dash
    return filename 

def check_note_exists(transcript_path: str):
    """Check if a note with the given title already exists."""
    try:
        # Sanitize the title for filename
        sanitized_title = transcript_path.split('/')[-1].strip('.txt')
        
        # Check if the note file exists
        os.makedirs("notes", exist_ok=True)
        note_path = os.path.join("notes", f"{sanitized_title}.md")
        exists = os.path.exists(note_path)
        
        print(f"Checking if note exists: {note_path}")
        
        return {
            "success": True,
            "exists": exists,
            "path": note_path if exists else None
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error checking note existence: {str(e)}"
        }

def read_websites_md():
    """Read the websites.md file to get list of URLs."""
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