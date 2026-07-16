import cv2 

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')

while True:
    ret,frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filmer = cv2.VideoWriter("MeuVideo.avi", codec, 20, (width, height))
    if not ret:
        print("Erro ao capturar")
        break
    #cv2.imshow('CFBCursos', frame)
    cv2.imshow("CFBCursos", frame_gray)
    filmer.write(frame_gray)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
filmer.release()
cv2.destroyAllWindows()
