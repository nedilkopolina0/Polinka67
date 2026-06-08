def simple_hash(password):
    return sum(ord(c) for c in password) % 10000

def brute_force(target_hash):
    for i in range(10000):
        pwd = f"{i:04d}"
        if simple_hash(pwd) == target_hash:
            return pwd
    return None

def evaluate_complexity(password):
    total_combinations = 10 ** 4
    if total_combinations <= 100000:
        return "легкий"
    elif total_combinations <= 1000000:
        return "средний"
    else:
        return "сложный"

if __name__ == "__main__":
    original_password = "1234"
    original_hash = simple_hash(original_password)
    print(f"Исходный пароль: {original_password}")
    print(f"Ero хеш: {original_hash}")

    found = brute_force(original_hash)
    print(f"Перебором найден пароль: {found}")

    complexity = evaluate_complexity(original_password)
    print(f"\nСложность взлома перебором: {complexity}")
