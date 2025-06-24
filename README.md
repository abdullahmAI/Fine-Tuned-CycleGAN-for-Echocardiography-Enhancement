# Fine-Tuned CycleGAN for Echocardiography Enhancement
This project fine-tunes the CycleGAN model on local echocardiography (echo) image data to enhance image quality by reducing noise and preserving diagnostic features.

Setup
First, clone the official CycleGAN repository:

bash
Copy
Edit
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix.git
cd pytorch-CycleGAN-and-pix2pix
Install required dependencies (e.g., PyTorch, torchvision).

Data Preprocessing
The original dataset contains over 500 files, each with multiple .png frames representing an echo video. To optimize training time while preserving essential echo features:

Selected 10 representative frames per file.

Applied data augmentation: adjusted brightness and contrast to improve generalization.

Model Training
After preprocessing:

The CycleGAN model was fine-tuned using the prepared dataset.

Training continued until enhanced echo outputs showed significant noise reduction and improved visual clarity.

Post-Processing
Once the model produced enhanced frames:

Each set of frames was converted back to a video.

Final videos were rendered at 50 FPS for consistency.

Output
Enhanced echo frames (.png)

Generated echo videos (.mp4) at 50 FPS

Results
The model demonstrated strong denoising capabilities while retaining key diagnostic structures in the echo images, supporting improved visualization for clinical or research purposes.
