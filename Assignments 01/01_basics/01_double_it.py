def double_until_100(start):
    curr_value = start
    results = []

    while curr_value < 100:
        curr_value = curr_value * 2
        results.append(curr_value)
    
    return results

def main():
    start_number = int(input("Enter a number: "))
    doubled_values = double_until_100(start_number)
    
    print("Doubled values:")
    for value in doubled_values:
        print(value)


if __name__ == '__main__':
    main()
