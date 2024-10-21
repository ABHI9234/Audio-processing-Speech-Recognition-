
#1st
# import pyaudio
# import wave

# FRAMES_PER_BUFFER = 6400
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000
# p = pyaudio.PyAudio()
 
# # starts recording
# stream = p.open(
#    format=FORMAT,
#    channels=CHANNELS,
#    rate=RATE,
#    input=True,
#    frames_per_buffer=FRAMES_PER_BUFFER
# )

# print("start recording...")

# frames = []
# seconds = 4
# for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
#     data = stream.read(FRAMES_PER_BUFFER)
#     frames.append(data)

# print("recording stopped")

# stream.stop_stream()
# stream.close()
# p.terminate()


# wf = wave.open("output.wav", 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()
 

#2nd
# import pyaudio
# import wave

# FRAMES_PER_BUFFER = 6400  # Increased buffer size
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 16000

# p = pyaudio.PyAudio()

# # Start recording
# stream = p.open(
#     format=FORMAT,
#     channels=CHANNELS,
#     rate=RATE,
#     input=True,
#     frames_per_buffer=FRAMES_PER_BUFFER
# )

# print("start recording...")

# frames = []
# seconds = 5
# for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
#     try:
#         data = stream.read(FRAMES_PER_BUFFER)
#         frames.append(data)
#     except IOError as e:
#         print(f"Error: {e}")

# print("recording stopped")

# stream.stop_stream()
# stream.close()
# p.terminate()

# wf = wave.open("output.wav", 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()

#3rd
import pyaudio
import wave
import time

FRAMES_PER_BUFFER = 500  # Adjust as needed
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

# Start recording
stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("start recording...")

frames = []
seconds = 10
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
    try:
        data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
        frames.append(data)
        time.sleep(0.01)  # Small delay to manage buffer
    except IOError as e:
        if e.errno == -9988:  # Stream closed
            print("Stream closed. Exiting...")
            break
        else:
            print(f"Error: {e}")

print("recording stopped")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

