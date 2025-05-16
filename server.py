from fastmcp import FastMCP
from notegen.keyword_utils import sync_keywords_with_notes as sync_keywords_with_notes_impl
from notegen.file_utils import check_note_exists as check_note_exists_impl
from typing import Dict, Any

mcp = FastMCP(title="notegen MCP Server")

@mcp.tool()
def sync_keywords_with_notes():
    """Sync keywords with notes."""
    return sync_keywords_with_notes_impl()

@mcp.tool()
def check_note_exists(transcript_path: str) -> Dict[str, Any]:
    """
    Check if a note with the given title already exists.
    
    Args:
        transcript_path: Path to the transcript to check
    
    Example:
        check_note_exists(transcript_path="transcripts/Variational Inference: ELBO, KL Divergence, and Applications.txt")
    """
    return check_note_exists_impl(transcript_path)

def main():
    """Run the MCP server using fastmcp."""
    mcp.run()

if __name__ == "__main__":
    main()