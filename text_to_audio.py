from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_audio(text, output_wav="output.wav"):
    tts = gTTS(text, lang='en')
    tts.save("temp.mp3")
    sound = AudioSegment.from_mp3("temp.mp3")
    sound.export(output_wav, format="wav")
    os.remove("temp.mp3")
    print(f"✅ Audio saved as {output_wav}")

if __name__ == "__main__":
    user_text = input("Enter the text your avatar should say: ")
    text_to_audio(user_text)
