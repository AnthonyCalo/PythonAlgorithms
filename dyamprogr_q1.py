class S:
    def __init__(self, index):
        self.index = index
        self.LIS = []
    def get_index(self):
        return self.index
    def set_list(self, listerine):
        self.LIS = listerine
    def append_list(self, appendage):
        self.LIS.append(appendage)
    def get_list(self):
        newlist = []
        if len(self.LIS) > 0:
            for i in self.LIS:
                newlist.append(i)
        return newlist
    def get_value(self):
        listvalue = len(self.LIS)
        if listvalue < 1:
            return 0
        else:
            return listvalue
    def printall(self):
        print(self.index,":",self.LIS)

mylist = [1,10,9,2,9,3,5,3,7, 18, 110]
def Get_LIS_FSL(slist):
    #get LIS from slist
    LIS = 0
    LIS_index = 0
    for i in slist:
        if i.get_value() >= LIS:
            LIS = i.get_value()
            LIS_index = i.get_index()
    return(LIS_index)

def Longest_Inc_Sub(mylist):
    slist = []
    index = 0
    for i in mylist:
        #create an S object in slist for each index
        slist.append(S(index))
        if index == 0 or mylist[index] == min(mylist[:index+1]):
            slist[index].append_list(mylist[index])
        else:
            j = 0
            for sitem in slist[:index]:
                #length LIS
                if sitem.get_value() >= slist[index].get_value() and mylist[index] >= mylist[j]:
                    if mylist[index]==mylist[j]:
                        slist[index].set_list(slist[j].get_list())
                    else:
                        newlist = slist[j].get_list()
                        #print(newlist)
                        newlist.append(mylist[index])
                        slist[index].set_list(newlist)
                j+=1
        index+=1
    LIS_index = Get_LIS_FSL(slist)
    return(slist[LIS_index].get_list())            
        
testlist = [5,1,6,7,5,4,9,2,3,5]    
print(Longest_Inc_Sub(mylist))
print(Longest_Inc_Sub(testlist))
