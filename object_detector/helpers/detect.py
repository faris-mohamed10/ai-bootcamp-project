import os
import tensorflow as tf
from object_detection.utils import label_map_util
from helpers.load_model import load_model
from helpers.process_image import process_image

script_dir = os.path.dirname(__file__)
label_map_util.tf = tf.compat.v1

category_index = label_map_util.create_category_index_from_labelmap(
    os.path.join(script_dir, '../../data/labels/label.pbtxt'), use_display_name=True)
detection_model = load_model('ssd_inception_v2_coco_2017_11_17')


def detect_image_class(img_path):
    result = process_image(detection_model,  img_path, category_index)
    return result
