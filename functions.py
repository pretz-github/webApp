def get_todo(file_name="todo.txt"):
    with open(file_name, "r") as file:
        todo_arg = file.readlines()
    return todo_arg


def write_todo(todo_arg, file_name="todo.txt"):
    with open(file_name, "w") as file_arg:
        file_arg.writelines(todo_arg)


if __name__ == "__main__":
    print("I am here")
