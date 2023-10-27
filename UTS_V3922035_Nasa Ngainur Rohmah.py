# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Vigenere Cipher
def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_index = 0

    for char in text:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index % len(key)].upper()) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

# Fungsi untuk mengenkripsi teks menggunakan Affine Cipher
def affine_encrypt(text, key):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            char = char.upper()
            encrypted_char = chr(((ord(char) - ord('A')) * key[0] + key[1]) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Affine Cipher
def affine_decrypt(text, key):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            char = char.upper()
            decrypted_char = chr(((ord(char) - ord('A') - key[1]) * key[0] % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Teks yang akan dienkripsi
text = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kunci numerik untuk Affine Cipher
affine_key = (5, 12)

# Enkripsi menggunakan Vigenere Cipher
vigenere_key = "87"
encrypted_text = vigenere_encrypt(text, vigenere_key)

# Enkripsi menggunakan Affine Cipher
encrypted_text = affine_encrypt(encrypted_text, affine_key)

print("Teks yang dienkripsi:", encrypted_text)

# Dekripsi menggunakan Affine Cipher
decrypted_text = affine_decrypt(encrypted_text, affine_key)

# Dekripsi menggunakan Vigenere Cipher
decrypted_text = vigenere_decrypt(decrypted_text, vigenere_key)

print("Teks yang didekripsi:", decrypted_text)
