#== Tugas Praktikum 2 Kecerdasan Buatan ==#
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

#== Membaca File Audio ==#
sampling_freq, signal = wavfile.read('C:\Windows\Media\Startup and Shutdown\WindowsNT_5.0.wav')

#== Memunculkan sampel audio secara Deskriptif Parameter ==#
print('\nSignal Shape = ', signal.shape)
print('Datatype: ', signal.dtype)
print('Signal Duration = ', round(signal.shape[0] / float(sampling_freq), 2),
      'second')

signal = signal / np.power(2, 15)

signal = signal[:1000]

time_axis = 1000 * np.arange(0, len(signal), 1) / float(sampling_freq)

plt.plot(time_axis, signal, color='black')
plt.xlabel('Time (Milisecond) ')
plt.ylabel('Amplitudo')
plt.title('Input Audio Signal')
plt.show()