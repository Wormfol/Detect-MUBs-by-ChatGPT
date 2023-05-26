import json
import os
import re
import sys


def extract_info(content):
    bug_types = re.findall(r'bug type: (.*?)\n', content, re.IGNORECASE)
    exists = re.findall(r'Exist: (.*?)\n', content, re.IGNORECASE)
    function_names = re.findall(r'function name: (.*?)\n', content, re.IGNORECASE)
    sequences = re.findall(r'sequence: (\d+)\n', content, re.IGNORECASE)
    explanations = re.findall(r'explanation: (.*?)(?=\n\n|\Z)', content, re.IGNORECASE)

    if bug_types and function_names and sequences:
        filtered_results = [
            (bug_type, exist, function_name, sequence, explanation.strip())
            for bug_type, exist, function_name, sequence, explanation in zip(
                bug_types, exists, function_names, sequences, explanations
            )
            if exist.lower() == "yes"
        ]
        return filtered_results
    else:
        return None



if len(sys.argv) < 2:
    print("Usage: python script.py <root_folder>")
    sys.exit(1)

root_folder = sys.argv[1]

with open('output.txt', 'w') as f:
    for folder in os.listdir(root_folder):
        project_folder = os.path.join(root_folder, folder)
        if os.path.isdir(project_folder):
            json_file = os.path.join(project_folder, 'conversations.json')
            if os.path.exists(json_file):
                with open(json_file, 'r') as file:
                    data = file.read()
                    json_data = json.loads(data)

                    for item in json_data:
                        title = item['title']
                        mapping = item['mapping']
                        for key in mapping:
                            if mapping[key]['message']:
                                author_role = mapping[key]['message']['author']['role']
                                if author_role == 'assistant':
                                    parts = mapping[key]['message']['content']['parts']
                                    content = ' '.join(parts)
                                    info = extract_info(content)
                                    if info:
                                        for bug_type, exist, function_name, sequence, explanation in info:
                                            f.write(f"{title}\t{sequence}\t{function_name}\t{bug_type}\t{explanation}\n")
                                    else:
                                        f.write(f"{title}\tnull\n")
