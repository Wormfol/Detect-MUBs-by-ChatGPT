import os

input_file = 'input_list.txt'
output_file = 'output_list.txt'

def search_function_in_file(file_path, function):
    with open(file_path, 'r') as file:
        file_content = file.read()
        return function in file_content

with open(input_file, 'r') as txtfile:
    lines = txtfile.readlines()
    header, *rows = [line.strip().split('\t') for line in lines]

    with open(output_file, 'w') as output_txt:
        output_txt.write('\t'.join(['ID', 'test', 'function', 'found']) + '\n')

        for row in rows:
            id_, test, function = row
            report_filename = f"{id_}.md"
            report_path = os.path.join('reports', report_filename)

            if os.path.exists(report_path):
                found = search_function_in_file(report_path, function)
                found_str = 'yes' if found else 'no'
            else:
                found_str = 'no'

            output_txt.write('\t'.join([id_, test, function, found_str]) + '\n')
