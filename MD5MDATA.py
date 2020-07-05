from PIL import Image
import hashlib
import sys
ap=sys.argv[1]
hifen="-"
md5_hash = hashlib.md5()

a_file = open(ap, "rb")
content = a_file.read()
md5_hash.update(content)

digest = md5_hash.hexdigest()
Thash=digest.upper()
#print(Thash)
new_file = open("CH", "a")
new_file.write(hifen)
new_file.write(Thash)
new_file.close()




