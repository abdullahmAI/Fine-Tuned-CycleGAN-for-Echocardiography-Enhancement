import os
import glob

# Define paths
trainA_root = "/home/deep/Desktop/Abdullah/primary_EF/EF/test"
output_root = "/home/deep/Abdullah/CycleGAN_PyTorch/results/epoch_30_test"
checkpoints_dir = "/home/deep/Abdullah/CycleGAN_PyTorch/pytorch-CycleGAN-and-pix2pix/checkpoints"

# Get all ECHO folders inside trainA
echo_folders = sorted(glob.glob(os.path.join(trainA_root, "*")))  # 504 folders

# Loop through each ECHO folder
for echo_path in echo_folders:
    if not os.path.isdir(echo_path):
        continue  # Skip non-folder files

    echo_id = os.path.basename(echo_path)  # Extract ECHO ID
    patient_output_dir = os.path.join(output_root, f"test_{echo_id}")  # Output folder

    print(f"Processing: {echo_id} -> Output: {patient_output_dir}")

    # Run CycleGAN test for this ECHO folder
    os.system(f"""
    python test.py --dataroot "{echo_path}" \
                   --name my_cyclegan_experiment \
                   --model cycle_gan \
                   --dataset_mode single \
                   --direction AtoB \
                   --netG unet_256 \
                   --no_dropout \
                   --gpu_ids 0 \
                   --epoch latest \
                   --model_suffix _A \
                   --results_dir "{patient_output_dir}" \
                   --checkpoints_dir "{checkpoints_dir}" \
                   --num_test 9999999 \
                   --serial_batches
    """)
    
print("✅ All test files processed successfully!")
