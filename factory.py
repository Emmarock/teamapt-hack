from PIL import Image
import shadow_maker as sm
import weighted as w
import cv2

cv2 = cv2.cv2
num = 37

pathToFinal = './final/'
pathToBg = './bg/'
outputPath = './production-ready/'
shadowImgPath = './shadow-images/'

offset=(170,-170)
border=0

for i in range(num):
    print(i)
    img = sm.Image.open(pathToFinal + str(i+1) + '.jpg')
    bg = cv2.imread(pathToBg + str(i+1) + '.jpeg')

    # add shadow to image
    shadow = sm.createShadow(img, offset=offset, border=border, background=0x000)
    shadowImage = sm.addShadow(image=img, back_shadow=shadow, offset=offset, border=0, shadow=0x111111, iterations=10)
    shadowImage.save(shadowImgPath + str(i+1)+'.png')

    # place shadowed image on background image
    shadowImg = cv2.imread(shadowImgPath + str(i+1)+'.png')
    weightedImage = w.placeImageOnBackground(shadowImg, bg)
    cv2.imwrite(outputPath + str(i+1)+'.jpg', weightedImage)