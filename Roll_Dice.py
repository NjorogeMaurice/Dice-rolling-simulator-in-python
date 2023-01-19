
## importing necessary libraries
import numpy as np
from tabulate import tabulate
import random 

## Roll dice class
class Roll_Dice:
    
    ## our constructor
    def __init__(self):
         ## The following represents the necessary counters corresponding to the 
        ## number of faces of a dice
        self.counter1=0
        self.counter2=0
        self.counter3=0
        self.counter4=0
        self.counter5=0
        self.counter6=0 
        
    ## random number generator function
    ## Using the random module
    ## It returns a value between 0.0 and 1.0 
    def random_gen(self):
        rand_num = random.random()
        return rand_num

    ## What follows next is a counter module
    ## According to the value of the parameter
    ## It increments the corresponding counter of the dice
    def counter(self,x):
        ## rounding off the value of x into 2 decimal places
        ## for simplication
        x = round(x,2)
        ## If clauses
        ## Here we use the np.arange formula to 
        ## return a range of decimal point values
        if(x in np.arange(0.00,0.18,0.01)):
            self.counter1+=1
        elif(x in np.arange(0.18,0.36,0.01)):
            self.counter2+=1
        elif(x in np.arange(0.36,0.53,0.01)):
            self.counter3+=1
        elif(x in np.arange(0.53,0.70,0.01)):
            self.counter4+=1
        elif(x in np.arange(0.70,0.87,0.01)):
            self.counter5+=1
        else:
            self.counter6+=1
            
    ## This is a one-time dice rolling module       
    def roll_dice(self):
        ## a random number is generated
        ## by calling the random_gen module
        face_number = self.random_gen()
        ## incrementing the corresponding counter
        #self.counter(face_number)
        self.counter(face_number)
    
    ## rolling the dice 1000 times, boom
    def rolling(self):
        count = 1
        while(count<1001):
            ## We now roll our dice
            self.roll_dice()
            count+=1
    
    ## displaying our results in a tabular format
    def results(self):
        data=[['1',self.counter1,round((self.counter1/10),1)],
             ['2',self.counter2,round((self.counter2/10),1)],
             ['3',self.counter3,round((self.counter3/10),1)],
             ['4',self.counter4,round((self.counter4/10),1)],
             ['5',self.counter5,round((self.counter5/10),1)],
             ['6',self.counter6,round((self.counter6/10),1)],
             ['Total',(self.counter1+
                        self.counter2+
                        self.counter3+
                        self.counter4+
                        self.counter5+
                        self.counter6  ),
              round((self.counter1/10),1)+
              round((self.counter2/10),1)+
              round((self.counter3/10),1)+
              round((self.counter4/10),1)+
              round((self.counter5/10),1)+
              round((self.counter6/10),1)
             ]]

        print(tabulate(data,headers=['Face Number','Frequency','Percentage']))
        
        
        
### <-----------Happy Coding, by Njoroge Maurice------------------------------->