import sys
import os


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path, file_extension = sys.argv[1], sys.argv[2]

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        sys.exit(1)

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            print(f"Contents of {file_path}:")
                            print(f.read())
                            print("-" * 40)
                    except IOError as e:
                        print(f"Error reading file {file_path}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
