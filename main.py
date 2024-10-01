from queue import Queue  # Module


def get_preference(message) -> int:
    """
    Takes message to display and gets user input and return user input as int
    :param message: "Queue Memory\nLimit of Queue:
    :return:10
    """
    while True:
        try:
            return int(input(message))
        except ValueError as e:
            print(f"Not valid input, Reason: {e}")


create = True
while create:
    limit: int = get_preference(message="Queue Memory\nLimit of Queue: ")
    stack_ = Queue(limit)
    print(f"Queue created with size of {limit}")
    is_on = True
    while is_on:
        choice: int = get_preference(message="1. Add Element to Queue\n"
                                             "2. Remove Element from Queue\n"
                                             "3. Display Queue\n"
                                             "4. Initialize new Queue\n"
                                             "5. Quit\n"
                                             "Choose operation on your stack: ")
        if choice == 1:
            new_element: int = get_preference(message="Data to add in your stack: ")
            stack_.add_element(data=new_element)
        elif choice == 2:
            stack_.remove_element()
        elif choice == 3:
            stack_.display()
        elif choice == 4:
            confirm = get_preference(message=f"1. Confirm\n"
                                             f"2. Cancel\n"
                                             f"Are you sure you want to clear your stack and create a new one? ")
            if confirm == 1:
                is_on = False
        elif choice == 5:
            create = False
            break
        else:
            print("Invalid choose! Please try again.")


