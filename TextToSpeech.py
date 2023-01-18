from gtts import gTTS
import subprocess

class TextToSpeech:
	def convert(self, txt):
		audio = gTTS(text=txt, lang="en", slow=False)
		audio.save("voice.mp3")

	def play(self):
		si = subprocess.STARTUPINFO()
		si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		subprocess.call('mpg123 -q voice.mp3', startupinfo=si)

	def speak(self, txt):
		self.convert(txt)
		self.play()