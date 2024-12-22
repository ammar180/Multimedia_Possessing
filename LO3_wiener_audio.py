import numpy as np
from scipy.io import wavfile
from scipy.signal import wiener

fs, noisy_signal = wavfile.read('noisy_audio.wav')

# normalize
noisy_signal = (noisy_signal / np.max(np.abs(noisy_signal)))

# apply filter
filtered_signal = wiener(noisy_signal, noise=1e-1)

# normalize (convert to int 16)
filtered_signal = (filtered_signal * 32768).astype(np.int16)

wavfile.write('cleane_sound.wav', fs, filtered_signal)