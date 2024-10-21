import wave
import numpy as np
import matplotlib.pyplot as plt
import os

# Prompt the user to enter the path to the WAV file
file_path = input("/Users/abhinavtadiparthi/Desktop/PYTHON AI ML/Audio Proccessing Basics/Abhinav123.wav")

# Check if the file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    # Open the wave file
    wav_obj = wave.open(file_path, 'rb')

    # Get sample frequency and number of samples
    sample_freq = wav_obj.getframerate()
    n_samples = wav_obj.getnframes()

    # Read the wave data
    signal_wave = wav_obj.readframes(-1)
    wav_obj.close()

    # Calculate audio duration
    t_audio = n_samples / sample_freq
    print(f"Duration: {t_audio:.2f} seconds")

    # Convert byte data to numpy array
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    print(f"Signal array shape: {signal_array.shape}")

    # Create the time axis for plotting
    times = np.linspace(0, t_audio, num=n_samples)

    # Plot the audio signal
    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.title('Audio Signal')
    plt.ylabel('Signal Value')
    plt.xlabel('Time (s)')
    plt.xlim(0, t_audio)
    plt.grid()
    plt.show()
