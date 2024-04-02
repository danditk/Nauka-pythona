def get_input():
    return input("Enter a word: ")

def print_vertical(word):
    for letter in word:
        print(letter)

# Main function
def main():
    input_word = get_input()
    print("Printing word vertically:")
    print_vertical(input_word)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
