import os
import subprocess
from collections import deque
from pathlib import Path
from dotenv import load_dotenv

from tafrigh import Config, TranscriptType, farrigh

# Load environment variables from .env file
load_dotenv()

# Define Wit.ai API keys for languages using environment variables
LANGUAGE_API_KEYS = {
    'EN': os.getenv('WIT_API_KEY_ENGLISH'),
    'AR': os.getenv('WIT_API_KEY_ARABIC'),
    'FR': os.getenv('WIT_API_KEY_FRENCH'),
    'JA': os.getenv('WIT_API_KEY_JAPANESE'),
    'ES': os.getenv('WIT_API_KEY_SPANISH'),  # Add Spanish language API key
    # Add more languages and API keys as needed
}

def download_youtube_audio(youtube_url):
    output_path = Path(__file__).parent / 'downloads' / '%(id)s.%(ext)s'
    subprocess.run(['yt-dlp', '-x', '--audio-format', 'wav', '-o', str(output_path), youtube_url], check=True)
    return next(Path(__file__).parent.glob('downloads/*.wav'))

def transcribe_file(file_path, language_sign):
    wit_api_key = LANGUAGE_API_KEYS.get(language_sign.upper())
    if not wit_api_key:
        print(f"API key not found for language: {language_sign}")
        return

    config = Config(
        urls_or_paths=[str(file_path)],
        wit_client_access_tokens=[wit_api_key],
        output_formats=[TranscriptType.TXT, TranscriptType.SRT],
        output_dir=str(file_path.parent),
    )

    farrigh(config)

def main():
    choice = input("Do you want to transcribe a YouTube video (Y) or a local file (L)? [Y/L]: ").strip().upper()

    if choice == 'Y':
        youtube_url = input("Enter the YouTube video link: ")
        language_sign = input("Enter the language sign (e.g., EN, AR, FR, JA, ES): ")
        audio_file = download_youtube_audio(youtube_url)
        transcribe_file(audio_file, language_sign)
    elif choice == 'L':
        file_path = input("Enter the path to the local file or directory: ").strip()
        file_path = Path(file_path)

        if file_path.is_dir():
            # Process all audio/video files in the directory
            for file in file_path.glob('*'):
                if file.suffix.lower() == '.wav':
                    language_sign = input(f"Enter the language sign for {file.name} (e.g., EN, AR, FR, JA, ES): ")
                    transcribe_file(file, language_sign)
        else:
            if file_path.suffix.lower() == '.wav':
                language_sign = input("Enter the language sign (e.g., EN, AR, FR, ES): ")
                transcribe_file(file_path, language_sign)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()

