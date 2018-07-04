# Objects-Recognition

cp tmp/output_labels.txt camera/data/labels.txt

toco \
  --input_file=tmp/output_graph.pb \
  --output_file=camera/data/mobilenet_quant_v1_224.tflite \
  --input_format=TENSORFLOW_GRAPHDEF \
  --output_format=TFLITE \
  --input_shape=1,224,224,3 \
  --input_array=input \
  --output_array=final_result \
  --inference_type=FLOAT \
  --input_data_type=FLOAT
