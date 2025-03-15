import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
           return False
    return True

def prime_sum(start, end):
    """Calculate the sum of all the prime numbers in a given range."""
    return sum(n for n in range(start, end + 1) if is_prime(n))

def length_converter(value, direction):
    """Caluate the sum of all prime numbers in a given range."""
    if direction == 'M':
        return round(value * 3.28084, 2)
    elif direction == 'F':
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")
    
def consonant_counter(text):
        """Count the number of the consonants in a given text."""
        consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
        return sum(1 for char in text if char in consonants)

def min_max_finder(numbers):
    # Simply return the minimum and maximum values of the numbers list
    return min(numbers), max(numbers)
   
def is_palindrome(text):
    """Check if a given text is a palindrome."""
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

import requests                        #type: ignore
from bs4 import BeautifulSoup          #type: ignore
import string

def word_counter(file_path):
    """Count specific words in a text file or from a URL."""
    words_to_count = ["the", "was", "and"]
    word_count = {word: 0 for word in words_to_count}
    
    if file_path.startswith("http://") or file_path.startswith("https://"):
        response = requests.get(file_path)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text().lower()
    else:
        with open(file_path) as file:
            text = file.read().lower()
    
    for word in words_to_count:
        word_count[word] = text.split().count(word)
    
    return word_count
def main():
    while True:
        print("\nMenu:")
        print("1. Prime number sum calculator")
        print("2. Length unit converter")
        print("3. Consonant counter")
        print("4. Min-Max number Finder")
        print("5. Palindrome checker")
        print("6. Word counter")
        print("7. Exit")
              
        choice = input("Select a function (1-7): ")

        if choice == '1':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print(f"sum of primes: {prime_sum(start, end)}")
            except ValueError:
                print("Invalid input. Please enter integers.")
        elif choice == '2':
            try:
                value = float(input("Enter the length value to convert: "))
                direction = input("Enter direction ('M' for meters to feet, 'F' for feet to meters): ")
                print(f"Converted length: {length_converter(value, direction)}")
            except ValueError as e:
                print(f"Innvalid input: {e}")

        elif choice == '3':
            text = input("Enter a text string: ")
            print(f"Number of consonants: {consonant_counter(text)}")

        elif choice == '4':
            try:
                count = int(input("How many numbers do you want to enter? "))  #Define count first
                numbers = []
                
                # Collect the numbers from user
                for i in range(count): 
                    number = float(input(f"Enter number {i+1}: "))   # Input a number
                    numbers.append(number)     # Append the entered number to the list

                # Calculate the minimum and maximum after collecting all numbers
                min_num, max_num = min_max_finder(numbers)

                # Print the minimum and maximum after all numbers are entered
                print(f"Smallest: {min_num}, Largest: {max_num}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '5':
            text = input("Enter a text string: ")
            print(f"Is a palindrome: {is_palindrome(text)}")

        elif choice == '6':
            try:
                file_path = input("Enter the file path or URL: ")
                words_to_count = ["the", "was", "and"]
                word_count = {word: 0 for word in words_to_count}

                if file_path.startswith("http://") or file_path.startswith("https://"):
                    response = requests.get(file_path)
                    soup = BeautifulSoup(response.text, "html.parser")
                    text = soup.get_text().lower()
                else:
                    with open(file_path) as file:
                        text = file.read().lower()

                for word in words_to_count:
                    word_count[word] = text.split().count(word)
                
                print(f"Word counts: {word_count}")
            except FileNotFoundError:
                print("File not found. Please enter a valid file path.")
            except Exception as e:
                print(f"An error occurred: {e}")
                      

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 7.")

if __name__ == "__main__":
    main()




        


        
        
    