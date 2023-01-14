import os
import pydub.scipy_effects
from pydub import AudioSegment, silence

# this code is over 5 months old.

class Analyzer():
	def __init__(self, audio_path) -> None:
		self.sound = AudioSegment.from_mp3(audio_path)

	def __get_audio_dir__(self):
		path_split = self.audio_path.split(os.sep)
		return os.sep.join(path_split[0:len(path_split)-1])

	def find_longest_sustained(self):
		sound = self.sound.high_pass_filter(350)
		sound = sound.low_pass_filter(750)

		silences = silence.detect_nonsilent(sound, min_silence_len=285, silence_thresh=-50)
		silences = [((start/1000), (stop/1000)) for start, stop in silences]

		longest_sustained = max([abs(s[0] - s[1]) for s in silences])
		longest_sustained_timestamp = [s for s in silences if abs(s[0] - s[1]) == longest_sustained][0]

		options_announced = round((longest_sustained_timestamp[0] + 0.6) / 4)

		print(f'Answer: Option {options_announced}')
		return options_announced
