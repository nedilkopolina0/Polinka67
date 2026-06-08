import random

def generate_params():
    p = 999983
    g = 5
    return p, g

def generate_key(p, g):
    x = random.randint(2, p-2)
    h = pow(g, x, p)
    return x, h

def encrypt(m, g, h, p):
    k = random.randint(2, p-2)
    c1 = pow(g, k, p)
    c2 = (m * pow(h, k, p)) % p
    return (c1, c2)

def decrypt(c1, c2, x, p):
    s = pow(c1, x, p)
    inv_s = pow(s, -1, p)
    return (c2 * inv_s) % p

def multiply_ciphers(ca, cb, p):
    c1a, c2a = ca
    c1b, c2b = cb
    return ((c1a * c1b) % p, (c2a * c2b) % p)

if __name__ == "__main__":
    p, g = generate_params()
    print(f"Параметры: p = {p}, g = {g}")

    x, h = generate_key(p, g)
    print(f"Секретный ключ: x = {x}")
    print(f"Открытый ключ: h = {h}\n")

    a = 42
    b = 7
    print(f"Числа: a = {a}, b = {b}")
    print(f"Произведение: a * b = {a * b}\n")

    ca = encrypt(a, g, h, p)
    cb = encrypt(b, g, h, p)
    print(f"Шифротекст E(a) = {ca}")
    print(f"Шифротекст E(b) = {cb}")

    prod_cipher = multiply_ciphers(ca, cb, p)
    print(f"\nПроизведение шифротекстов: E(a) ⊗ E(b) = {prod_cipher}")

    decrypted_prod = decrypt(prod_cipher[0], prod_cipher[1], x, p)
    print(f"Расшифрованное произведение: {decrypted_prod}")

    print("\n" + "="*50)
    if decrypted_prod == (a * b) % p:
        print(" РАБОТАЕТ!")
        print("Произведение шифротекстов расшифровалось в произведение чисел.")
    else:
        print("Ошибка")
    print("="*50)
