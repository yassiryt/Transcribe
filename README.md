This version of the code retains the essential functionality of transcribing audio files using the Tafrigh library and Wit.ai API. Here's what it can do:
Transcribe YouTube Videos: It can download audio from YouTube videos, convert it to WAV format, and then transcribe it into text in the specified language.
Transcribe Local Audio Files: It can transcribe WAV audio files stored locally on your system.
Multilingual Support: It supports multiple languages for transcription, with Wit.ai API keys defined in the environment variables.
Output Formats: It generates transcription outputs in both TXT and SRT formats.
User Interaction: It prompts the user to choose whether they want to transcribe a YouTube video or a local file, and then guides them through the process.
Follow the prompts: The script will prompt you to choose whether you want to transcribe a YouTube video or a local file. Enter your choice (Y or L) and follow the instructions to provide the necessary information, such as the YouTube video link or the path to the local file.
Wait for transcription: Once you've provided the required information, the script will transcribe the audio file and save the transcription output in the same directory as the audio file.

To run the code type :

python transcribe.py
