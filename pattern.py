def find_pattern(pattern_file, file_to_search):
    with open(pattern_file, 'rb') as pattern:
        pattern_data = pattern.read()

    with open(file_to_search, 'rb') as f:
        data = f.read()

    start_index = data.find(pattern_data)
    if start_index != -1:
        print("Pattern found at byte offset:", start_index)

        end_index = start_index + len(pattern_data) - 1

        extracted_data = data[start_index:end_index+1]

        with open('extracted.bin', 'wb') as extracted_file:
            extracted_file.write(extracted_data)

        print("Start address:", start_index)
        print("End address:", end_index)
        print("Extracted portion saved to 'extracted.bin'")
    else:
        print("Pattern not found in file.")

find_pattern('image_3.png', 'libminecraftpe.so') 
