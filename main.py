from PIL import Image


def image_filter(pixels, i, j):
    '''Повышает теплоту оттенка пикселя в зависимости от исходного цвета'''
    r, g, b = pixels[i, j]
    if pixels[i, j][0] < 255:
        if pixels[i, j][0] < 30:
            r += 35
        elif pixels[i, j][0] > 30 and (pixels[i, j][0] < 100):
            r += 20
        elif pixels[i, j][0] > 100 and (pixels[i, j][0] < 175):
            r += 15
        elif pixels[i, j][0] > 175:
            r += 7
    if pixels[i, j][1] < 102:
        if pixels[i, j][1] < 30:
            g += 30
        elif pixels[i, j][1] > 30 and (pixels[i, j][1] < 50):
            g += 20
        elif pixels[i, j][1] > 50 and (pixels[i, j][1] < 80):
            g += 15
        elif pixels[i, j][1] > 80:
            g = 90
    if pixels[i, j][2] > 11:
        if pixels[i, j][2] > 150:
            b -= 90
        elif pixels[i, j][2] < 150 and (pixels[i, j][2] > 70):
            b -= 40
        elif pixels[i, j][2] < 70 and (pixels[i, j][2] > 30):
            b -= 20
        elif pixels[i, j][2] < 30 and (pixels[i, j][2] > 0):
            b = 15
    pixels[i, j] = r, g, b


def main_process():
    print("Приветствую! Данная функция повышает теплоту оттенка изображения в зависимости от исходного цвета.\n"
          "Для продолжения работы программмы введите название файла\n(если он размещен в том же каталоге,"
          " что и сама программа) или путь к нему")
    file_name = input('Ввод: ')
    im = Image.open("{}".format(file_name))
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            image_filter(pixels, i, j)
    print("Введите название файла в которм хотите сохранить изображение.")
    name = input("Название файла: ")
    print("Введите формат файла в которм хотите сохранить изображение.")
    f = input("Формат файла: ")
    im.save(name + "." + f)


main_process()