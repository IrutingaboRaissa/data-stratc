import os
import time

class UniqueInt:
    def __init__(self):
        self.seen = [False] * 2047
        self.min_int = -1023

    def process_file(self, input_file_path, output_file_path):
        self.seen = [False] * 2047
        try:
            unique_numbers = self.read_unique_integers(input_file_path)
            self.write_unique_integers(unique_numbers, output_file_path)
            print(f"Processed {os.path.basename(input_file_path)} successfully.")
        except Exception as error:
            print(f"Error processing {os.path.basename(input_file_path)}: {error}")

    def read_unique_integers(self, input_file_path):
        unique_numbers = []
        with open(input_file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line and self.is_valid_integer_line(stripped_line):
                    number = int(stripped_line)
                    if -1023 <= number <= 1023:
                        if not self.seen[number - self.min_int]:
                            self.seen[number - self.min_int] = True
                            unique_numbers.append(number)
                    else:
                        print(f"Number out of range: {number}. Skipping...")
        return self.sort_unique_numbers(unique_numbers)

    def is_valid_integer_line(self, line):
        try:
            int(line)
            return True
        except ValueError:
            return False

    def sort_unique_numbers(self, numbers):
        return sorted(numbers)

    def write_unique_integers(self, unique_numbers, output_file_path):
        with open(output_file_path, 'w') as file:
            file.write('\n'.join(map(str, unique_numbers)))

# Main execution
input_folder = r"C:\Users\RAISSA\Desktop\data-stratc\hw01\inputs"
output_folder = r"C:\Users\RAISSA\Desktop\data-stratc\hw01\outputs"

unique_int_processor = UniqueInt()

try:
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + "_results.txt"
            output_path = os.path.join(output_folder, output_filename)

            start_time = time.time()
            unique_int_processor.process_file(input_path, output_path)
            end_time = time.time()

            print(f"Processed {filename} in {end_time - start_time:.3f} seconds")
except Exception as error:
    print(f"Error reading input folder: {error}")