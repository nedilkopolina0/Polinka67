def xor_cipher(text, key):
    text_bytes = text.encode('utf-8')
    key_bytes = key.encode('utf-8')

    key_repeated = (key_bytes * (len(text_bytes) // len(key_bytes) + 1))[:len(text_bytes)]

    encrypted_bytes = bytes(a ^ b for a, b in zip(text_bytes, key_repeated))

    return encrypted_bytes

def xor_decrypt(encrypted_bytes, key):
    key_bytes = key.encode('utf-8')
    key_repeated = (key_bytes * (len(encrypted_bytes) // len(key_bytes) + 1))[:len(encrypted_bytes)]
    decrypted_bytes = bytes(a ^ b for a, b in zip(encrypted_bytes, key_repeated))

    return decrypted_bytes.decode('utf-8')

if __name__ == "__main__":
    phrase = "информатика"
    key = "рамма"

    print(f"Исходная фраза: {phrase}")
    print(f"Ключ: {key}")

    encrypted = xor_cipher(phrase, key)
    print(f"Зашифрованные байты: {encrypted}")

    decrypted = xor_decrypt(encrypted, key)
    print(f"Расшифрованная фраза: {decrypted}")

    assert phrase == decrypted, "Ошибка: расшифрованный текст не совпадает с исходным!"
    print("Успешно! Шифрование и дешифрование работают корректно.")
