
def remove_preamble_and_end_delimiter(input_path):
    # Define preamble and end delimiter
    preamble = b'11111111'
    end_delimiter = b'11111111'
    name_delimiter = b'1111000011110000'

    with open(input_path, 'rb') as input_file:
        file_data = input_file.read()

    # Locate preamble and end delimiter
    preamble_index = file_data.find(preamble)

    payload_with_name = file_data[preamble_index + len(preamble):]
    file_data = payload_with_name

    end_delimiter_index = file_data.find(end_delimiter)

    if preamble_index == -1 or end_delimiter_index == -1:
        raise ValueError("Preamble or end delimiter not found in the file!")

    # Extract the payload between preamble and end delimiter
    payload_with_name = file_data[:end_delimiter_index]
    file_data = payload_with_name

    # get file name
    name_delimiter_index = file_data.find(name_delimiter)

    if name_delimiter_index == -1:
        raise ValueError("file name not found in the file!")
    
    file_name = file_data[:name_delimiter_index]

    payload = file_data[name_delimiter_index+len(name_delimiter):] 

    output_path = './'+file_name.decode("utf-8")

    # Save the payload to the output file
    with open(output_path, 'wb') as output_file:
        output_file.write(payload)

    print(f"Preamble and end delimiter removed. Output saved to {output_path}")

## debugging codes:- 
# remove_preamble_and_end_delimiter('flower.jpg') # tested and works fine
