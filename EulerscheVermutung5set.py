# 2019-11-19
# list 16
# dict  4.x
# set   3.x no matter if frozen or not
# Eulersche Vermutung
# https://de.wikipedia.org/wiki/Eulersche_Vermutung
# 27^5 + 85^5 + 110^5 +133^5 = 144^5
#
import time
lir = 150
runtime = time.time()
lp5 = [x**5 for x in range(lir)]
sp5 = set([x**5 for x in range(lir)])

li4 = lir - 1 
li3 = lir - 2
li2 = lir - 3
li1 = lir - 4
cnt, i1 = 0, 1
while i1 < li1:
    i2 = i1 + 1
    while i2 < li2:
        i3 = i2 + 1
        while i3 < li3:
            i4 = i3 + 1
            while i4 < li4:
                cnt += 1
                sum = lp5[i1] + lp5[i2] + lp5[i3] + lp5[i4] 
                if(sum > lp5[-1]): 
                    break
                
                if sum in sp5:
                    i5 = lp5.index(sum)
                    print(f"Bingo! need {cnt} trials")
                    print(lp5[i1], "+", lp5[i2], "+", lp5[i3], "+", lp5[i4], "=", sum)
                    print(i1,i2,i3,i4,i5)
                    runtime = time.time() - runtime 
                    print(f"run time: {runtime}")
                    print(f"ops per second: {cnt/runtime}")
                    exit()
                i4 += 1
            i3 += 1
        i2 += 1
    i1 += 1