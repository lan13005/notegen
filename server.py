from fastmcp import FastMCP
from notegen.keyword_utils import sync_keywords_with_notes as sync_keywords_with_notes_impl
from notegen.file_utils import get_unsynced_transcripts as get_unsynced_transcripts_impl

mcp = FastMCP(title="notegen MCP Server")

@mcp.tool()
def sync_keywords_with_notes():
    """Sync keywords with notes."""
    return sync_keywords_with_notes_impl()

@mcp.tool()
def get_unsynced_transcripts():
    """Get list of unsynced transcripts."""
    return get_unsynced_transcripts_impl()

def main():
    """Run the MCP server using fastmcp."""
    mcp.run()

if __name__ == "__main__":
    main()