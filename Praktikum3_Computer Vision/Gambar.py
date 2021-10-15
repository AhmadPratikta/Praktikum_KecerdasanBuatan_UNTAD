# import library #
import cv2

# Membaca file gambar "SebuahFoto.jpg" yang berada satu folder dengan "main.py" #
img = cv2.imread("SebuahFoto.jpeg")

# Menampilkan data piksel dari citra #
print('Image', img)

# Menampilkan citra #
cv2.imshow("Sebuah Gambar Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
