import os
import sys
import glob
from PIL import Image
import argparse


# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument(
#     "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
# )
# parser.add_argument(
#     "--sum",
#     dest="accumulate",
#     action="store_const",
#     const=sum,
#     default=max,
#     help="sum the integers (default: find the max)",
# )

# args = parser.parse_args()
# print(args.accumulate(args.integers))

size = 250, 250

for infile in glob.glob("/home/dkt/Documents/niamoto/person_image/*.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)

    im.thumbnail(size)
    name_file = os.path.basename(infile)
    dir_file = os.path.dirname(infile)
    if not os.path.exists(dir_file + "/reduce"):
        print("creation dossier reduce")
        os.mkdir(dir_file + "/reduce")

    # im.save(dir_file + "/reduce/" + name_file, "png")
    # print(im.histogram())

