import cv2
import numpy as np

# Kamera başlatma
cap = cv2.VideoCapture(0)
while True:
    # Görüntüyü okuma
    ret, frame = cap.read()

    # Renk uzayını değiştirme (BGR -> HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirleme
    lower_red = np.array([0, 140, 140])
    upper_red = np.array([10, 255, 255])

    # Belirlenen kırmızı renk aralığında maske oluşturma
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntü ve maskeyi birleştirme
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Görüntüleri gösterme
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basılmasını bekleyin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera kapatma
cap.release()
cv2.destroyAllWindows()