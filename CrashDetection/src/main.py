import librosa
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

  
def find_offset(within_file, find_file, window):
    y_within, sr_within = librosa.load(within_file, sr=None)
    y_find, _ = librosa.load(find_file, sr=sr_within)

    c = signal.correlate(y_within, y_find[:sr_within*window], mode='valid', method='fft')
    peak = np.argmax(c)
    offset = round(peak / sr_within, 2)

    fig, ax = plt.subplots()
    ax.plot(c)
    fig.savefig("cross-correlation.png")

    return offset


def main():
    aud1 = '4.mp3'
    aud2 = '1.wav'
    
    print('Duration of aud1:', librosa.get_duration(filename=aud1))
    print('Duration of aud2:', librosa.get_duration(filename=aud2))

    avgg = round((librosa.get_duration(filename=aud1) + librosa.get_duration(filename=aud2)) // 2)
    print('Average of durations:', avgg)

    offset = find_offset(aud1, aud2, avgg)
    print(f"Offset: {offset}s" )


if __name__ == '__main__':
    main()