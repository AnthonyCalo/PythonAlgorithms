#******************************************************************************
# paint2.py
#******************************************************************************
# Name: Anthony Calo
#******************************************************************************
#
file = open("intervals.txt", "r")

def overlaps(x,y):
    #1 starts after orginal
    if y[0] >= x[1] and x[0] < y[1]:
        return False
    #original starts after 1
    if x[0] >= y[1] and y[0] < x[1]:
        return False
    return True

x = []
for line in file:
    splitline = line.split()
    d2_list = []
    a = splitline[0].strip('[')
    b = a.strip(',')
    #first number as a float is b
    b = float(b)
    c = splitline[1].strip(']')
    #second number as a float = c
    c = float(c)
    d2_list.append(b)
    d2_list.append(c)
    x.append(d2_list)
    
def recursive_paint(x):
    distance_painted = 0
    #last element just return the total distance
    if len(x) == 1:
        distance_painted += x[0][1] - x[0][0]
        return distance_painted
    L = len(x) - 1
    for i in range(len(x)-1):
        if overlaps(x[L], x[i]):
            #if x[i] encapsulates the one we are comparing to  
            if x[L][0] >= x[i][0] and x[L][1] <= x[i][1]:
                del x[L]
                return distance_painted + recursive_paint(x)
            #if the last element encapsulates x[i]
            elif x[L][0] <= x[i][0] and x[L][1] >= x[i][1]:
                #then x{i} will become the last element
                x[i][0] = x[L][0]
                x[i][1] = x[L][1]
                del x[L]
                return distance_painted + recursive_paint(x)
            #if the last element starts after x[i] and ends after
            elif x[L][0] > x[i][0] and x[L][1] > x[i][1]:
                #replace the x[i] y coordinate with the last elements
                x[i][1] = x[L][1]
                del x[L]
                return distance_painted + recursive_paint(x)
            #only thing left is last element starts before x[i]
            else:
                #replace x[i]s first one then del last and recall function
                x[i][0]= x[L][0]
                del x[L]
                return distance_painted + recursive_paint(x)
    difference = x[L][1] - x[L][0] 
    distance_painted += difference
    del x[L]
    return distance_painted + recursive_paint(x)       
print("The total painted length is {0}".format(recursive_paint(x)))
