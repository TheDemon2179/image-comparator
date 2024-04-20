import keyboard
import comparator
from PIL import ImageGrab

def paste_image():
    image = ImageGrab.grabclipboard()
    
    if image is not None:
        if isinstance(image, list):
            for i, img in enumerate(image):
                img.save(f"pasted_image_{i}.png")
                print(f"Изображение {i} успешно вставлено и сохранено.")
                print("\nНачинается поиск.")
                comparator.compare_image_with_database(f'pasted_image_{i}.png')
        else:
            image.save("pasted_image.png")
            print("Изображение успешно вставлено и сохранено.")
            print("\nНачинается поиск.")
            comparator.compare_image_with_database('pasted_image.png')
    else:
        print("В буфере обмена нет изображения.")

keyboard.add_hotkey('ctrl+v', paste_image) # lots of false inputs if running in the background, if it disturbs you, fix it yourself xD
keyboard.wait()
