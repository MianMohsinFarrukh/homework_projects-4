# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):
# What's your favorite animal? cow
# My favorite animal is also cow!


def main():
    # Prompt the user for their favorite animal
    animal = input("\033[1;3m What's your favorite animal? ")

# ANSI Escape Sequences - GitHub Gist :
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

      
    print(f"My favorite animal is also {animal}!")

if __name__ == "__main__":
        main()