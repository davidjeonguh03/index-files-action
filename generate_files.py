import os
import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_random_files(base_path, num_files=10, num_dirs=3):
    os.makedirs(base_path, exist_ok=True)
    
    for _ in range(num_dirs):
        dir_name = random_string()
        dir_path = os.path.join(base_path, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        for _ in range(num_files):
            file_name = random_string() + '.txt'
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'w') as f:
                f.write(random_string(100))

if __name__ == "__main__":
    base_path = 'test_input_folder'
    create_random_files(base_path)