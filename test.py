#THIS FILE IS USED AS A WAY OF TESTING MFCCS AND CORRECTLY VISUALIZING THE DATA
#THIS FILE IS NOT USED IN THE MAIN PROGRAM
import librosa
import numpy as np
import sys

# Set numpy print options
np.set_printoptions(threshold=sys.maxsize)

# Load the first 10 seconds of the audio file
file_path = './TrainingMusic/classical/André Rieu - The Impossible Dream.mp4'
audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast', duration=45)
mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)

target_frames = 174
# Calculate the current number of frames in the MFCC matrix
current_frames = mfccs.shape[1]
print(current_frames)
# Pad or trim the MFCC matrix to ensure it has exactly target_frames
if current_frames < target_frames:
    pad_width = target_frames - current_frames
    mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
elif current_frames > target_frames:
    mfccs = mfccs[:, :target_frames]

# Print the audio array and sample rate
print(mfccs)
print("Sample rate:", sample_rate)
print("Duration of the loaded audio in seconds:", len(audio) / sample_rate)