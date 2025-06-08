import cv2
from PIL import Image

image_path = 'cat.jpg'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
print(cat_face)
cat = Image.open(image_path)
glasses = Image.open('glasses.png')
shlypa = Image.open('1.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
for (x, y, w, h) in cat_face:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
    glasses = glasses.resize((500, 200))
    shlypa = shlypa.resize((500, 200))
    cat.paste(glasses, (x - 320, int(y + h / 3)), glasses)
    cat.paste(shlypa, (x - 350, int(y -  320)), shlypa)
    cat.save("cat_with_glasses.png")
    cat.save("cat_with_shlypa.png")
    cat_with_glasses = cv2.imread("cat_with_glasses.png")
    cv2.imshow("Cat_with_glasses", cat_with_glasses)
    cv2.waitKey()
cv2.imshow("Cat", image)
cv2.waitKey()
