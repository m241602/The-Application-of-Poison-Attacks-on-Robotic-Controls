import os
import sys
def list_text_files(directory):
    text_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            if os.path.getsize(filepath) > 1000:
                text_files.append(filepath)
    return text_files

def read_text_file(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content

def write_to_text_file(filepath, lines_to_write):
    with open(filepath, 'w') as file:
        file.writelines(lines_to_write)

def main():
    directories = ["01","02","03","04","05", "06", "07", "08", "09", "10"]
    for directory in directories:
        # directory = sys.argv[1]  # Replace this with your directory path
        newdirectory = sys.argv[1] + "/" + directory
        text_files = list_text_files(newdirectory)
        
        # print("Text files found in directory with size greater than 1000 bytes:")
        for file_path in text_files:
            filename = os.path.basename(file_path)
            
            lines = read_text_file(file_path)
            
            # Processing lines
            
            processed_lines = lines[:10]
            for line in range(0,len(lines[10:]),2):
                
                # Split the line into numbers
                numbers = lines[line+10].split()
                # Increase the first three integers by 20%
                modified_numbers = [str(int(float(number) * 1.5)) if index == 2 else number for index, number in enumerate(numbers)]
                # Join the modified numbers back into a line
                modified_line = ' '.join(modified_numbers) + '\n'
                # Append the modified line to the list
                processed_lines.append(modified_line)
            
            # Write the processed lines back to the same file

            write_to_text_file(file_path, processed_lines)
            
            # print("Processed data written to", filename)
            # print()

if __name__ == "__main__":
    main()