from PIL import Image
import os

kuva = input("open picture: ")
tallenna = input("Save as: ")
w = 32
h = 24
clean = []
image = Image.open(kuva)
pikselit = image.load()
width, height = image.size

if not width == w or height == h:
    print("Warning resizing for further processing!")
    image2 = image.resize((w, h))
    image2.save("pythonkuva.png")
    pikselit = image2.load()
    width, height = image2.size

f = open(tallenna,'w')
f.write("(" + str(w) + ")(" + str(h) + ")")

for y in range(height):
    for x in range(width):
        info = pikselit[x, y]
        r = str(info[0])
        g = str(info[1])
        b = str(info[2])
        clean = ( '#%02x%02x%02x' % (int(r), int(g), int(b))).split("#")
        #print("(0x" + clean[1]+ ")")
        data = "(0x" + clean[1]+ ")"
        f.write(data)
f.close()
os.remove("pythonkuva.png")
print("completed")
