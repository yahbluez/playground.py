# Eulersche Vermutung
# https://de.wikipedia.org/wiki/Eulersche_Vermutung
# 27^5 + 85^5 + 110^5 +133^5 = 144^5
#
import time

time_start = time.time()
lp5 = [x**5 for x in range(150)]
li4 = len(lp5) - 1 
li3 = len(lp5) - 2
li2 = len(lp5) - 3
li1 = len(lp5) - 4
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
                if sum in lp5:
                    i5 = lp5.index(sum)
                    print(f"Bingo! need {cnt} trials")
                    print(lp5[i1], "+", lp5[i2], "+", lp5[i3], "+", lp5[i4], "=", sum)
                    print(i1,i2,i3,i4,i5)
                    time_end = time.time()
                    print("run time:", time_end - time_start)
                    exit()
                i4 += 1
            i3 += 1
        i2 += 1
    i1 += 1