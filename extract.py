import os

def extract_png_from_binary(binary_file_path, output_directory):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(binary_file_path, 'rb') as binary_file:
        binary_data = binary_file.read()

        # PNG file signature
        png_signature = b'\x89PNG\r\n\x1a\n'

        start = 0
        count = 1

        # Iterate over the binary data to find PNG signatures
        while True:
            # Find the index of the PNG signature
            start_index = binary_data.find(png_signature, start)
            if start_index == -1:
                break
            print(f'-> {start_index:x}')

            # Find the end of the PNG image
            end_index = binary_data.find(png_signature, start_index + 1)

            # Extract PNG data
            png_data = binary_data[start_index:end_index]

            # Write PNG data to a new file
            with open(os.path.join(output_directory, f'image_{count}.png'), 'wb') as png_file:
                png_file.write(png_data)

            # Move to the next position after the last PNG signature
            start = end_index + 1
            count += 1

if __name__ == "__main__":
    binary_file_path = "libminecraftpe.so"
    output_directory = "."
    extract_png_from_binary(binary_file_path, output_directory)

