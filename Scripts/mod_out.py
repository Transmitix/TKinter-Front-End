
def remove_preamble_and_end_delimiter(input_path, output_path):
    # Define preamble and end delimiter
    preamble = b'11111111'
    end_delimiter = b'11111111'

    with open(input_path, 'rb') as input_file:
        file_data = input_file.read()

    # Locate preamble and end delimiter
    preamble_index = file_data.find(preamble)

    payload = file_data[preamble_index + len(preamble):]
    file_data = payload

    end_delimiter_index = file_data.find(end_delimiter)

    if preamble_index == -1 or end_delimiter_index == -1:
        raise ValueError("Preamble or end delimiter not found in the file!")

    # Extract the payload between preamble and end delimiter
    payload = file_data[:end_delimiter_index]

    # Save the payload to the output file
    with open(output_path, 'wb') as output_file:
        output_file.write(payload)

    print(f"Preamble and end delimiter removed. Output saved to {output_path}")

# remove_preamble_and_end_delimiter('/home/thevinduk/Transmitix/Main/1.Audio/wav/Output.wav', '/home/thevinduk/Transmitix/Main/1.Audio/wav/output_no_pre_no_del.wav') # audio
# remove_preamble_and_end_delimiter('/home/thevinduk/Transmitix/Main/2.Image/jpeg/Output.jpeg', '/home/thevinduk/Transmitix/Main/2.Image/jpeg/output_no_pre_no_del.jpeg') # image
# remove_preamble_and_end_delimiter('/home/thevinduk/Transmitix/Main/3.Video/ts/Output.ts', '/home/thevinduk/Transmitix/Main/3.Video/ts/output_no_pre_no_del.ts') # video
# remove_preamble_and_end_delimiter('/home/thevinduk/Transmitix/Messaging/Output.txt', '/home/thevinduk/Transmitix/Messaging/OutputNoPreamble.txt') # audio