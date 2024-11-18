import random
import string
def generate_password(length):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
def main():
    print("Password Generator")
    length = int(input("Enter the length of the password: "))
    password = generate_password(length)
    print("Generated Password:", password)
    result=password
    print("Your password is ",result)
if __name__ == "__main__":
    main()
