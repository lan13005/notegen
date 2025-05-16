# notegen MCP

An MCP server setup that helps language models convert YouTube video transcripts into structured technical notes in markdown format, intended for the [Obsidian](https://obsidian.md) graphs. 

- Uses wiki-style links to link core ideas inside a note across multiple notes.
- The system uses a persistent central Keyword store to track and reuse core ideas.
- Categories are tracked like keywords and form more connections between notes.
- Stores video metadata into markdown frontmatter.

## Setup

1. Install dependencies:
```bash
uv pip install -e .
```

2. Enable the MCP server in your editor settings

3. Example prompt:
```
Please create notes for files in transcripts/ folder
```