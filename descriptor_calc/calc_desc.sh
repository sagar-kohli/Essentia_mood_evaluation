#!/bin/bash

# essentia 2.1 with Gaia required

for f in ../final_together/*.mp3
do
	cd ~/Desktop/essentia/build/src/examples/
	./streaming_extractor_archivemusic ~/Dropbox/Mood_Research/izbrana\ glasba/essentia_descriptors/$f ~/Dropbox/Mood_Research/izbrana\ glasba/essentia_descriptors/"${f%.mp3}.yaml"	
done
