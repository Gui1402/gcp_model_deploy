from tensorflow import keras
import tensorflow as tf
import os
"""

Train your model here

"""


model = None  # model trained


# Exporting
MODEL_DIR = './models/cats'  # define model_dir path
VERSION = '1'     # define version
export_path = os.path.join(MODEL_DIR, VERSION)  # merge dirs


model.save(export_path, save_format="tf")  # exporting

print('saved')

