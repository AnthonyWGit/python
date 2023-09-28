import random

class RNA:
    def generate_rna(self):
        #The array of letters to choose from
        letters = ['A', 'C', 'G', 'U']
        #Initilization
        i = 0
        #this var contains empty string
        random_rna=""
        #
        while i < 30:
            random_letter = random.choice(letters)
            random_rna += random_letter
            i += 1
        return random_rna
    
    def generate_rna_new(self, generated_dna):
        dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} #We will do like complementary DNA but replace all Ts with U 
        toTransform = generated_dna
        for i in range(len(toTransform)):
            toTransform = toTransform.replace(toTransform[i], dic[toTransform[i]])
            toTransform2 = toTransform.replace('T', 'U') #replace all Ts with U
        return toTransform2