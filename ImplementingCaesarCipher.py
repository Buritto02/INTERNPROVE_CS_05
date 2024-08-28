def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
  
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97  
           
            shifted = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted
        else:
            result += char
    
    return result

def main():
    print("Caesar Cipher Tool:")
    mode = input("Would you like to encrypt or decrypt your message? (enter 'encrypt' or 'decrypt'): ").strip().lower()
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    
    result = caesar_cipher(message, shift, mode)
    
    print(f"\nThe {mode}ed message is: {result}")

if __name__ == "__main__":
    main()

