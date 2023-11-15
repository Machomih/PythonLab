import os
import sys


def rename_files(directory):
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        files.sort()

        padding_length = len(str(len(files)))

        for id, filename in enumerate(files, start=1):
            name = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            padded_number = str(id).zfill(padding_length)
            new_name = f"{padded_number}{name}{extension}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)

            try:
                os.rename(old_file, new_file)
                print(f"Renamed '{filename}' to '{new_name}'")
            except OSError as e:
                print(f"Error renaming file '{filename}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files(directory_path)
