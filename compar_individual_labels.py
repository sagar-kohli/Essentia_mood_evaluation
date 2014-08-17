import json
from utils.data_collect import(
    songs_label,
    best_label,
    label2cluster,
    best_label_and_second
)
from os import listdir
import yaml

'''
program compare individual label essentia algorithm 
with data gathered 
compare only happines, saddnes and relaxed
'''

# columns of all tree in csv
happines_column = 104
sadnes_column = 106
relaxed_column = 122

song_label = songs_label('survey_data/survery2dataMin1.csv')

best_label = best_label_and_second(song_label)

happines = [0, 0]
saddnes = [0, 0]
relaxed = [0, 0]

for file in listdir('descriptors_yaml'):
    song_id = int(file[:-5])
    #print best_label[song_id]
    if happines_column in best_label[song_id]['best'] or \
        sadnes_column in best_label[song_id]['best'] or \
        relaxed_column in best_label[song_id]['best']:

        print song_id

        stream = open('descriptors_yaml/' + file, "r")
        docs = yaml.load(stream)

        if happines_column in best_label[song_id]['best']:
            happines_pre = docs['highlevel']['mood_happy']['value']
            happines[0] += 1 if happines_pre == 'happy' else 0
            happines[1] += 1 if not happines_pre == 'happy' else 0

        if sadnes_column in best_label[song_id]['best']:
            sadnes_pre = docs['highlevel']['mood_sad']['value']
            saddnes[0] += 1 if sadnes_pre == 'sad' else 0
            saddnes[1] += 1 if not sadnes_pre == 'sad' else 0

        if relaxed_column in best_label[song_id]['best']:
            relaxed_pre = docs['highlevel']['mood_relaxed']['value']
            relaxed[0] += 1 if relaxed_pre == 'relaxed' else 0
            relaxed[1] += 1 if not relaxed_pre == 'relaxed' else 0

print best_label

print happines
print saddnes
print relaxed
