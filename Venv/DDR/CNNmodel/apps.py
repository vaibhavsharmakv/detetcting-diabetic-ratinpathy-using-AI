from PIL import Image
from DDR.settings import BASE_DIR
import os,sys
from io import BytesIO
from typing import List, Dict, Union, ByteString, Any
import base64

def get_Image(imgName: str)->Image:
    dir = os.path.join(BASE_DIR,"datasetsImages/datasetsImages")
    image = Image.open(os.path.join(dir,imgName))
    return image



imgName = sys.argv[1]
image = get_Image(imgName)


print(imgName)