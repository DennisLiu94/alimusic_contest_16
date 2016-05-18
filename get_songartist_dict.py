import qzliu_util as qzl


def parse(lines):
    res=[line.strip().split(',') for line in lines]
    return res


if __name__=='__main__':
    lines=qzl.readlines('data/mars_tianchi_songs.csv')
    records=parse(lines)

    artist=set()
    artist_list=[r[1] for r in records]
    artist.update(artist_list)

    qzl.dump_data(artist,'data/artist_set.pkl')
    
    artist2song={}

    for ar in list(artist):
        artist2song[ar]=[]
    for r in records:
        if not r[0] in artist2song[r[1]]:
            artist2song[r[1]].append(r[0])
    

    song=set()
    song_list=[r[0] for r in records]
    song.update(song_list)
    qzl.dump_data(song,'data/song_list')

    song2artist={}

    for r in records:
        if r[0] in song2artist and song2artist[r[0]]!=r[1]:
            print 'err'
        song2artist[r[0]]=r[1]
    qzl.dump_data(artist2song,'data/artist2song.pkl')
    qzl.dump_data(song2artist,'data/song2artist.pkl')

