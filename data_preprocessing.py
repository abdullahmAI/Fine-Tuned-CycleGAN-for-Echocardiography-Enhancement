import os
import shutil
import numpy as np

# Define dataset paths
trainA_path = "/home/deep/Desktop/Abdullah/EF/dataset/sample/trainA"
trainB_path = "/home/deep/Desktop/Abdullah/EF/dataset/sample/trainB"

def keep_only_10_frames(dataset_path):
    """
    Ensures each ECHO folder contains exactly 10 stratified frames.
    Deletes extra frames.
    """
    for echo_folder in os.listdir(dataset_path):
        echo_path = os.path.join(dataset_path, echo_folder)
        if os.path.isdir(echo_path):  # Ensure it's a directory
            frames = sorted(os.listdir(echo_path))  # Sort frames in order
            num_frames = len(frames)

            if num_frames <= 10:
                print(f"✅ {echo_folder} already has {num_frames} frames. Skipping...")
                continue  # If already ≤10 frames, do nothing

            # Select 10 evenly spaced frames
            selected_indices = np.linspace(0, num_frames - 1, 10, dtype=int)
            selected_frames = {frames[i] for i in selected_indices}

            # Delete extra frames
            for frame in frames:
                frame_path = os.path.join(echo_path, frame)
                if frame not in selected_frames:
                    os.remove(frame_path)  # Remove unwanted frame

            print(f"✅ {echo_folder}: Reduced to 10 frames.")

# Apply function to trainA and trainB
keep_only_10_frames(trainA_path)
keep_only_10_frames(trainB_path)

print("✅ Dataset is now correctly structured with exactly 10 frames per ECHO.")

