Project is divided in two parts:
1. Random Data Generator</br>
2. Analyzer

Random Data Generator
This script just generate random data which is written to a text/csv file</br>
which then will be analysed to control the traffic light</br>

Format of data generated:</br>
Lane_3 9</br>
Lane_2 3</br>
Lane_3 8</br>
Lane_1 0</br>
Lane_3 6</br>
Lane_2 7</br>
Lane_1 8</br>

Here First Column depicts the lane in which vehicles are going and 2nd column</br>
shows respective vehicle count</br>

Let intersection roads be like 1 2 3 4</br>
</br>
![alt text](https://github.com/yashj302/Traffic-Management-System/blob/master/Intersection%20Roads.png)

T1 controlling the traffic lights that control lane 4th</br>
Similarly T2 controlling lane 3</br>
T3-> 4th</br>
T4-> 2nd </br>

Analyzer:
It Analyzes the data detects which lane number is and then sends its vehicle count to that lane's function</br>
there based on vehicle count it calculates how much time should be set to green light in traffic lights so that traffic should be minimum.

