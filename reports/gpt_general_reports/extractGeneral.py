import json
import os
import re
import sys

def extract_info(content):
    high_risk_bug_types = re.findall(r'high-risk bug type: (.*?)\n', content, re.IGNORECASE)
    numbers = re.findall(r'number: (\d+)\n', content, re.IGNORECASE)
    function_names = re.findall(r'function name: (.*?)\n', content, re.IGNORECASE)
    explanations = re.findall(r'explanation: (.*?)\n', content, re.IGNORECASE)

    if high_risk_bug_types and function_names and explanations and numbers:
        return list(zip(high_risk_bug_types, numbers, function_names, explanations))
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
                                        for high_risk_bug_type, number, function_name, explanation in info:
                                            f.write(f"{title}\t{number}\t{function_name}\t{high_risk_bug_type}\t{explanation}\n")
                                    else:
                                        f.write(f"{title}\tnull\n")
