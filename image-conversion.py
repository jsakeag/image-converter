# Pillow is a fork of PIL, Python Image Library (Used for Image Processing)
import os
from PIL import Image

# Used to identify file extensions
import glob

print(glob.glob("*.jpg"))

# Converts files (https://stackoverflow.com/a/43258974/5086335)


def convert(old, new, pixel_format, delete_old=False):
    print("Converting from " + old + " to " + new + "...")
    totalFiles = len(glob.glob("*." + old))
    filesDone = 0
    for file in glob.glob("*." + old):
        im = Image.open(file)
        # png supports RGBA, jpg supports only RGB
        # so RGBA to convert to png, RGB for jpg
        out_im = im.convert(pixel_format)
        file = file.replace(old, new)
        out_im.save(file, quality=95)
        filesDone += 1
        printProgressBar(filesDone, totalFiles, 'Progress: ',
                         '(' + str(filesDone)+"/"+str(totalFiles)+' Converted...)', 1, 10)

    filesDone = 0
    print("Deleting old files...")
    if(delete_old):
        for file in glob.glob("*." + old):
            os.remove(file)
            filesDone += 1
            printProgressBar(filesDone, totalFiles, 'Progress: ',
                             '(' + str(filesDone)+"/"+str(totalFiles)+' Deleted...)', 1, 10)
    print("Conversion finished!")

# Print iterations progress (https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters?noredirect=1&lq=1)


def printProgressBar(amount, total, prefix='', suffix='', decimals=1, length=100, printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (amount / float(total)))
    filledLength = int(length * amount // total)
    bar = '█' * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if amount == total:
        print()


# Run this command to convert from jpg to png
convert('jpg', 'png', 'RGBA', True)

input("Press Enter to continue...")
# Run this command to convert from png to jpg
convert('png', 'jpg', 'RGB', True)
