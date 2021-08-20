class men:
    def __init__(self, man_name, preference_list):
        self.mans_name=man_name
        self.preference_list=preference_list
        self.matched= False
        self.proposals=0
        self.next_proposal=len(self.preference_list)-self.proposals
        self.match=''

    def __repr__(self):
        return self.mans_name

    def proposal(self):
        #woman he is proposing to.
        #number of proposals = number on list of preferences he is proposing to
        woman = self.preference_list[self.proposals]
        #call woman response to proposal
        response = woman.proposal_response(self.mans_name)
        
        #will have to adjust bnased on wemon class
        if response==True:
            self.matched=True
            self.match=woman
        else:
            #print('here')
            self.matched=False
            self.proposals+=1
            return(self.proposal())
    
    def lady_left(self):
        self.matched=False
        self.match=''
        self.proposals+=1

    def is_matched(self):
        return(self.matched)
    def print_match(self):
        return(print(self.match))

class women:
    def __init__(self, wname, Wpreference_list):
        self.name = wname
        self.preference_list= Wpreference_list
        self.matched=False
        self.match=''
        if self.match != '':
            self.match_preference_number=self.preference_list.index(self.match)
    def __repr__(self):
        return(self.name)

    def proposal_response(self, proposer):
        #print('called')
        if self.match=='':            
            self.matched == True
            self.match=proposer
            self.match_preference_number=self.preference_list.index(self.match)
            #print('blank lady matched', self.name)
            return True
        elif self.match!='' and self.match_preference_number > self.preference_list.index(proposer):
            print('{} left {} for {}'.format(self.name, self.match, proposer))
            match = eval(self.match)
            match.lady_left()
            self.matched == True
            self.match=proposer
            self.match_preference_number=self.preference_list.index(self.match)
            return True 
        else:
            return False
    def print_match(self):
        print(self.match)


alice = women('alice',['tom','jim', 'Jon', 'tony'])
jane = women('jane',['tom', 'tony','jim', 'Jon'])
tina = women('tina',['jim','tom', 'tony', 'Jon'])
pam = women('pam', ['tom','jim', 'Jon', 'tony'])



Jon = men('Jon', [alice, jane, pam, tina])
tony = men('tony', [jane, pam, tina, alice])
tom = men('tom', [jane, tina, pam, alice])
jim = men('jim', [alice, jane, tina, pam])


list_of_men = [Jon, tom, tony, jim]


everyone_matched=False
while everyone_matched !=True:
    #print('back here')
    for man in list_of_men:
        if man.is_matched()==True:
            #print('fart')
            pass
        else:
            man.proposal()
    for man in list_of_men:
        #print(man, man.is_matched())
        if man.is_matched()==False:
            everyone_matched=False
            break
        else:
            everyone_matched=True

for man in list_of_men:
    print(man, end=": ")
    man.print_match()

#jane.print_match()
#tina.print_match()






