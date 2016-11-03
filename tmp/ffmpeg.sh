#!/bin/bash

# HOW TO RUN:
# ./ffmpeg.sh [arg]
# where arg is 'a' for audio only, 'v' for audio+video, 's' for audio+screengrab
# screengrab still has bad audio, trying to figure that one out

arg=$1
audio="ffmpeg -f avfoundation -i \"none:0\" -y -vn -f mp4 -c:a libmp3lame output.mp4"
video="ffmpeg -f avfoundation -r 30 -c:v rawvideo -i \"0:0\" -y -f mp4 -c:v mpeg4 -c:a libmp3lame output.mp4"
screengrab="ffmpeg -f avfoundation -r 30 -c:v rawvideo -i \"1:0\" -y -f mp4 -c:v mpeg4 -c:a libmp3lame output.mp4"

if [ "$arg" == "a" ]; then
	eval $audio
fi
if [ "$arg" == "v" ]; then
	eval $video
fi
if [ "$arg" == "s" ]; then
	eval $screengrab
fi