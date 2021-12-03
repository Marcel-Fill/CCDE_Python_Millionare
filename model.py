
class question: 
    def __init__(self,question, lvl, awns ,awns1,awns2, awns3 ):
        self.question = question
        self.lvl = lvl
        self.awns = awns
        self.awns1 = awns1
        self.awns2 = awns2
        self.awns3 = awns3
         
    
    def __str__(self):
        return self.question + "  " + self.lvl + "\t" + self.awns + " | " + self.awns1 + " | " + self.awns2 + " | " + self.awns3
        
    
