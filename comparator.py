import keyboard
import comparator_module
from PIL import ImageGrab

def paste_image():
    image = ImageGrab.grabclipboard() # i find it quite convenient
    
    if image is not None:
        image.save("pasted_image.png")
        print("Изображение успешно вставлено и сохранено.")
        print("\nНачинается поиск.")
        comparator_module.compare_image_with_database('pasted_image.png')
    else:
        print("В буфере обмена нет изображения.")

keyboard.add_hotkey('ctrl+v', paste_image) # lots of false inputs if running in the background, if it disturbs you, fix it yourself xD

keyboard.wait()