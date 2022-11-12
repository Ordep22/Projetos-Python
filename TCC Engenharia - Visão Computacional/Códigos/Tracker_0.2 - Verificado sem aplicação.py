import cv2


captura = cv2.VideoCapture("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Vídeos Resende - Bobinas CG/c-00-20200819-194148.ts")


_, imgFundo = captura.read()
imgFundo = cv2.resize(imgFundo, (640, 480))
imgFundoGray = cv2.cvtColor(imgFundo, cv2.COLOR_RGB2GRAY)

binaria = False

while True:

    _, frame = captura.read()

    frame = cv2.resize(frame, (640, 480))

    if (binaria == True):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        imgSemFundo = cv2.subtract(imgFundoGray, frame)
        imgComBordas = cv2.Canny(imgSemFundo, 50, 100)

        cv2.imshow("Imagem", imgComBordas)

    else:
        cv2.imshow("Imagem", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    if cv2.waitKey(98) & 0xFF == ord("b"):
        binaria = True
    if cv2.waitKey(99) & 0xFF == ord("c"):
        binaria = False

captura.release()
cv2.destroyAllWindows()









