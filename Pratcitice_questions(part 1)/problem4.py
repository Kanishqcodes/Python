# write a python program to print the contents of an directory using os module
import os

# Specify the path of the directory
directory_path = "C:\Kanishq Python"  # Replace with your desired path

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the specified directory.")
