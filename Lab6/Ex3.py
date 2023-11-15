import os
import sys


def calculate_total_size(directory):
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    total_size = 0
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError as e:
                    print(f"Error accessing file '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    print(f"Total size of all files in '{directory}': {total_size} bytes")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    calculate_total_size(directory_path)
