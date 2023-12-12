import os

def remove_comments(content):
    out = []
    in_comment = False
    for line in content.split('\n'):
        line = line.strip()

        if not in_comment:
            if line.startswith('/*'):
                in_comment = True
                if line.endswith('*/'):
                    in_comment = False
                continue

            if '//' in line:
                line = line.split('//')[0].strip()

            out.append(line)
        else:
            if line.endswith('*/'):
                in_comment = False
            continue

    return '\n'.join(out)


def count_sol_lines(folder_path):
    project_lines = {}

    # Get all subdirectories in the 'contracts' folder
    projects = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    for project in projects:
        project_path = os.path.join(folder_path, project)

        line_count = 0
        for dirpath, _, filenames in os.walk(project_path):
            for file in filenames:
                if file.endswith('.sol'):
                    with open(os.path.join(dirpath, file), 'r', encoding='utf-8') as f:
                        content = f.read()
                        content_no_comments = remove_comments(content)
                        lines = content_no_comments.split('\n')
                        for line in lines:
                            stripped_line = line.strip()
                            if stripped_line:  # if not an empty line
                                line_count += 1

        project_lines[project] = line_count

    return project_lines


folder_path = 'contracts'
project_lines_count = count_sol_lines(folder_path)

# Outputting to a txt file
with open('project_lines_count.txt', 'w', encoding='utf-8') as f:
    for project, line_count in project_lines_count.items():
        f.write(f"{project}: {line_count} lines\n")

# Printing total lines and average lines
total_lines = sum(project_lines_count.values())
num_projects = len(project_lines_count)
average_lines = total_lines / num_projects if num_projects > 0 else 0

print(f"Total lines of code in '.sol' files (excluding comments and empty lines): {total_lines}")
print(f"Average lines of code per project: {average_lines:.2f}")