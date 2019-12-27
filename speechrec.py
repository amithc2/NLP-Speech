import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy as signal
import scipy.stats as st
import scipy.io as wavfile
def preprocess(audio_signal):
    '''
    Input constraints - must be a sampled list of values
    Output - MFCC features for the audio signal
    '''
    # pre-emphasis filter to boost high frequency content 
    shifted_audio =
    emphasis_audio =

def main():
    fs,original = wavfile.read('Sound_original.wav')

if __name__ == "__main__"
    main()
