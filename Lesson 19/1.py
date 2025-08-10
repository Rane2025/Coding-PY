import random, time

def date_time(startdate, enddate):
    print("Printing", startdate,"and",enddate)
    randomgen = random.random()
    df = '%m/%d/%Y'
    st = time.mktime(time.strptime(startdate, df))
    et = time.mktime(time.strptime(enddate, df))
    rt = st + randomgen * (et - st)
    rd = time.strftime(df, time.localtime(rt))
    return rd
print("Random date = ", date_time("1/1/2020", "1/1/2026"))