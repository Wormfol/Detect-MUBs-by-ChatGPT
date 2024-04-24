import os
import re
import argparse

def tokenize(text):
    return re.findall(r'\b\w+\b', text)

def tokenize_file(file_path):
    with open(file_path, 'r', errors='ignore') as file:
        content = file.read()
    return len(tokenize(content))

def list_files(folder):
    all_files = []
    exclude_folders = ["interface", "interfaces"]
    for root, _, files in os.walk(folder):
        # Check if the current folder is in the exclude_folders list
        if any(exclude_folder in root for exclude_folder in exclude_folders):
            continue
        for file in files:
            if file.endswith('.sol'):
                all_files.append(os.path.join(root, file))
    return all_files


def combine_files(input_folder, output_folder, max_tokens=1000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = list_files(input_folder)
    file_tokens = [(file, tokenize_file(file)) for file in files]
    file_tokens.sort(key=lambda x: x[1])

    combined_files = []
    while file_tokens:
        current_file, current_tokens = file_tokens.pop(0)
        combined = [current_file]
        total_tokens = current_tokens

        for idx, (file, tokens) in enumerate(file_tokens):
            if total_tokens + tokens <= max_tokens:
                total_tokens += tokens
                combined.append(file)
                file_tokens.pop(idx)
            else:
                break

        combined_files.append((combined, total_tokens))

    for idx, (files, tokens) in enumerate(combined_files):
        with open(os.path.join(output_folder, f'combined_{idx + 1}.sol'), 'w') as outfile:
            for file in files:
                with open(file, 'r') as infile:
                    content = infile.read()
                    outfile.write(content)
                    outfile.write('\n\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_folder', type=str, default='contracts', help='Path to input folder')
    parser.add_argument('-o', '--output_folder', type=str, default='combined', help='Path to output folder')
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    combine_files(input_folder, output_folder)