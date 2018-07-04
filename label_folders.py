# Copyright 2015 The Datawiz Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
r"""
    Simple script for prediction of images labels using given model.
"""

import argparse
import sys,os
import tensorflow as tf
from PIL import Image
import numpy as np
import argparse

def load_image(filename):
    """Read in the image_data to be classified."""
    im=Image.open(filename)
    image=np.asarray(im, dtype="float32")
    img=(image-128.0)/128.0
    img=np.array(img).reshape(1,224,224,3)
    return img

def load_labels(filename):
    #Read in labels, one label per line."""
    return [line.rstrip() for line in tf.gfile.GFile(filename)]

def load_graph(filename):
    #Unpersists graph from file as default graph."""
    with tf.gfile.FastGFile(filename, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_imgs',
                        type=str,
                        default='dataset/test/',
                        help='Path to folders of test images.'
                        )
    parser.add_argument('--labels',
                        type=str,
                        default='tmp/output_labels.txt',
                        help='Path to labels'
                        )
    parser.add_argument('--graph',
                        type=str,
                        default='tmp/output_graph.pb',
                        help='Path to labels'
                        )
    parser.add_argument('--input_layer',
                        type=str,
                        default='input:0',
                        help='Input layer'
                        )
    parser.add_argument('--output_layer',
                        type=str,
                        default='final_result:0',
                        help='Output layer'
                        )
    FLAGS, unparsed = parser.parse_known_args()


    load_graph(FLAGS.graph)
    labels = load_labels(FLAGS.labels)
    num_top_predictions = 2
    
    with tf.Session() as sess:
        for f in os.listdir(FLAGS.test_imgs): #Loop over each test image
            if (f=='.DS_Store'): continue #Avoiding critical error on MAC OS
            image_data = load_image(FLAGS.test_imgs+f) #load image
            
            softmax_tensor=sess.graph.get_tensor_by_name(FLAGS.output_layer) #define output tensor
            predictions,=sess.run(softmax_tensor, {FLAGS.input_layer: image_data}) #run model
            top_k = predictions.argsort()[-num_top_predictions:][::-1] #get few top predictions

            for node_id in top_k:
                predicted_label = labels[node_id] #get node id responsible for the prediction
                score = predictions[node_id] #get confidence of our prediction
                print(f,predicted_label,score)
            print("\n")
