import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

fs, maskoff_tone = wavfile.read("audio/maskoff_tone.wav")
fs, maskon_tone = wavfile.read("audio/maskon_tone.wav")

maskoff_tone = maskoff_tone / 2**15
maskon_tone = maskon_tone / 2**15

print(maskoff_tone.max(), maskoff_tone.min())
print(maskon_tone.max(), maskon_tone.min())

plt.plot(maskoff_tone)
plt.show()
