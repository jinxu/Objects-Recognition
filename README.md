# Objects-Recognition

At this tutorial we will shoot short videos for few objects, and teach model MobileNet 1.0 (using transfering learning) to recognise objects from the videos. And use this model inside the IOS mobile app. 

[how does it works](https://youtu.be/na2CQGZndNc)

# Dependencies:
- Python 3.6
- opencv
- XCode 9.4 (i didn't check on elder version)
- Tensorflow 1.7 (TOCO will not work with 1.8 so be sure that you install Tensorflow 1.70

# Usage
1. Shoot video for each objects that do you want to use. Video's filename is a label.
[video example](https://youtu.be/LMbLLQGp9tc)
2. Run <code> python decompose_videos.py </code> to decompose video to the frame. We get result at dataset/objects/. Each folder will be renamed as label and inside folder we get easch video frame as a picture.
3. <code> python retrain.py </code>  Train model MobileNet (get from TF dist, but I little bit fix it)
4. (Optional) Also possible to test model, place few files in dataset/test/ and run <code>label_folders.py</code> We will get 2 top prediction for each file.
5. After training is done neet to convert model into TFLITE format.
```
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
```

TOCO will convert model and put it inside Camera app IOS model folder.

6.1 Copy label file inside app. <code> cp tmp/output_labels.txt camera/data/labels.txt </code>
7. Open camera app via XCode, compile it to device, it will not work on simulator.
(App i get from here https://www.tensorflow.org/mobile/tflite/demo_ios but I little but fix it)


