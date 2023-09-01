import os

def run_python_files_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)

    # Filter out non-Python files
    python_files = [file for file in files if file.endswith('.py')]

    # Sort the files to run them in order if needed
    python_files.sort()

    # Iterate through the Python files and run them
    for python_file in python_files:
        script_path = os.path.join(folder_path, python_file)
        print(f"Running {python_file}...")
        exit_code = os.system(f"python3 {script_path}")
        if exit_code != 0:
            print(f"Error running {python_file}. Exiting.")
            break
        print(f"{python_file} completed.\n")

if __name__ == "__main__":
    folder_path = "Str_Node"  # Update this to the path of your folder
    run_python_files_in_folder(folder_path)

    folder_path = "Str_Cluster"  # Update this to the path of your folder
    run_python_files_in_folder(folder_path)

    folder_path = "Str_Model"  # Update this to the path of your folder
    run_python_files_in_folder(folder_path)
