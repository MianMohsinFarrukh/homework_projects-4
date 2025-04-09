def access_element(lst, index):
    """Returns the element at the specified index or an error message."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modifies the element at the specified index or returns an error message."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"List updated: {lst}"
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    """Returns a slice of the list from start to end or handles out-of-range indices."""
    try:
        return lst[start:end]
    except IndexError:
        return "One or more indices are out of range."

def play_index_game():
    # Initialize the list
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    print("Welcome to the Index Game!")
    print(f"Your list: {my_list}\n")

    while True:
        # Display menu
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        # Get user's choice
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':  # Access an element
            try:
                index = int(input("Enter the index to access: "))
                print(f"Element at index {index}: {access_element(my_list, index)}\n")
            except ValueError:
                print("Please enter a valid integer.\n")
        
        elif choice == '2':  # Modify an element
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value) + "\n")
            except ValueError:
                print("Please enter a valid integer.\n")
        
        elif choice == '3':  # Slice the list
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                print(f"Sliced list: {slice_list(my_list, start, end)}\n")
            except ValueError:
                print("Please enter valid integers.\n")
        
        elif choice == '4':  # Exit
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please try again.\n")

# Run the game
play_index_game()
