import cv2 as cv

img1 = cv.imread('files/teste.png')

#img1[100:150, 150:200] = [0,0,255]

#pixel = img1[100, 150]

#cv.imshow("Foto Teste", img1)
roi = img1[100:300, 150:350]

cv.imshow("Area de interesse", roi)

cv.waitKey(0)

cv.destroyAllWindows()

#print(f"Valor BGR do pixel", pixel)