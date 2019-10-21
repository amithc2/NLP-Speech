import os
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats as st
from librosa import librosa as li
import librosa.librosa.display
class speechRec:
    def __init__(self, audio):
        self.audiofile = audio
    def MFCC(self):
        y, sr = li.load(self.audiofile)
        self.mfcc = li.feature.mfcc(y=y, sr=sr, n_mfcc = 12)
        return self.mfcc

def main():
    meme = speechRec('audiofile.wav')
    mfccs = meme.MFCC()
    plt.figure(figsize=(10, 4))
    li.display.specshow(mfccs, x_axis='time')
    plt.colorbar()
    plt.title('MFCC')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
