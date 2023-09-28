FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    """ Help info here """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):
    """ Help info here """
    with open(filepath, "w") as file_local:
        todos_local = file_local.writelines(todos_argument)


if __name__ == "__main__":
    print("The functions.py was called from the main script")
