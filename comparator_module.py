import os
import csv
from PIL import Image
import imagehash
from PIL import ImageFilter
import datetime
import locale

def create_image_database(directory):
    with open('image_database.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Hash", "File name", "File creation date"])
        for filename in os.listdir(directory):
            if (filename.endswith(".jpg") or filename.endswith(".png")) and '_thumb' not in filename:
                path = os.path.join(directory, filename)
                hash = imagehash.average_hash(Image.open(path))
                creation_date = os.path.getctime(path)
                writer.writerow([str(hash), filename, creation_date])

def compare_image_with_database(image_path, threshold=2):
    hash = imagehash.average_hash(Image.open(image_path))
    with open('image_database.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if '_thumb' in row[1]:
                continue
            otherhash = imagehash.hex_to_hash(row[0])
            if hash - otherhash < threshold:
                print(f"Найдено совпадение: {row}")
                time_str = row[1].split('@')[1].replace('.jpg', '')
                time_obj = datetime.datetime.strptime(time_str, "%d-%m-%Y_%H-%M-%S")
                
                locale.setlocale(locale.LC_TIME, 'ru_RU')
                
                print(f"Время: {time_obj.strftime('%d %B %Y года в %H:%M:%S')}")

def compare_images_with_blur(image_path, directory, threshold=2):
    img1 = Image.open(image_path)
    img1 = img1.filter(ImageFilter.BoxBlur(radius=3))
    phash1 = imagehash.phash(img1)
    ahash1 = imagehash.average_hash(img1)

    with open('image_database.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            img2_path = os.path.join(directory, row[1])
            img2 = Image.open(img2_path)
            img2 = img2.filter(ImageFilter.BoxBlur(radius=3))
            phash2 = imagehash.phash(img2)
            ahash2 = imagehash.average_hash(img2)
            total_accuracy = (phash1 - phash2) + (ahash1 - ahash2)
            if total_accuracy < threshold:
                print(f"Найдено совпадение: {row}")

if __name__ == "__main__":
    use = input("Создавать базу данных? (y / n): ")
    if use.lower() != 'y':
        name_image = input("Введите имя картинки: ") #example: photo12345.jpg
        compare_image_with_database(name_image)

        # compare_images_with_blur(name_image, 'YOUR_PATH_TO_PHOTOS') #example: photos/favorites
        # better, but MUCH MUCH slower, found on stackoverflow, thanks to Tanner Clark / https://stackoverflow.com/a/55959484
    else:
        path_images = input("Введите относительный путь к изображениям: ") #example: photos/favorites
        create_image_database(path_images)
