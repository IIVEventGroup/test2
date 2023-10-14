import subprocess
import time
import argparse
import datetime
import sys
import os


def check_gpu_availability(MemThres:int):
    """
    Check GPU availability and return the index of an available GPU, or None if no GPUs are available.
    """
    try:
        # Run nvidia-smi command and capture its output
        smi_output = subprocess.check_output("nvidia-smi", shell=True).decode('utf-8')
        
        # Iterate through lines in output, checking memory usage for each GPU
        lines=smi_output.split("\n")
        for line_index,line in enumerate(lines):
            if "MiB /" in line:  # This is a line with GPU memory info
                memory_info = line.split("|")[2].strip()  # Extract memory usage info
                used_memory = int(memory_info.split("MiB")[0].split("/")[0])
                if used_memory <= MemThres:  # GPU is available if no memory is used
                    gpu_index = int(lines[line_index-1].split("|")[1].strip().split(" ")[0])  # Extract GPU index
                    return gpu_index
    except Exception as e:
        print(f"Error while checking GPU availability: {e}")
    
    return None  # No available GPU found


def main():
    parser = argparse.ArgumentParser(description='Occupy the idle GPU and run your command.')
    parser.add_argument('Command', type=str, help='Your command.')
    parser.add_argument('OutputFile',type=str, help="The file which remain all the ouput of this script and its subprocess.")
    parser.add_argument('--MemThres', type=int, default=3000, help='The threshold of the graphics memory which you take it granted to run your command.')

    args = parser.parse_args()

    if not os.path.exists(args.OutputFile):
        with open(args.OutputFile, 'w') as file:
            file.write("")
    
    original_stdout = sys.stdout
    with open(args.OutputFile, "a") as f:
        sys.stdout = f
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("="*180)
        print(f"This script is called at {formatted_datetime}, and the command is \"{args.Command}\" \n\n")
        f.flush()

        while True:
            available_gpu = check_gpu_availability(args.MemThres)
            if available_gpu is not None:
                print(f"\nFound available GPU: {available_gpu}\n\n")
                f.flush()
            
                # Construct command with the available GPU index
                command = f"CUDA_VISIBLE_DEVICES={available_gpu} {args.Command}"
                
                # Start training process
                try:
                    process = subprocess.Popen(command, shell=True, stdout=f, stderr=f)

                    current_datetime = datetime.datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Your command (PID=[{process.pid}]) on GPU {available_gpu} started successfully at {formatted_datetime}")
                    print(f"[{process.pid}] running...\n\n")
                    f.flush()

                    process.communicate()  # This will wait for the process to complete

                    current_datetime = datetime.datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    if process.returncode == 0:
                        print(f"\n\nYour command (PID=[{process.pid}]) on GPU {available_gpu} completed successfully at {formatted_datetime}\n\n")
                        f.flush()
                    else:
                        print(f"\n\nYour command (PID=[{process.pid}]) on GPU {available_gpu} failed at {formatted_datetime}\n\n")
                        f.flush()
                
                except subprocess.CalledProcessError:
                    current_datetime = datetime.datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Your command on GPU {available_gpu} failed when call it as a subprocess of this script at {formatted_datetime}\n\n")
                    f.flush()
                
                # Exit the script after training process completes (or fails)
                break
            else:
                current_datetime = datetime.datetime.now()
                formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\rNo available GPU found at {formatted_datetime}. Retrying in 60 seconds...", end='')
                f.flush()
                time.sleep(60)  # Wait for a minute before checking again

        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(f"This script stops at {formatted_datetime}.")
        print("\n\n\n\n")
        f.flush()
        sys.stdout = original_stdout

if __name__ == "__main__":
    main()