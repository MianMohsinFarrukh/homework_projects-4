# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst):
    """ Prints the first element of a given non-empty list. """
    print("The first element in the list is:", lst[0])

def main():

    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  


    get_first_element(lst)

# Required line to run the program
if __name__ == '__main__':
    main()