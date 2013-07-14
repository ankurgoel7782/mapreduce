from os import popen
dfs_cmd = "/usr/local/hadoop/bin/hadoop dfs -cat " + "/user/hduser/vikram/free"  + "/part-00000 > /home/hduser/data/tmp/test" 
print dfs_cmd
f = popen(dfs_cmd)
ins = open( "/home/hduser/data/tmp/test", "r" )
for line in ins:
    print line

