import argparse
from notegen.video_utils import process_video_metadata, process_video_transcript, get_sanitized_title_from_url
from notegen.file_utils import read_websites_md
from notegen.keyword_utils import sync_keywords_with_notes
import os
from rich.console import Console

console = Console()

def init_project():
    """
    Initialize the notegen project structure by creating required directories and files if they do not exist:
    - notes/
    - transcripts/
    - keywords.md
    - websites.md
    Prints a confirmation message to the console.
    """
    os.makedirs('notes', exist_ok=True)
    os.makedirs('transcripts', exist_ok=True)
    if not os.path.exists('keywords.md'):
        with open('keywords.md', 'w') as f:
            f.write('')
    if not os.path.exists('websites.md'):
        with open('websites.md', 'w') as f:
            f.write('# Websites to process\n')
    console.print('Project initialized.', style='green')

def dump_initial_transcript(metadata, transcript_text, sanitized_title):
    """
    Write an initial transcript note file using the provided metadata and transcript text.
    Args:
        metadata (dict): Video metadata (title, link, uploader, duration, views).
        transcript_text (str): The transcript text to include in the note.
        sanitized_title (str): Sanitized title used for the filename.
    Returns:
        str: The path to the written note file.
    """
    note_path = os.path.join('transcripts', f'{sanitized_title}.txt')
    with open(note_path, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: {metadata['title']}\nlink: {metadata.get('link', '')}\nuploader: {metadata.get('uploader', '')}\nduration: {metadata.get('duration', '')}\nviews: {metadata.get('views', '')}\n---\n\n# {metadata['title']}\n\n{transcript_text}...\n")
    return note_path

def transcribe_websites_md():
    """
    Process all URLs in websites.md:
    - For each URL, extract the sanitized title and check if a transcript already exists.
    - If not, download metadata and transcript, and write the transcript file.
    - Prints progress and error messages to the console.
    """
    websites = read_websites_md()
    if not websites['success']:
        console.print('Error reading websites.md:', websites['error'], style='red')
        return
    processed_count = 0
    for url in websites['urls']:
        console.print(f'Processing: {url}', style='blue')
        title_result = get_sanitized_title_from_url(url)
        if not title_result['success']:
            raise Exception(f'  Title extraction error: {title_result["error"]}')
        sanitized_title = title_result['sanitized_title']
        transcript_path = os.path.join('transcripts', f'{sanitized_title}.txt')
        if os.path.exists(transcript_path) and os.path.getsize(transcript_path) > 0:
            console.print(f'  Transcript already exists and is not empty, skipping: {transcript_path}', style='yellow')
            continue
        meta = process_video_metadata(url)
        if not meta['success']:
            console.print('  Metadata error:', meta['error'], style='red')
            continue
        transcript = process_video_transcript(url)
        if not transcript['success']:
            console.print('  Transcript error:', transcript['error'], style='red')
            continue
        dump_initial_transcript(meta['metadata'], transcript['transcript_text'], sanitized_title)
        processed_count += 1
    console.print(f'\nAll URLs processed, {processed_count} transcripts generated', style='green')

def main():
    """
    Entry point for the notegen CLI. Parses command-line arguments and dispatches to the appropriate subcommand:
    - init: Initialize project structure
    - transcribe: Transcribe all URLs in websites.md
    - sync: Synchronize keywords with notes
    """
    parser = argparse.ArgumentParser(description='notegen CLI')
    subparsers = parser.add_subparsers(dest='command')

    parser_init = subparsers.add_parser('init', help='Initialize notegen project structure')
    parser_transcribe = subparsers.add_parser('transcribe', help='Attempt to transcribe all URLs in websites.md')
    parser_transcribe.add_argument('websites_md', nargs='?', default='websites.md', help='websites.md file to process')

    parser_sync = subparsers.add_parser('sync', help='Sync keywords with notes')

    args = parser.parse_args()

    if args.command == 'init':
        init_project()
    elif args.command == 'transcribe':
        transcribe_websites_md()
    elif args.command == 'sync':
        sync_keywords_with_notes()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
