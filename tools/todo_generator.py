import os
import mimetypes


def print_todo_set(set, completed=False):
    if len(set) == 0: return ""

    if completed: return '- [X] ' + '- [X] '.join(set)
    else: return '- [ ] ' + '- [ ] '.join(set)


def extract_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    todos = set()
    todo_str = "TODO" + ": " # this is a hack so it doesn't grab the lines that use this comment
    for line in lines:
        if todo_str in line:
            temp = line.split(todo_str)
            # TODO: RESEARCH: see if theres a way to find if a line is a comment
            if len(temp) > 1:
                todos.add(temp[1])
            else:
                todos.add(line)

    return todos


def process_files(file_dir, file_todos=None):
    # initialize the set if it's the first call
    if file_todos is None: file_todos = set()

    # move through all child dirs and files
    for item in os.listdir(file_dir):
        # ignore hidden files and directories
        if item.startswith('.'): continue

        item_path = os.path.join(file_dir, item)
        
        # get type of file so it doesn't search non-text files
        mime_type, _ = mimetypes.guess_type(item_path)

        # recursive call for subdirectory
        if os.path.isdir(item_path):
            file_todos = process_files(item_path, file_todos)
        # extract info and update the set if it's a file (excluding README.md)
        elif os.path.isfile(item_path) and item != 'README.md':
            # ignore any files that are not text
            if mime_type is None or (not mime_type.startswith('text')): continue
            file_todos.update(extract_info(item_path))

    return file_todos


def generate_todo_readme(file_dir="./", readme="./README.md"):
    # read in readme
    with open(readme, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    readme_todos = set() # keep todo's in set
    readme_todos_done = set() # keep done todos in other set

    header_section = True
    todo_section = False
    header, footer, todo_line = "", "", "\n## TODO\n"
    for line in lines:
        # only do work inside todo section
        if todo_section and "# " in line:
            todo_section = False
            header_section = False
        if "# TODO" in line:
            todo_section = True
            todo_line = line

        # make remaking the file easier
        if not todo_section and header_section: header += line
        if not todo_section and not header_section: footer += line

        # actually parse out todos
        if todo_section and line.startswith("- [ ]"):
            readme_todos.add(line.split("- [ ] ")[1])
        if todo_section and line.startswith("- [X]"):
            readme_todos_done.add(line.split("- [X] ")[1])

    # read over files for TODO
    file_todos = process_files(file_dir)

    # identify todos that are in readme but no longer in files
    readme_todos_done.update(readme_todos - file_todos)

    # update the sets by removing the completed todos from readme_todos and removing any duplicates from file_todos
    readme_todos -= readme_todos_done
    file_todos -= readme_todos

    # rewrite readme with new lists of todos
    with open('README.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(
            header +  todo_line + '\n' + \
            print_todo_set(file_todos) + \
            print_todo_set(readme_todos) + \
            print_todo_set(readme_todos_done, completed=True) + \
            footer
        )

    return


if __name__ == "__main__":
    generate_todo_readme()
