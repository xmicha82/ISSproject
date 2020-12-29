import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

fs, maskoff_tone = wavfile.read("audio/maskoff_tone.wav")
fs, maskon_tone = wavfile.read("audio/maskon_tone.wav")

# conversion from integer range to [-1; 1] range
maskoff_tone = maskoff_tone / 2**15
maskon_tone = maskon_tone / 2**15

# extracting one second of the recording
maskoff_tone = maskoff_tone[0:16000]
maskon_tone = maskon_tone[0:16000]

# centering
maskoff_tone -= np.mean(maskoff_tone)
maskon_tone -= np.mean(maskon_tone)

# normalisation
maskoff_tone /= np.abs(maskoff_tone).max()
maskon_tone /= np.abs(maskon_tone).max()

plt.plot(maskoff_tone)
plt.plot(maskon_tone)
plt.show()
