import cv2
import matplotlib.pyplot as  plt
from tkinter import filedialog
import os

filename = filedialog.askopenfilename(initialdir=os.getcwd())

img = cv2.imread(filename)

plt.imshow(img)
plt.title('exemplo imagem')
plt.show()