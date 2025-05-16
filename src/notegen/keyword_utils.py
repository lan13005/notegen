import os
from typing import Dict, Any
import re

def sync_keywords_with_notes() -> Dict[str, Any]:
    """
    Scan all notes in notes/ for [[Keyword]] links, compare to keywords.md, append missing keywords, and remove unused ones.
    Returns a dict with the sync result.
    """
    notes_dir = "notes"
    keywords_file = "keywords.md"
    keyword_pattern = re.compile(r'\[\[([^\]]+)\]\]')
    keywords_in_notes = set()

    # 1. Scan all notes for [[Keyword]] links
    if os.path.exists(notes_dir):
        for fname in os.listdir(notes_dir):
            if fname.endswith(".md"):
                fpath = os.path.join(notes_dir, fname)
                try:
                    with open(fpath, "r") as f:
                        content = f.read()
                    found = keyword_pattern.findall(content)
                    keywords_in_notes.update([k.strip() for k in found if k.strip()])
                except Exception:
                    continue  # skip unreadable files
    # 2. Read keywords.md
    if not os.path.exists(keywords_file):
        with open(keywords_file, "w") as f:
            f.write("")
        keywords_in_glossary = set()
    else:
        with open(keywords_file, "r") as f:
            keywords_in_glossary = set(line.strip() for line in f if line.strip())
    # 3. Compute keywords to add and remove
    to_add = keywords_in_notes - keywords_in_glossary
    to_remove = keywords_in_glossary - keywords_in_notes
    # 4. Update keywords.md -> Get the union then remove the remove set
    updated_keywords = sorted((keywords_in_glossary | to_add) - to_remove)
    try:
        with open(keywords_file, "w") as f:
            for kw in updated_keywords:
                f.write(f"{kw}\n")
        return {
            "success": True,
            "added": sorted(to_add),
            "removed": sorted(to_remove),
            "final_keywords": updated_keywords
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Error updating keywords.md: {str(e)}"
        }

if __name__ == "__main__":
    return_dict = sync_keywords_with_notes()
    print(return_dict)