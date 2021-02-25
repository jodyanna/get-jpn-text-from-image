import os
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image


def main():
    # loop over files in input dir
    for file in os.scandir('./input'):
        # Get the filename
        filename = os.fsdecode(file)

        # Get the Japanese text from that file
        text = get_jpn_from_img(filename)

        # Write that Japanese text to a new .txt file
        write_string_to_file(text, filename)

        # Japanese text was written to file successfully
        print(f'{filename.split("/")[2]} completed.')


def get_jpn_from_img(image):
    """
    Uses pytesseract to extract Japanese text from image.
    :param image: image data
    :return string:
    """
    try:
        jpn = pytesseract.image_to_string(Image.open(image), lang='jpn_vert')
    except Exception as err:
        jpn = ''
        print(err)

    return jpn


def write_string_to_file(text, filename):
    """
    Creates a new .txt file and writes the string to it.
    :param text: string of Japanese text
    :param filename: name for the new .txt file
    """
    # Remove file extension, add .txt extension
    filename = filename[:-4].split('/')[2] + '.txt'

    # Create and write the file
    with open('./output/' + filename, 'w') as outfile:
        print(text, file=outfile)


main()
