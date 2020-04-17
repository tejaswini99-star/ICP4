{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"ICP_4_1.ipynb","provenance":[],"mount_file_id":"1_ZqzSfwV01l9ETc7Cn_Yody4tM1CjWjW","authorship_tag":"ABX9TyPf2ZBvcj0Rd6+yubYzpILw"},"kernelspec":{"name":"python3","display_name":"Python 3"}},"cells":[{"cell_type":"code","metadata":{"id":"zpm7OYPhlrhR","colab_type":"code","colab":{"base_uri":"https://localhost:8080/","height":956},"outputId":"0be60822-7079-4dca-b770-dd74c764b445","executionInfo":{"status":"ok","timestamp":1587153930737,"user_tz":300,"elapsed":936007,"user":{"displayName":"tejaswini rayapati","photoUrl":"","userId":"05015603313691621650"}}},"source":["import numpy\n","import keras\n","import matplotlib.pyplot as plt\n","from keras.datasets import cifar10\n","from keras.models import Sequential\n","from keras.layers import Dense\n","from keras.layers import Dropout\n","from keras.layers import Flatten\n","from keras.constraints import maxnorm\n","from keras.optimizers import SGD\n","from keras.layers.convolutional import Conv2D\n","from keras.layers.convolutional import MaxPooling2D\n","from keras.utils import np_utils\n","'''from keras import backend as K\n","K.set_image_dim_ordering('th')'''\n","\n","# fix random seed for reproducibility\n","seed = 7\n","numpy.random.seed(seed)\n","# load data\n","(X_train, y_train), (X_test, y_test) = cifar10.load_data()\n","# normalize inputs from 0-255 to 0.0-1.0\n","X_train = X_train.astype('float32')\n","X_test = X_test.astype('float32')\n","X_train = X_train / 255.0\n","X_test = X_test / 255.0\n","# one hot encode outputs\n","y_train = np_utils.to_categorical(y_train)\n","y_test = np_utils.to_categorical(y_test)\n","num_classes = y_test.shape[1]\n","# Create the model\n","model = Sequential()\n","model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), padding='same', activation='relu', kernel_constraint=maxnorm(3)))\n","model.add(Dropout(0.2))\n","model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))\n","model.add(MaxPooling2D(pool_size=(2, 2)))\n","model.add(Conv2D(64, (3,3),activation='relu',padding='same',kernel_constraint=maxnorm(3)))\n","model.add(Dropout(0.2))\n","model.add(Conv2D(64, (3,3),activation='relu',padding='same',kernel_constraint=maxnorm(3)))\n","model.add(MaxPooling2D(pool_size=(2,2)))\n","model.add(Conv2D(128, (3,3),activation='relu',padding='same',kernel_constraint=maxnorm(3)))\n","model.add(Dropout(0.2))\n","model.add(Conv2D(128, (3,3),activation='relu',padding='same',kernel_constraint=maxnorm(3)))\n","model.add(MaxPooling2D(pool_size=(2,2)))\n","model.add(Flatten())\n","model.add(Dropout(0.2))\n","model.add(Dense(1024,activation='relu',kernel_constraint=maxnorm(3)))\n","model.add(Dropout(0.2))\n","model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))\n","model.add(Dropout(0.2))\n","model.add(Dense(num_classes, activation='softmax'))\n","# Compile model\n","epochs = 2\n","lrate = 0.01\n","decay = lrate/epochs\n","sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)\n","model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])\n","print(model.summary())\n","tbCallBack= keras.callbacks.TensorBoard(log_dir='./Graph', histogram_freq=10,write_graph=True, write_images=True)\n","# Fit the model\n","model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=32,callbacks=[tbCallBack])\n","# Final evaluation of the model\n","scores = model.evaluate(X_test, y_test, verbose=0)\n","print(\"Accuracy: %.2f%%\" % (scores[1]*100))\n","#save to disk\n","model_json = model.to_json()\n","with open('model.json', 'w') as json_file:\n","    json_file.write(model_json)\n","model.save_weights('model.h5')"],"execution_count":3,"outputs":[{"output_type":"stream","text":["Model: \"sequential_3\"\n","_________________________________________________________________\n","Layer (type)                 Output Shape              Param #   \n","=================================================================\n","conv2d_13 (Conv2D)           (None, 32, 32, 32)        896       \n","_________________________________________________________________\n","dropout_13 (Dropout)         (None, 32, 32, 32)        0         \n","_________________________________________________________________\n","conv2d_14 (Conv2D)           (None, 32, 32, 32)        9248      \n","_________________________________________________________________\n","max_pooling2d_7 (MaxPooling2 (None, 16, 16, 32)        0         \n","_________________________________________________________________\n","conv2d_15 (Conv2D)           (None, 16, 16, 64)        18496     \n","_________________________________________________________________\n","dropout_14 (Dropout)         (None, 16, 16, 64)        0         \n","_________________________________________________________________\n","conv2d_16 (Conv2D)           (None, 16, 16, 64)        36928     \n","_________________________________________________________________\n","max_pooling2d_8 (MaxPooling2 (None, 8, 8, 64)          0         \n","_________________________________________________________________\n","conv2d_17 (Conv2D)           (None, 8, 8, 128)         73856     \n","_________________________________________________________________\n","dropout_15 (Dropout)         (None, 8, 8, 128)         0         \n","_________________________________________________________________\n","conv2d_18 (Conv2D)           (None, 8, 8, 128)         147584    \n","_________________________________________________________________\n","max_pooling2d_9 (MaxPooling2 (None, 4, 4, 128)         0         \n","_________________________________________________________________\n","flatten_3 (Flatten)          (None, 2048)              0         \n","_________________________________________________________________\n","dropout_16 (Dropout)         (None, 2048)              0         \n","_________________________________________________________________\n","dense_7 (Dense)              (None, 1024)              2098176   \n","_________________________________________________________________\n","dropout_17 (Dropout)         (None, 1024)              0         \n","_________________________________________________________________\n","dense_8 (Dense)              (None, 512)               524800    \n","_________________________________________________________________\n","dropout_18 (Dropout)         (None, 512)               0         \n","_________________________________________________________________\n","dense_9 (Dense)              (None, 10)                5130      \n","=================================================================\n","Total params: 2,915,114\n","Trainable params: 2,915,114\n","Non-trainable params: 0\n","_________________________________________________________________\n","None\n","Train on 50000 samples, validate on 10000 samples\n","Epoch 1/2\n","50000/50000 [==============================] - 457s 9ms/step - loss: 1.9635 - accuracy: 0.2744 - val_loss: 1.8770 - val_accuracy: 0.3408\n","Epoch 2/2\n","50000/50000 [==============================] - 458s 9ms/step - loss: 1.6758 - accuracy: 0.3857 - val_loss: 1.6206 - val_accuracy: 0.4192\n","Accuracy: 41.92%\n"],"name":"stdout"}]}]}