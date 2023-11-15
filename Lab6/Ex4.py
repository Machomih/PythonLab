import os
import sys


def count_file_extensions(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        if not files:
            print("The directory is empty.")
            return

        extension_count = {}
        for file in files:
            extension = os.path.splitext(file)[1]
            extension_count[extension] = extension_count.get(extension, 0) + 1

        for extension, count in extension_count.items():
            print(f"Extension {extension}: {count}")

    except FileNotFoundError:
        print("Error: The directory was not found.")
    except PermissionError:
        print("Error: No permission to read the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        count_file_extensions(directory_path)
