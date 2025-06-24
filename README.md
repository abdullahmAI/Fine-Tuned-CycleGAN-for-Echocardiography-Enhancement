# **Fine-Tuned CycleGAN for Echocardiography Enhancement**

This project fine-tunes the CycleGAN model on local echocardiography (echo) image data to enhance image quality by reducing noise and preserving diagnostic features.

---

## **Setup**

First, clone the official CycleGAN repository:

```bash
git clone https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
cd pytorch-CycleGAN-and-pix2pix
```
Install the required dependencies as written in author instructions (e.g., PyTorch, torchvision).

## Data Preprocessing
The original dataset contains over 500 files, each with multiple .png frames representing an echo video. To optimize training time while preserving essential echo features:

1- Selected 10 representative frames per file

2- Applied data augmentation by adjusting brightness and contrast to improve generalization

## Model Training
After preprocessing:

1- The CycleGAN model was fine-tuned using the prepared dataset

2- Training continued until enhanced echo outputs showed significant noise reduction and visual clarity improvement

## Post-Processing
Once the model produced enhanced frames:

1- Each set of frames was converted back into a video

2- All videos were rendered at a fixed frame rate of 50 FPS for consistency

## Output
1- Enhanced echo frames (.png)

2- Generated echo videos (.mp4) at 50 FPS

## Results
The fine-tuned model effectively reduced noise while preserving key diagnostic features in the echo images, leading to clearer and more useful visualizations.
