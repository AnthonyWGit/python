import random

class DNA:
    def generate_dna(self):
        #The array of letters to choose from
        letters = ['A', 'C', 'G', 'T']
        #Initilization
        i = 0
        #this var contains empty string
        random_dna=""
        #
        while i < 30:
            random_letter = random.choice(letters)
            random_dna += random_letter
            i += 1
        return random_dna
    
    def generate_complementary(self, generated_dna):
        dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        toTransform = generated_dna
        for i in range(len(toTransform)):
            toTransform = toTransform.replace(toTransform[i], dic[toTransform[i]])
        return toTransform
    
