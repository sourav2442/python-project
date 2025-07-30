input("Welcome to the Secret Code Language Program! Do you want to code or decode a message? (type 'code' or 'decode' or 'exit'): ").strip().lower()
while True:
    choice = input("Enter your choice (code/decode/exit): ").strip().lower()
    
    if choice == 'exit':
        print("Exiting the program. Goodbye!")
        break
    
    if choice == 'code':
        message = input("Enter the message you want to code: ")
        coded_message = ''.join(chr(ord(char) + 3) for char in message)
        print(f"Coded message: {coded_message}")
    
    elif choice == 'decode':
        coded_message = input("Enter the coded message you want to decode: ")
        decoded_message = ''.join(chr(ord(char) - 3) for char in coded_message)
        print(f"Decoded message: {decoded_message}")
    
    else:
        print("Invalid choice. Please enter 'code', 'decode', or 'exit'.")