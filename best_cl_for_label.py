import json
from utils.data_collect import(
    songs_label,
    best_label,
    label2cluster
)
from os import listdir
import yaml

'''
this program compare which clouster mood_cluster
most often belongs to label
'''


# read clusters for mood
with open('labels_clousters/clousters1.json') as data_file:
    mood_cluster = json.load(data_file)

# get counting per labels per song
song_label = songs_label('survey_data/survery2dataMin1.csv')

best_label = best_label(song_label)

labels_range = range(102, 129, 2)  # range with cluster label

belonging = [[0 for x in range(5)] for y in range(20)]

for song, labels in best_label.items():
    # open file with data for this song
    stream = open('descriptors_yaml/' + str(song) + '.yaml', "r")
    docs = yaml.load(stream)
    cluster = int(docs['highlevel']['moods_mirex']['value'][7])

    for label in labels['best']:
        lab = labels_range.index(label)
        belonging[lab][cluster-1] += 1

print belonging
