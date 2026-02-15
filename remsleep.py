from datetime import datetime, timedelta

rntime=datetime.now()
#time rn

ask=int(input("How many minutes to fall asleep?: "))
askdelta = timedelta(minutes=ask)
sletime= rntime + askdelta
#minutes to fall asleep

remcycles=int(input("How many REM cycle intervals would you like to know?"))
remdelta= timedelta(hours=1, minutes=30)
#rem sleep

intervals=[]

for i in range(1, remcycles+1):
    interval=(sletime + (remdelta * i))

    hoursslept= (((interval - sletime).total_seconds())/3600)
    
    intervals.append((interval.time(), hoursslept))



cycle=0
for i in intervals:
    cycle+=1
    print(f"REM Cycle {cycle} - {i[0].strftime('%I:%M %p')} - {i[1]} hours slept")