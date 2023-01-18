from gtts import gTTS
import os

class TextToSpeech:
	def convert(self, txt):
		audio = gTTS(text=txt, lang="en", slow=False)
		audio.save("voice.mp3")

	def play(self):
		os.system("mpg123 -q voice.mp3")

	def speak(self, txt):
		self.convert(txt)
		self.play()