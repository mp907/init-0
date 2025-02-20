def caesar_encrypt(number, shift):
    encrypted_number = chr((ord(number) - 65 + shift) % 26 + 65)
    return encrypted_number

# Example usage
input_number = "123"
shift = 2
encrypted_letter = caesar_encrypt(input_number, shift)
print(f"Encrypted number: {encrypted_letter}")