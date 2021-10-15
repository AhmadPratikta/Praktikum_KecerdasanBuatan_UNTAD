import cv2

# Membuat penangkap objek video dan pembaca input file video #
cap = cv2.VideoCapture('Video_CV.mp4')

# Mengecek apakah pemutar video telah terputar.#
if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Memutar video hingga terselesaikan #
while (cap.isOpened()):
    # Menampilkan Frame per frame #
    ret, frame = cap.read()
    if ret == True:
        # Menampilkan hasil frame #
        cv2.imshow('Frame', frame)
        # Tekan 'Q' untuk memberhentikan video #
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Memberhentikan perulangan #
    else:
        break
# Menunjukkan Hasil #
cap.release()
# Menutup Video #
cv2.destroyAllWindows()

