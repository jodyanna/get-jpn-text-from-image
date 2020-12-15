import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


def main():
    for file in os.scandir('./input'):
        filename = os.fsdecode(file)
        text = get_jpn_from_img(filename)
        write_jpn_to_file(text, filename)


def get_jpn_from_img(image):
    try:
        jpn = pytesseract.image_to_string(Image.open(image), lang='jpn_vert')
    except Exception as err:
        jpn = ''
        print(err)

    return jpn


def write_jpn_to_file(jpn, filename):
    # Remove file extension
    print(filename)
    filename = filename[:-4].split('/')[2] + '.txt'
    print(filename)
    with open('./output/' + filename, 'w') as outfile:
        print(jpn, file=outfile)


main()
