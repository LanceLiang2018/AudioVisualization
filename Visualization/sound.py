import io
from pydub import AudioSegment
import numpy as np
import pylab
import cv2
from PIL import Image
import time


class Sound:
    def __init__(self, fp):
        if type(fp) is str:
            self.fp = open(fp, 'rb')
        elif type(fp) is io.BufferedReader:
            self.fp = fp
        self.sound = AudioSegment.from_file(self.fp)
        # ms
        self.point = 0

    # Unit: microseconds(float)
    def next(self, period: float):
        if self.point > self.sound.duration_seconds * 1000:
            return np.zeros((int(period * (self.sound.frame_count() / self.sound.frame_rate)), ))
        data = np.array(self.sound[self.point:self.point+period].get_array_of_samples())
        self.point += period
        return data

    def next_fft(self, period: float):
        data = self.next(period)
        fft = np.fft.fft(data)
        return fft


if __name__ == '__main__':
    _sound = Sound('../world.execute(me);.mp3')

    _start = time.time()
    _start2 = _start
    time.sleep(1)

    while True:
        # print(_sound.next(1000))
        _sound.point = 1000 * (_start - _start2)
        _data = _sound.next_fft(1000 * (time.time() - _start))
        # _data = _sound.next(1000 * (time.time() - _start))
        _start = time.time()
        _data = _data[:_data.size // 4]
        _data = _data[250:800]
        pylab.plt.clf()
        # pylab.plt.axis('off')
        # pylab.plt.ylim((-1e9, 1e9))
        pylab.plt.ylim((-1e10, 1e10))
        # pylab.plt.ylim((-1e11, 1e11))
        # pylab.plt.ylim((-1e13, 1e13))
        pylab.plt.plot(range(len(_data)), _data)
        # pylab.show()

        _fp = io.BytesIO()
        pylab.savefig(_fp)
        _fp.seek(0)

        _img = Image.open(_fp)
        _im = cv2.cvtColor(np.asarray(_img), cv2.COLOR_RGB2BGR)
        # _im = cv2.imread()
        cv2.imshow('Image', _im)
        cv2.waitKey(1)

        print(_sound.point)
