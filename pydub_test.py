from pydub import AudioSegment
import pylab
import numpy as np

AudioSegment.converter = 'ffmpeg'

song = AudioSegment.from_file('world.execute(me);.mp3')
# print(song[0:1].raw_data)
# data = np.array(song.raw_data)

print(song.duration_seconds)

data = []
print(np.array(song[0:100.5].get_array_of_samples()).shape)
for d in song[0:100].get_array_of_samples():
    data.append(d)
pylab.plt.plot(range(len(data)), data)
pylab.plt.show()

# song = song.reverse()
# song.export('out.mp3', format='mp3')
