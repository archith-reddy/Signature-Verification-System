# Signature-Verification-System
A signature verification system created using <b>Deep Convolution Neural Networks.</b>

The system uses UTSIG dataset (https://arxiv.org/ftp/arxiv/papers/1603/1603.03235.pdf)

This is the architecture of the model:

      model = tf.keras.models.Sequential([
       tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
       tf.keras.layers.MaxPooling2D(2, 2),
       tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
       tf.keras.layers.MaxPooling2D(2, 2),
       tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
       tf.keras.layers.MaxPooling2D(2, 2),
       tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
       tf.keras.layers.MaxPooling2D(2, 2),
       tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
       tf.keras.layers.MaxPooling2D(2, 2),
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(1024, activation='relu'),
       tf.keras.layers.Dense(1, activation='sigmoid')
      ])

      model.compile(optimizer=RMSprop(lr=0.001), loss='binary_crossentropy',
      metrics=['acc'])

      print(model.summary()) 
      
      
Python's tkinter library was used to develop GUI for the model. The trained networks' weights and parameters are saved locally on a machine and GUI is built on top of it.


