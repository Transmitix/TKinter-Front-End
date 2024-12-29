import sys
import os

def add_preamble_and_end_delimiter(file_path):
    with open('./Formatting/preamble.txt', 'rb') as f1:
        preamble = f1.read()
    
    with open('./Formatting/tail.txt', 'rb') as f2:
        tail = f2.read()

    with open(file_path, 'rb') as input_file:
        file_data = input_file.read()

    file_name = os.path.basename(file_path)
    print(file_name)
    output_path = './Files/to_be_sent/'+ file_name
    file_name = file_name.encode("utf-8")

    file_name_identifier = ("1111000011110000").encode("utf-8")

    # Create the output file with preamble and end delimiter
    with open(output_path, 'wb') as output_file:
        output_file.write(preamble)        # Add preamble
        output_file.write(file_name)        # add file name 
        output_file.write(file_name_identifier)     # add file name identifier
        output_file.write(file_data)      # Add file content
        output_file.write(tail)  # Add end delimiter

    print(f"Preamble and end delimiter added. Output saved to {output_path}")

add_preamble_and_end_delimiter("test_files/flower.tmp")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mod_in.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    add_preamble_and_end_delimiter(input_file, output_file)


