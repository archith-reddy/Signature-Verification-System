from tkinter import *
from tkinter.filedialog import askopenfilename
import os
import tensorflow as tf
model = tf.keras.models.load_model('new_model.h5')
import numpy as np
from keras.preprocessing import image
from PIL import Image, ImageTk


window = Tk()
# configuring main windows
window.title("Signature Verification System")
width_window = str(window.winfo_width())
height_window = str(window.winfo_height())
window.state('zoomed')

window.configure(background='#333333')

welcome_label = Label(window, text ="WELCOME TO SIGNATURE VERIFICATION SYSTEM", font= (None, 25, "bold"))
welcome_label.configure(background='#333333',fg="#048932")
welcome_label.pack(anchor='n', pady=25)

def open():
    full_name = askopenfilename(title = "Choose a file.")
    name = os.path.basename(full_name)
    file_label = Label(window, text="File selected: "+name, font=(None, 10, "bold"))
    file_label.configure(background='#333333', fg="#048932")
    file_label.pack(anchor='n', pady=25)
    path = full_name
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    print(classes[0])

    if classes[0] > 0.5:
        print(" genuine")
        label2 = Label(window, text="The Signature you uploaded is Genuine, Probability of Genuineness: "+str(classes[0]), font=(None, 10, "bold"))
        label2.configure(background='#333333', fg="#048932")
        label2.pack(anchor='n', pady=25)

    else:
        print(" forged")
        label5 = Label(window, text="The Signature you uploaded is not Genuine..., Probability of Genuineness: "+str(classes[0]), font=(None, 10, "bold"))
        label5.configure(background='#333333', fg="red")
        label5.pack(anchor='n', pady=25)


# verify signature button
ver_sig_button = Button(window,text='Upload a signature for Verification',width = 50, height=3,font=(None, 10, 'bold'),borderwidth=0,command=open)
ver_sig_button.pack()
ver_sig_button.configure(bg='#048932',fg='white')

window.mainloop()