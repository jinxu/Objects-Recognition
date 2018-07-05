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
    Decompose video to frames
"""
import os
import cv2

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--videoes_dir',
                        type=str,
                        default='dataset/videoes/',
                        help='Path to folders with videos'
                        )
    parser = argparse.ArgumentParser()
    parser.add_argument('--photoes_dir',
                        type=str,
                        default='dataset/objects/',
                        help='Path to folders with photoes'
                        )
    FLAGS, unparsed = parser.parse_known_args()

    for video_file in os.listdir(FLAGS.videoes_dir): 
        if (video_file=='.DS_Store'): continue
        dest_dir = FLAGS.photoes_dir+video_file[:-4]
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        vidcap = cv2.VideoCapture(videoes_dir+video_file)
        success,image = vidcap.read()
        count = 0
        success = True
        while success:
            cv2.imwrite(dest_dir+"/frame%d.jpg" % count, image)     # save frame as JPEG file
            success,image = vidcap.read()
            count += 1

    


