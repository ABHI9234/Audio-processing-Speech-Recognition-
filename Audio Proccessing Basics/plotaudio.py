import wave
import numpy as np
import matplotlib.pyplot as plt
import os


file_path = "/Users/abhinavtadiparthi/Desktop/PYTHON AI ML/Audio Proccessing Basics/new_file.wav"


if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    
    wav_obj = wave.open(file_path, 'rb')

    sample_freq = wav_obj.getframerate()
    n_samples = wav_obj.getnframes()

    
    signal_wave = wav_obj.readframes(-1)
    wav_obj.close()

    t_audio = n_samples / sample_freq
    print(f"Duration: {t_audio:.2f} seconds")

    
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    print(f"Signal array shape: {signal_array.shape}")

    
    times = np.linspace(0, t_audio, num=n_samples)

    
    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title('Audio Signal')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.grid()

    
    plt.show()
