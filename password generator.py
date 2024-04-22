import random
import string

print("\n\n")
print("\t\t\tWELCOME TO PASSWORD RANDOM PASSWORD GENERATOR !!!")
print("\t\t    ========================================================")

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        try:
            num_passwords = int(input("Enter the number of passwords to generate: "))
            password_length = int(input("Enter the length of each password: "))
            print("\nGenerating your",num_passwords,"passwords........\n")

            for i in range(num_passwords):
                password = password_generator(password_length)
                print("Password {}: {}".format(i+1, password))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter valid numeric values.")
            continue

if __name__ == "__main__":
    main()