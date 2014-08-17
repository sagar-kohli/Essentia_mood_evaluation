import csv


def songs_label(path):
    '''
    function opens csv file on path
    and count how many times one
    each label appears with song
    '''

    csvfile = open(path, "rb")
    data = csv.reader(csvfile)

    song_label = {}

    for row in data:
        song_id = int(row[81])
        if not song_id in song_label:
            song_label[song_id] = {}
        for i in range(102, 128+1, 2):
            if not i in song_label[song_id]:
                song_label[song_id][i] = 0
            # check if value vas marked
            # if not it's 9 here (proper values are between -1 and 1)
            if float(row[i]) < 5:
                song_label[song_id][i] += 1

    return song_label


def best_label(label_dic):
    '''
    function accept dictionary of counts per label per song
    function select best maching label and return it
    in dict
    '''
    best_labels = {}

    for song in label_dic.keys():
        best_labels[song] = {'count': 0, 'best': []}
        counts = label_dic[song]
        for label in counts.keys():
            if counts[label] > best_labels[song]['count']:
                best_labels[song]['best'] = [label]
                best_labels[song]['count'] = counts[label]
            elif counts[label] == best_labels[song]['count']:
                best_labels[song]['best'].append(label)

    return best_labels


def best_label_and_second(label_dic):
    '''
    function accept dictionary of counts per label per song
    function select best maching label and return it
    in dict
    function also add second label if near (2 avay)
    '''
    best_labels = {}

    # find best label
    for song in label_dic.keys():
        best_labels[song] = {'count': 0, 'best': []}
        counts = label_dic[song]
        for label in counts.keys():
            if counts[label] > best_labels[song]['count']:
                best_labels[song]['best'] = [label]
                best_labels[song]['count'] = counts[label]
            elif counts[label] == best_labels[song]['count']:
                best_labels[song]['best'].append(label)

    # find other near
    for song in label_dic.keys():
        counts = label_dic[song]
        for label in counts.keys():
            if counts[label] >= best_labels[song]['count'] - 2:
                best_labels[song]['best'].append(label)

    return best_labels


def label2cluster(label_dict, label_cluster, key_in_label_dict):
    '''
    fucntion transfer labels to cluster numbers
    labels per song are in lable_dict under key key_in_label_dict
    returns dict of structure song_id->key_in_label_dict->cluster
    '''

    cluster_dict = {}
    for song_id, value in label_dict.items():
        cluster_dict[song_id] = []

        for label in value[key_in_label_dict]:
            cl = label_cluster[str(label)]['cluster']
            cluster_dict[song_id].append(cl)

    return cluster_dict
