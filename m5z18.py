import exifread
import os

def decimal_coords(coords, ref):
    degrees = float(coords[0].num) / float(coords[0].den)
    minutes = float(coords[1].num) / float(coords[1].den)
    seconds = float(coords[2].num) / float(coords[2].den)
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_metadata(image_path):
    if not os.path.exists(image_path):
        print("Файл не найден.")
        return

    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    print(f"# Анализируем файл: {image_path}\n")

    gps_latitude = None
    gps_longitude = None
    metadata_found = False

    if 'Image Make' in tags:
        print(f"Производитель: {tags['Image Make']}")
        metadata_found = True

    if 'Image Model' in tags:
        print(f"Модель: {tags['Image Model']}")
        metadata_found = True

    date_tag = tags.get('EXIF DateTimeOriginal')
    if date_tag:
        print(f"Дата съёмки: {date_tag}")
        metadata_found = True

    if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags and \
       'GPS GPSLatitudeRef' in tags and 'GPS GPSLongitudeRef' in tags:
        gps_latitude = decimal_coords(tags['GPS GPSLatitude'].values, tags['GPS GPSLatitudeRef'].values)
        gps_longitude = decimal_coords(tags['GPS GPSLongitude'].values, tags['GPS GPSLongitudeRef'].values)

        if gps_latitude and gps_longitude:
            print(f"\n GPS-координаты:")
            print(f"   Широта: {gps_latitude:.6f}")
            print(f"   Долгота: {gps_longitude:.6f}")
            print(f"   Google Maps: https://www.google.com/maps?q={gps_latitude},{gps_longitude}")
            metadata_found = True

    if not metadata_found:
        print(" В этом файле нет EXIF-метаданных или доступ к ним ограничен.")
        return

    print("\nПРЕДУПРЕЖДЕНИЕ О РИСКАХ ПРИВАТНОСТИ:")
    print("Обнаружены личные данные в метаданных файла!")
    print("Перед публикацией в интернете рекомендуется удалить EXIF-данные для защиты личной информации.")

if __name__ == "__main__":
    photo_path = input("Введите путь к фотографии: ").strip()
    extract_metadata(photo_path)
