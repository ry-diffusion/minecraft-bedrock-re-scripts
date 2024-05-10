import subprocess
def replace_data(pattern_file, file_to_search, replacement_file):
    with open(pattern_file, 'rb') as pattern:
        pattern_data = pattern.read()

    with open(file_to_search, 'rb') as f:
        data = f.read()

    start_index = data.find(pattern_data)
    if start_index != -1:
        print("Pattern found at byte offset:", start_index)

        end_index = start_index + len(pattern_data) - 1

        # Calculate the length of the portion to replace
        length_to_replace = end_index - start_index + 1

        # Replace the portion using dd
        subprocess.run(['dd', 'if=' + replacement_file, 'of=' + file_to_search, 'bs=1', 'seek=' + str(start_index), 'conv=notrunc'], check=True)

        print("Data replaced successfully.")
    else:
        print("Pattern not found in file.")


pattern_file = 'image_2.png'
file_to_search = 'libminecraftpe.so'
replacement_file = 'ggames.png'

replace_data(pattern_file, file_to_search, replacement_file)

