import numpy as np
from PIL import Image
im = Image.open('1.png')
print im.size,im.format,im.mode
new = im.convert('L')
new.show()

