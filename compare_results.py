import json
from utils.data_collect import(
    songs_label,
    best_label,
    label2cluster,
    best_label_and_second
)
from os import listdir
import yaml

# read clusters for mood
with open('labels_clousters/clousters.json') as data_file:
    mood_cluster = json.load(data_file)

# get counting per labels per song
song_label = songs_label('survey_data/survery2dataMin1.csv')

best_label = best_label_and_second(song_label)

best_cluster = label2cluster(best_label, mood_cluster, 'best')

rights = 0
wrongs = 0

clouster_clouster = [[0 for x in range(5)] for y in range(5)]

for file in listdir('descriptors_yaml'):
    stream = open('descriptors_yaml/' + file, "r")
    docs = yaml.load(stream)

    cluster = int(docs['highlevel']['moods_mirex']['value'][7])
    song_id = int(file[:-5])

    print song_id
    print best_cluster[song_id]
    if cluster in best_cluster[song_id]:
        real_cluster = cluster
        rights += 1
    else:
        real_cluster = best_cluster[song_id][0]
        wrongs += 1

    clouster_clouster[real_cluster-1][cluster-1] += 1

    print rights, wrongs

print clouster_clouster
