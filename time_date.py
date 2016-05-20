'''
don not support next year
'''
month_days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
def get_f_days(f_date):
    month=int(f_date[4:6])
    month_end=month_days[month]
    today=int(f_date[6:])
    assert today<=month_end,('day too big')
    return month_end-today+1
def get_t_days(t_date):
    assert int(t_date[6:])<=month_days[int(t_date[4:6])]
    return int(t_date[6:])

def add_date(d1,days):
    res=d1+days
    str_res=str(res)
    day=int(str_res[6:])
    mon=int(str_res[4:6])
    while day > month_days[mon]:
        day-=month_days[mon]
        mon+=1
    return 20150000+day+mon*100
def get_continuous_dates(f_date,t_date):
    f_month=int(f_date[4:6])
    t_month=int(t_date[4:6])
    assert f_month<=t_month

    if f_month==t_month:
        int_f_date=int(f_date)
        int_t_date=int(t_date)

        return range(int_f_date,int_t_date+1)

    else:
        f_list=range(int(f_date),int(f_date)-int(f_date[6:])+month_days[int(f_date[4:6])]+1)
        t_list=range(int(t_date)-int(t_date[6:])+1,int(t_date)+1)
        middle_list=[]
        for mon in range(f_month,t_month-1):
            middle_list+=range(20150000+mon*100+1,20150000+mon*100+month_days[mon]+1)
        return f_list+middle_list+t_list
def get_time_list(f_date,t_date,groups):

    
    

    int_f_date=int(f_date)
    int_t_date=int(t_date)
    assert int_f_date<int_t_date,('f_date is after t_date')
    int_f_month=int(f_date[4:6])
    int_t_month=int(t_date[4:6])

    middle_days=0
    for i in range(int_f_month+1,int_t_month):
        middle_days+=month_days[i]
    f_days=get_f_days(f_date)
    t_days=get_t_days(t_date)
    total_days=f_days+t_days+middle_days
    group_size=total_days/groups
    res=[int(f_date)]
    for i in range(groups-1):
        res.append(add_date(res[-1],group_size))
    res.append(int(t_date))
    return res
