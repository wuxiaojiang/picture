import numpy as np
from PIL import Image

print im.size,im.format,im.mode
new = im.convert('L')
new.show()
