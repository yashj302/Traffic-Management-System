from random import *
"""
Random Data Generator
This script just generate random data which is written to a text/csv file
which then will be analysed to control the traffic light

Format of data generated:

Lane_3 9
Lane_2 3
Lane_3 8
Lane_1 0
Lane_3 6
Lane_2 7
Lane_1 8

Here First Column depicts the lane in which vehicles are going and 2nd column
shows respective vehicle count

Let intersection roads be like 1 2 3 4
               |        |
               |        |
               |        |
               |        |
               |  Lane1 |
   ____________T1        T2________________

   Lane 2                  Lane 4
   ____________T3        T4________________

               |        |
               |  Lane3 |
               |        |
               |        |
               |        |

T1 controlling the traffic lights that control lane 4th
Similarly T2 controlling lane 3
T3-> 4th
T4-> 2nd 



"""

#Creating new file or deleting contents
file = open("RoadData.txt","w+")
file.seek(0)
file.truncate()

#Random Data generated

Lanes_name = ['Lane_1','Lane_2','Lane_3','Lane_4']

for i in range(20):

    #Lane_Number = randint(1,4)

    f= open("RoadData.txt","a")

    random_Vehicle_count = randint(0,10)
    
    Lane_random = sample(Lanes_name, 1)
    tobewritten="%s %s\n"%(Lane_random[0],random_Vehicle_count)

    f.write(tobewritten)
    print(tobewritten)
    




