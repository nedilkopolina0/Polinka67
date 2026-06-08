from PIL import Image
import numpy as np

def text_to_bits(text):
    data = text.encode('utf-8')
    length = len(data).to_bytes(4, byteorder='big')
    bits = []
    for byte in length + data:
        for i in range(7, -1, -1):
            bits.append((byte >> i) & 1)
    return bits

def bits_to_text(bits):
    length_bits = bits[:32]  # первые 32 бита — длина
    length = 0
    for i, bit in enumerate(length_bits):
        length |= (bit << (31 - i))
    byte_bits = bits[32:32 + length * 8]
    data = bytearray()
    for i in range(0, len(byte_bits), 8):
        byte = 0
        for j in range(8):
            byte |= (byte_bits[i + j] << (7 - j))
        data.append(byte)
    return data.decode('utf-8')

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)
    original_shape = pixels.shape
    bits = text_to_bits(message)
    total_pixels = pixels.size
    if len(bits) > total_pixels:
        raise ValueError("Сообщение слишком длинное для этого изображения")

    flat = pixels.flatten()
    for i in range(len(bits)):
        flat[i] = (flat[i] & 0xFE) | bits[i]  # 0xFE = 11111110, обнуляем младший бит
    new_pixels = flat.reshape(original_shape)
    img_out = Image.fromarray(new_pixels.astype('uint8'), 'RGB')
    img_out.save(output_path)
    print(f"Сообщение внедрено в {output_path}")

def decode_lsb(image_path):
    img = Image.open(image_path).convert('RGB')
    pixels = np.array(img)
    flat = pixels.flatten()
    bits = [flat[i] & 1 for i in range(flat.size)]
    try:
        message = bits_to_text(bits)
        return message
    except Exception as e:
        return f"Ошибка извлечения: {e}"

if __name__ == "__main__":
    test_img = "original.png"
    encoded_img = "encoded.png"

    width, height = 200, 200
    random_pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    img = Image.fromarray(random_pixels, 'RGB')
    img.save(test_img)
    print(f"Создано тестовое изображение: {test_img}")

    secret = "Древо"

    encode_lsb(test_img, secret, encoded_img)

    extracted = decode_lsb(encoded_img)
    print(f"Извлечённое сообщение: {extracted}")

    if extracted == secret:
        print("Успех: сообщение извлечено корректно!")

    original = Image.open(test_img)
    encoded = Image.open(encoded_img)
    diff = np.abs(np.array(original) - np.array(encoded))
    max_diff = diff.max()
    print(f"Максимальная разница в пикселях: {max_diff} (обычно 0 или 1)")
    print("Визуально изображения почти не отличаются, так как изменены только младшие биты.")
