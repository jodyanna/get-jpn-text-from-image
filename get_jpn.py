import os
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image


def main():
    for file in os.scandir('./input'):
        filename = os.fsdecode(file)
        text = get_jpn_from_img(filename)
        write_jpn_to_file(text, filename)
        print(f'{filename.split("/")[2]} completed.')


def get_jpn_from_img(image):
    try:
        jpn = pytesseract.image_to_string(Image.open(image), lang='jpn_vert')
    except Exception as err:
        jpn = ''
        print(err)

    return jpn


def write_jpn_to_file(jpn, filename):
    # Remove file extension, add .txt extension
    filename = filename[:-4].split('/')[2] + '.txt'

    with open('./output/' + filename, 'w') as outfile:
        print(jpn, file=outfile)


main()
