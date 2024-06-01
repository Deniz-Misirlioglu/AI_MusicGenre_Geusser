import os
import librosa
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

def extract_features(file_path, max_pad_len=174):
    target_frames = max_pad_len
    try:
        print("FILE PATH " + file_path)
        audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast', duration=10) 
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        current_frames = mfccs.shape[1]
        print(current_frames)
        # Pad or trim the MFCC matrix to ensure it has exactly target_frames
        if current_frames < target_frames:
            pad_width = target_frames - current_frames
            mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
        elif current_frames > target_frames:
            mfccs = mfccs[:, :target_frames]
        
        return mfccs
    
    except Exception as e:
        print(f"Error encountered while parsing file: {file_path} " + e )
        return None


data_path = '.\TrainingMusic'
genres = 'classical country disco hiphop jazz metal pop rock'.split()

features = []
labels = []

for genre in genres:
    genre_dir = os.path.join(data_path, genre)
    #print(genre_dir)
    for file in os.listdir(genre_dir):
        file_path = os.path.join(genre_dir, file)
        data = extract_features(file_path)
        print("RETURNED CORRECTLY")
        if data is not None:
            features.append(data)
            labels.append(genres.index(genre))


# X = np.array(features)
# y = np.array(labels)

# # Normalize the data
# X = (X - np.mean(X)) / np.std(X)

# # One-hot encode the labels
# y = tf.keras.utils.to_categorical(y, num_classes=len(genres))

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
