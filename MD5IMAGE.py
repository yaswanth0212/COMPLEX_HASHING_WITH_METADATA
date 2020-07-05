from PIL import Image
import hashlib
import sys


#md5hash = hashlib.md5(Image.open('1.png').tobytes())
#print(md5hash.hexdigest())

#import base64
#from PIL import Image
#import hashlib

s = sys.argv[1]
with open(s, "rb") as imageFile:
	#str = base64.b64encode(imageFile.read())
	str = imageFile.read()
    #print (str)
	


#hash_obj = hashlib.md5(str)
#print(hash_obj.hexdigest())


st=hashlib.md5(str).hexdigest()
Thash=st.upper()
#image_file = Image.open('1.png')
#print(hashlib.md5(strhexdigest())
new_file = open("CH", "w+")
new_file.write(Thash)
new_file.close()
print(Thash)