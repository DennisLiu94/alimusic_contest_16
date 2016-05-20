import qzliu_util as qzl
import time_date as td


if __name__=='__main__':
    data=qzl.load_data('data/artist_in_interval.pkl')
    data=data[-1]
    time_list=td.get_continuous_dates('20150901','20151030')
    print time_list
    res=[]
    for date in time_list:
        tmp=[]
        for ar in data.keys():
            tmp_str=str(ar)+','+str(data[ar])+','+str(date)
            tmp.append(tmp_str)
        res+=tmp
    qzl.writelines(res,'data/first_sub.csv')
