from tensorflow.keras import backend as K

# This clears the session, which is like resetting the whole TensorFlow environment
K.clear_session()

# Now, TensorFlow will release the GPU memory allocated for the model and tensors
