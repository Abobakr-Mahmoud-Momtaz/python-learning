import abobakr_tools as at
from sys import exit


def main():
    to_do_list = []
    user_command = get_valid_command()
    
    while user_command.lower().strip() in ["add", "view", "delete", "end task", "find task number", "count", "sort", "reverse", "stop"]:
        match user_command.lower().strip():

            case "add":
                task_to_add = at.read_non_numeric_string("What task would you like to add?: ")
                print("The task added.")
                to_do_list = at.append_to_list(to_do_list, task_to_add)
                user_command = handle_error_and_get_next_command("The task appended.")
                
            case "view":
                if at.get_sequence_length(to_do_list) == 0:
                    user_command = handle_error_and_get_next_command("No tasks.")
                else:
                    print("Your tasks are:")
                    at.print_items(to_do_list)
                    user_command = get_valid_command()

            case "delete":
                task_to_delete = at.read_non_numeric_string("What task would you like to delete?: ")
                if task_to_delete in to_do_list:
                    to_do_list = at.remove_all_occurrences(to_do_list, task_to_delete)
                    user_command = handle_error_and_get_next_command("The task deleted.")
                    
            case "end task":
                task_to_end = at.read_non_numeric_string("What task would you like to end?: ")
                if task_to_end in to_do_list:
                    # ملاحظة: نستخدم index() الأصلية في Python هنا لأنها أسرع من دالة مخصصة
                    task_index = to_do_list.index(task_to_end)
                    to_do_list.pop(task_index)
                    print("The task ended and deleted.")
                    user_command = get_valid_command()
                else:
                    user_command = handle_error_and_get_next_command()
                    
            case "find task number":
                target_task = at.read_non_numeric_string("What is the task?: ")
                if target_task in to_do_list:
                    task_position = at.find_first_index(to_do_list, target_task) + 1
                    print(f"Task number is {task_position}")
                    user_command = get_valid_command()
                else:
                    user_command = handle_error_and_get_next_command()
                    
            case "count":
                target_task = at.read_non_numeric_string("What is the task to count?: ")
                # ملاحظة: نستخدم count() الأصلية في Python
                occurrence_count = to_do_list.count(target_task)
                print(f"Count is {occurrence_count}")
                user_command = get_valid_command()
                
            case "sort":
                if to_do_list:
                    while True:
                        sort_method = at.read_non_numeric_string("Which sort method (len task or letters)?: ")
                        match sort_method:
                            case "len task":
                                to_do_list.sort(key=len)
                                print(to_do_list)
                                break
                            case "letters":
                                to_do_list.sort()
                                print(to_do_list)
                                break
                            case _:
                                continue
                else:
                    user_command = handle_error_and_get_next_command("I do not find any task.", False)
                user_command = get_valid_command()
                
            case "reverse":
                if to_do_list:
                    to_do_list = at.reverse_items(to_do_list)
                    print(to_do_list)
                    user_command = get_valid_command()
                else:
                    user_command = handle_error_and_get_next_command("I do not find any task.", False)

            case "stop":
                confirmation = at.read_non_numeric_string("Are you sure you want to stop this program (Yes/No)?: ")
                while confirmation.lower().strip() not in ["yes", "no"]:
                    confirmation = at.read_non_numeric_string("Are you sure you want to stop this program (Yes/No)?: ")
                if confirmation.lower().strip() == "yes":
                    print("The program stopped.")
                    exit()
                elif confirmation.lower().strip() == "no":
                    user_command = get_valid_command()


def handle_error_and_get_next_command(message: str = "The task was not found.", should_print_message: bool = True) -> str:
    if should_print_message:
        print(message)

    user_input = input("Write anything to continue, or write 'stop' to exit: ")
    if user_input.lower().strip() == "stop":
        next_command = "stop"
    else:
        next_command = get_valid_command()
    return next_command


def get_valid_command() -> str:
    user_command = at.read_non_numeric_string(
        "Would you like to add, view, delete, end task, find task number, count, sort, reverse, or stop? "
        "(add/view/delete/end task/find task number/count/sort/reverse/stop): "
    )
    while True:
        if user_command.lower().strip() not in ["add", "view", "delete", "end task", "find task number", "count", "sort", "reverse", "stop"]:
            user_command = at.read_non_numeric_string(
                "Invalid input. Would you like to add, view, delete, end task, find task number, count, sort, reverse, or stop? "
                "(add/view/delete/end task/find task number/count/sort/reverse/stop): "
            )
            continue
        else:
            break

    return user_command


if __name__ == "__main__":
    main()