# Objects-Recognition

At this tutorial we will shoot short videos for few objects, and teach model MobileNet 1.0 (using transfering learning) to recognise objects from the videos. And use this model inside the IOS mobile app. 

# Dependencies:
- Python 3.6
- opencv
- XCode 9.4
- Tensorflow 1.7

# Usage
1. Shoot video for each objects that do you want to use. Video's filename is a label.
2. Run <code> python decompose_videos.py </code> to decompose video to the frame. We get result at dataset/objects/. Each folder will be renamed as label and inside folder we get easch video frame as a picture.
3. <code> python retrain.py </code>  Train model MobileNet
4. After training is done neet to convert model into TFLITE format.
<code>
toco \
  --input_file=tmp/output_graph.pb \
  --output_file=camera/data/mobilenet_v1_224.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --input_shape=1,224,224,3 \
  --input_array=input \
  --output_array=final_result \
  --inference_type=FLOAT \
  --input_data_type=FLOAT
</code>
TOCO will convert model and put it inside Camera app IOS model folder.

4.1 Copy label file inside app. <code> cp tmp/output_labels.txt camera/data/labels.txt </code>
