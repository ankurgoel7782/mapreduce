#!/bin/bash
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar -file /home/hduser/mappernew.py    -mapper "/home/hduser/mappernew.py $1 $2" -file /home/hduser/reducer.py   -reducer "/home/hduser/reducer.py $3" -input /user/hduser/vikram/* -output /user/hduser/vikram/$4
