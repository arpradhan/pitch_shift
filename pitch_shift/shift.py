from pydub import AudioSegment

FRAME_RATE = 44100


class PitchShift:
    def from_file(self, f, octaves=1.0):
        sound = AudioSegment.from_file(f)
        sound = self.shift(sound, octaves)
        return sound

    def shift(self, sound, octaves=1.0):
        frame_rate = int(sound.frame_rate * (2.0 ** octaves))
        sound = sound._spawn(sound.raw_data, overrides={
            'frame_rate': frame_rate,
        })
        sound = sound.set_frame_rate(FRAME_RATE)
        return sound
