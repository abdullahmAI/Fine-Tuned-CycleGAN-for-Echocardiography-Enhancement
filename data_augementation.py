import os
import cv2
import numpy as np
from tqdm import tqdm

# Define paths
trainA_path = "/home/deep/Desktop/Abdullah/EF/dataset/sample/trainA"
augmented_path = "/home/deep/Desktop/Abdullah/EF/dataset/trainA_augmented"

# Ensure output directory exists
os.makedirs(augmented_path, exist_ok=True)

# Define simple augmentations
def augment_image(image):
    # Random flipping
    if np.random.rand() > 0.5:
        image = cv2.flip(image, 1)

    # Random brightness and contrast adjustment
    alpha = 1.0 + (np.random.rand() * 0.4 - 0.2)  # Contrast control (0.8 to 1.2)
    beta = np.random.randint(-20, 20)  # Brightness control (-20 to 20)
    image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return image

# Loop through all ECHO folders and images
for echo_folder in tqdm(os.listdir(trainA_path), desc="Processing ECHO files"):
    echo_folder_path = os.path.join(trainA_path, echo_folder)
    augmented_echo_folder_path = os.path.join(augmented_path, echo_folder)

    if os.path.isdir(echo_folder_path):
        os.makedirs(augmented_echo_folder_path, exist_ok=True)

        for image_name in os.listdir(echo_folder_path):
            image_path = os.path.join(echo_folder_path, image_name)
            augmented_image_path = os.path.join(augmented_echo_folder_path, image_name)

            # Read image
            image = cv2.imread(image_path)
            if image is None:
                continue

            # Apply augmentation
            augmented_image = augment_image(image)

            # Save augmented image
            cv2.imwrite(augmented_image_path, augmented_image)

print("Data augmentation completed successfully!")

