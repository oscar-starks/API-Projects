# from datetime import datetime
# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%Y-%m-%d")
#     d2 = datetime.strptime(d2, "%Y-%m-%d")
#     print (abs((d2 - d1).days))

# jan_1_2020 = datetime.datetime(2020, 1, 1)
# dec_12_2020 = datetime.datetime(2020, 12, 12)

# days_between(jan_1_2020, dec_12_2020)
import datetime

jan_1_2020 = datetime.datetime(2020, 1, 1)
dec_12_2020 = datetime.datetime(2020, 12, 12)

if jan_1_2020 < dec_12_2020:
    answer = dec_12_2020-jan_1_2020
    print(answer.days)
    
    
def trial(name, classs):
    print(name, classs)
    
mydict = {"name":"Hello", "classs":"jsssss3"}

trial(**mydict)