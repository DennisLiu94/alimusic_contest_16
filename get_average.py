import qzliu_util as qzl
import get_songartist_dict as gsd
import time_date
from collections import Counter
def split_by_time(time_list,records):
    res=[]
    for i in range(len(time_list)-1):
        f_date=time_list[i]
        t_date=time_list[i+1]

        tmp=[]
        

        for r in records:
            if int(r[4])>=f_date and int(r[4])<t_date:
                tmp.append(r)
        res.append(tmp)
    return res
def get_play_list(record_groups):
    res=[]
    for group in record_groups:
        tmp=[]
        for r in group:
            if r[3] =='1':
                tmp.append(r[1])
        res.append(tmp)
    return res
def count_play(play_list):
    res=[]
    for group in play_list:
        res.append(Counter(group))
    return res

def get_artist_play(artist2song,play):
    res=[]
    artist=artist2song.keys()

    for counter in play:
        tmp={}
        for ar in artist:
            songs=artist2song[ar]
            for song in songs:
                if song in counter:
                    if not ar in tmp:
                        tmp[ar]=counter[song]
                    else:
                        tmp[ar]+=counter[song]
        res.append(tmp)
    return res
def get_average(artist_in_intervals,date_list):
    res=[]
    for i in range(len(artist_in_intervals)):
        f_date=date_list[i]
        t_date=date_list[i+1]
        interval=t_date-f_date
        d=artist_in_intervals[i]
        tmp={}
        for k in d.keys():
            tmp[k]=d[k]/interval
        res.append(tmp)
    return res

if __name__=='__main__':
    '''
    lines=qzl.readlines('data/mars_tianchi_user_actions.csv')
    records=gsd.parse(lines)
    time_list=time_date.get_time_list(f_date='20150301',t_date='20150830',groups=12)
    
    record_groups=split_by_time(time_list,records)
    qzl.dump_data(record_groups,'data/record_groups.pkl')
    '''
    time_list=time_date.get_time_list(f_date='20150301',t_date='20150830',groups=12)
    record_groups=qzl.load_data('data/record_groups.pkl')
    play_list=get_play_list(record_groups)
    play_in_intervals=count_play(play_list)

    artist2song=qzl.load_data('data/artist2song.pkl')

    artist_in_intervals=get_artist_play(artist2song,play_in_intervals)
    artist_in_intervals=get_average(artist_in_intervals,time_list)
    qzl.dump_data(artist_in_intervals,'data/artist_in_interval.pkl')
