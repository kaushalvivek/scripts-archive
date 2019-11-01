import matplotlib.pyplot as plt
import math

companies = [line.split(':', 1) for line in open('age.txt')]
ages = []
for i in range (0,60):
    ages += ([int(s) for s in companies[i][1].split() if s.isdigit()])

x = sum(ages)/len(ages)
ages2 = [ (math.ceil(ages[i]/3.4))for i in range(0,60)]
ages3 = []
for i in range (0,60) :
    if (ages2[i] > 10):
        ages3.append(10)

    elif (ages2[i] == 0):
        ages3.append(1)
    else:
        ages3.append(int(ages2[i]))

print(ages3)
final = open('finalage.txt', 'w+')
for i in range (0,60):
    final.write(str(companies[i][0])+" : "+str(ages3[i])+'\n')w
final.close()
# plt.plot(ages3)
# plt.ylabel(x)
# plt.show()
