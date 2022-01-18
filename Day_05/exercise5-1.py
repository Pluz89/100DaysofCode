#Average Height
avg2=0
heights=input('Please input the heights separated by a comma:\n').split(', ')
for n in range(0, len(heights)):
    heights[n] = int(heights[n])
for avg in heights:
    avg2 += avg
tot_avg=avg2/len(heights)
print(round(tot_avg, 0))