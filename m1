import random
import string
import math

def generate_password(length):
    if length < 1:
        raise ValueError("Длина пароля должна быть положительной")
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def evaluate_password(password):
    length = len(password)
    if length == 0:
        return 0.0, "пустой"
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    alphabet_size = 0
    if has_lower:
        alphabet_size += 26
    if has_upper:
        alphabet_size += 26
    if has_digit:
        alphabet_size += 10
    if has_special:
        alphabet_size += len(string.punctuation)

    entropy = math.log2(alphabet_size) * length if alphabet_size > 0 else 0

    if entropy < 40:
        strength = "слабый"
    elif entropy < 60:
        strength = "средний"
    else:
        strength = "сильный"
    
    return entropy, strength
