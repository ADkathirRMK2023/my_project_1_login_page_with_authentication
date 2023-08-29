def encrypt_password(password, shift=3):
    encrypted_password = ''
    for char in password:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_password += encrypted_char
        elif char.isdigit():
            encrypted_digit = chr((ord(char) - ord('0') + shift) % 10 + ord('0'))
            encrypted_password += encrypted_digit
        else:
            encrypted_password += char
    return encrypted_password









