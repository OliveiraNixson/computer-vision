import cv2 as cv

img1 = cv.imread('files/teste_ruido.jpg')

blur_img  = cv.blur(img1,[3,3])

blur_gaus_img = cv.GaussianBlur(img1[100:500, 100:500], [5,5], 0)

blur_media_img = cv.medianBlur(img1,5)

cv.imshow("Imagem com ruido Gaussiano", blur_gaus_img)

cv.waitKey(0)

cv.destroyAllWindows()