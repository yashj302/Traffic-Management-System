import array
import time
print("TIME::::::::::",time.time()," :::::::::::::TIME")
import datetime
time_traffic = int(1525189000)     #CurrentTime : time.time()*1000  #tested Time : "1525189000"
time_store = datetime.datetime.fromtimestamp(time_traffic / 1000).strftime('%H:%M:%S')
print ("--------------",time_store,"----------")

array.array('i')
#Analysing Data from file
Line_count = 0
with open("RoadData.txt","r") as file_count:
    for line in file_count:
        Line_count += 1
#print("NUMBER OF LINES ___________  ",Line_count,"________________ ")        
file = open("RoadData.txt","r")
Line_number = 0

#Variables Defined for Vehicle count According to lanes
Lane_1_count = 0.0
Lane_2_count = 0.0
Lane_3_count = 0.0
Lane_4_count = 0.0

tLane_1_count = 0
tLane_2_count = 0
tLane_3_count = 0
tLane_4_count = 0


"""
#Series of traffic light t1 , t2 , t3 and then t4
t2traffic = 0
t3traffic = 0
t4traffic = 0
"""
#Variable Defined for Delay count for Traffic Light in Lanes
Max_delay = 50.0
Min_delay = 15.0
Initial_delay_all = 30.0
Delay_Lane_1 = 30.0
Delay_Lane_2 = 30.0
Delay_Lane_3 = 30.0
Delay_Lane_4 = 30.0

#Delay Variable that is to be added to another Lane's traffic light
Diff_delay_1 = 0.0
Diff_delay_2 = 0.0
Diff_delay_3 = 0.0
Diff_delay_4 = 0.0

Vechile_count = array.array('i',(0 for i in range(0,Line_count)))

def lane_one(Lane_1_count):
    print(Lane_1_count)
    global Delay_Lane_1,Diff_delay_1,Max_delay,Initial_delay_all,Min_delay,tLane_1_count
    tLane_1_count = int(tLane_1_count) + int(Lane_1_count)
    if(int(Lane_1_count)>0):
        print("Initial Delayed Value 1 ::::::  ",Delay_Lane_1,"  :::::::::")
        Delay_Lane_1 = Delay_Lane_1 + float(Lane_1_count)*0.4
        print("Delayed Value 1 :::::: ", Delay_Lane_1 ," :::::::::")
        
    if(int(Lane_1_count)<1):
        Delay_Lane_1 = float(Delay_Lane_1) - float(1)*0.4
        print("Delayed Value negative ---- ",Delay_Lane_1,"--------")
        
    if(Delay_Lane_1>Max_delay):
        Delay_Lane_1 = Max_delay
        
    if(Delay_Lane_1<Min_delay):
        Delay_Lane_1 = Min_delay
        
    Diff_delay_1 = Delay_Lane_1 - Initial_delay_all    
    print("---------------")
    print(Diff_delay_1)
    print("---------------")    
        
def lane_two(Lane_2_count):
    print(Lane_2_count)
    global Delay_Lane_2,Diff_delay_2,Max_delay,Initial_delay_all,Min_delay,tLane_2_count
    tLane_2_count = int(tLane_2_count) + int(Lane_2_count)
    if(int(Lane_2_count)>0):
        print("Initial Delayed Value 2 ::::::",Delay_Lane_2," ::::::::::")
        Delay_Lane_2 = Delay_Lane_2 + float(Lane_2_count)*0.4
        print("Delayed Value 2 ::::::",Delay_Lane_2," ::::::::::")

    if(int(Lane_2_count)<1):
        Delay_Lane_2 = Delay_Lane_2 - float(1)*0.4
        
    if(Delay_Lane_2>Max_delay):
        Delay_Lane_2 = Max_delay
        
    if(Delay_Lane_2<Min_delay):
        Delay_Lane_2 = Min_delay
        
    Diff_delay_2 = Delay_Lane_2 - Initial_delay_all    
    print("---------------")
    print(Diff_delay_2)
    print("---------------")      

def lane_three(Lane_3_count):
    global Delay_Lane_3,Diff_delay_3,Max_delay,Initial_delay_all,Min_delay,tLane_3_count
    print(Lane_3_count)
    tLane_3_count = int(tLane_3_count) + int(Lane_3_count)
    if(int(Lane_3_count)>0):
        print("Initial Delayed Value 3 ::::::",Delay_Lane_3," ::::::::::")
        Delay_Lane_3 = Delay_Lane_3 + float(Lane_3_count)*0.4
        print("Delayed Value 3 ::::::",Delay_Lane_3," ::::::::::")

    if(int(Lane_3_count)<1):
        Delay_Lane_3 = Delay_Lane_3 - float(1)*0.4
        
    if(Delay_Lane_3>Max_delay):
        Delay_Lane_3 = Max_delay
        
    if(Delay_Lane_3<Min_delay):
        Delay_Lane_3 = Min_delay
        
    Diff_delay_3 = Delay_Lane_3 - Initial_delay_all    
    print("---------------")
    print(Diff_delay_3)
    print("---------------")      
    

def lane_four(Lane_4_count):
    global Delay_Lane_4,Diff_delay_4,Max_delay,Initial_delay_all,Min_delay,tLane_4_count
    print(Lane_4_count)
    tLane_4_count = int(tLane_4_count) + int(Lane_4_count)
    if(int(Lane_4_count)>0):
        print("Initial Delayed Value 4 ::::::",Delay_Lane_4," ::::::::::")
        Delay_Lane_4 = Delay_Lane_4 + float(Lane_4_count)*0.4
        print("Delayed Value 4 ::::::",Delay_Lane_4," ::::::::::")

    if(int(Lane_4_count)<1):
        Delay_Lane_4 = Delay_Lane_4 - float(1)*0.4
        
    if(Delay_Lane_4>Max_delay):
        Delay_Lane_4 = Max_delay
        
    if(Delay_Lane_4<Min_delay):
        Delay_Lane_4 = Min_delay
        
    Diff_delay_4 = Delay_Lane_4 - Initial_delay_all    
    print("---------------")
    print(Diff_delay_4)
    print("---------------")      


for line in file:
    fields = line.split(" ")
    Lanes = fields[0]
    Vehicle_count = fields[1]
        #Comparing Values of Column 1 i.e detecting which lane it is
    if(Lanes=="Lane_1"):
        lane_one(Vehicle_count)
            
    if(Lanes=="Lane_2"):
        lane_two(Vehicle_count)

    if(Lanes=="Lane_3"):
        lane_three(Vehicle_count)

    if(Lanes=="Lane_4"):
        lane_four(Vehicle_count)
        

    #print(Lanes+" "+Vehicle_count)
def display_all_values():
    print("--------------------------------------------------------------------------")
    print("---------------------------------FINAL DATA-------------------------------")
    print("--------------------------------------------------------------------------")
    print("Delay Lane 1 : ",str(round(Delay_Lane_1, 2)), "  Difference time : ",str(round(Diff_delay_1, 2)))
    print("Delay Lane 2 : ",str(round(Delay_Lane_2, 2)), "  Difference time : ",str(round(Diff_delay_2, 2)))
    print("Delay Lane 3 : ",str(round(Delay_Lane_3, 2)), "  Difference time : ",str(round(Diff_delay_3, 2)))
    print("Delay Lane 4 : ",str(round(Delay_Lane_4, 2)), "  Difference time : ",str(round(Diff_delay_4, 2)))
display_all_values()

def manipulatingtime():
    global Lane_1_count,Lane_2_count,Lane_3_count,Lane_4_count
    global time_traffic,time_store,tLane_1_count
    Green_time_for_1 = time_traffic + int(Delay_Lane_1)*1000
    print("--------------------------------------------------------------------------")
    print("---------------------------------RESULT-----------------------------------")
    print("--------------------------------------------------------------------------")
    
    time_to_be_displayed = datetime.datetime.fromtimestamp(Green_time_for_1 / 1000).strftime('%H:%M:%S')
    print("Green Light T1 till :- ",time_to_be_displayed)
    Green_time_for_2 = Green_time_for_1 + int(Delay_Lane_2)*1000
    time_to_be_displayed = datetime.datetime.fromtimestamp(Green_time_for_2 / 1000).strftime('%H:%M:%S')
    print("Green Light T2 till :- ",time_to_be_displayed)
    Green_time_for_3 = Green_time_for_2 + int(Delay_Lane_1)*1000
    time_to_be_displayed = datetime.datetime.fromtimestamp(Green_time_for_3 / 1000).strftime('%H:%M:%S')
    print("Green Light T3 till :- ",time_to_be_displayed)
    Green_time_for_4 = Green_time_for_3 + int(Delay_Lane_1)*1000
    time_to_be_displayed = datetime.datetime.fromtimestamp(Green_time_for_4 / 1000).strftime('%H:%M:%S')
    print("Green Light T4 till :- ",time_to_be_displayed)
    
    print("-----------------------------Vehicle Count--------------------------------")
    print("Lane 1 : ",tLane_1_count)
    print("Lane 2 : ",tLane_2_count)
    print("Lane 3 : ",tLane_3_count)
    print("Lane 4 : ",tLane_4_count)
    print("\n\n\n\n\n\n")
manipulatingtime()

