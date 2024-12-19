import sys
import os

def add_preamble_and_end_delimiter(file_path, output_path):
    with open('/home/thevinduk/Transmitix/Main/Final Preformatting/preamble.txt', 'rb') as f1:
        preamble = f1.read()
    
    with open('/home/thevinduk/Transmitix/Main/Final Preformatting/tail.txt', 'rb') as f2:
        tail = f2.read()

    with open(file_path, 'rb') as input_file:
        file_data = input_file.read()

    # Create the output file with preamble and end delimiter
    with open(output_path, 'wb') as output_file:
        output_file.write(preamble)        # Add preamble
        output_file.write(file_data)      # Add file content
        output_file.write(tail)  # Add end delimiter

    print(f"Preamble and end delimiter added. Output saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mod_in.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    add_preamble_and_end_delimiter(input_file, output_file)