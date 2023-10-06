# NEEDS
# BBOX UTILS
# TRAIN UTILS OF HYPERPARAMS

from utils import data_utils, draw_utils
import os
from models import prediction_head, decoder


import tensorflow as tf

model_path = "D:\\1.Skripsi\\SSD_VGG_TF_SKRIPSI\\Workspace\\trained_model\\vgg16_Id-58_2023-10-06.h5"
custom_img_dir = data_utils.get_data_dir('custom_test_imgs')
img_path = os.path.join(custom_img_dir, os.listdir(custom_img_dir)[0])

data = data_utils.single_custom_data_gen(img_path, 300, 300)

labels = ['background', 'face']

model = tf.keras.models.load_model(model_path, compile=False)
print(type(model))

p_bbox, p_scores, p_labels = model.predict(data)
data = tf.squeeze(data)
p_bbox = tf.squeeze(p_bbox)
p_scores = tf.squeeze(p_scores)
p_labels = tf.squeeze(p_labels)

print(any(i >= 0.5 for i in p_scores))
print(p_scores.shape)


draw_utils.infer_draw_predictions(data, p_bbox, p_labels, p_scores, labels)


