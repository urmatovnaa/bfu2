"""Pillow это форк PIL (Python Image Library), которая появилась благодаря поддержке Алекса Кларка и других участников.
Основана на коде PIL, а затем преобразилась в улучшенную, современную версию.
Предоставляет поддержку при открытии, управлении и сохранении многих форматов изображения. Многое работает так же, как и в оригинальной PIL.
Форматы файлов
Перед началом использования модуля Pillow, давайте укажем некоторые поддерживаемые типы файлов:
BMP, EPS, GIF, IM, JPEG, MSP, PCX PNG, PPM, TIFF, WebP, ICO, PSD, PDF.
Некоторые типы файлов возможны только для чтения, в то время как другие доступны только для написания.
Чтобы увидеть полный список поддерживаемых типов файла и больше информации о них, ознакомьтесь с руководством к Pillow.
Скачаем изображение
Момжно скачать его например отсюда. Сохраните изображение на жестком диске. А потом выберите его при помощи метода files.upload()"""

# from google.colab import files
# uploaded = files.upload()
#
# file_path = list(uploaded.keys())[0]

"""Используйте метод open идентификации файла на компьютере, а затем загрузить идентифицированный файл с помощью myfile.load(). 
Как только изображение будет загружено, с ним можно работать. Часто используется блок try except при работе с файлами. 
Чтобы загрузить изображение с помощью try except используйте:"""
from PIL import Image, ImageFilter

try:
    image = Image.open("images.jpeg")
except FileNotFoundError:
    print("Файл не найден")

rotated_image = image.rotate(45)
rotated_image.save("rotated.jpg")

"""Теперь, когда у вас есть объект Image, вы можете использовать доступные атрибуты для проверки файла. 
Например, если вы хотите увидеть размер изображения, вы можете использовать атрибут format."""

print("Размер изображения:")
print(image.format, image.size, image.mode)

# Размытие изображения
blurred = image.filter(ImageFilter.BLUR)
# открываем оригинал и размытое изображение
image.show()
blurred.show()
# сохраняем изображение
blurred.save("blurred.png")

# В модуле Pillow предоставляет следующий набор предопределенных фильтров для
"""BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SMOOTH
SMOOTH_MORE
SHARPEN"""

img = Image.open("images.jpeg")
img = img.filter(ImageFilter.CONTOUR)
img.save("Killua" + ".jpg")
img.show()