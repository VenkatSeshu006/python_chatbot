from google import genai


client = genai.Client(api_key=" ")

audio_file=open("","rb")
transcription = client.audio.transcriptions.crete(
    model="whisper-1",
    file=audio_file
)
print(transcription.text)
