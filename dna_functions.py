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
    
    def generate_complementary(self, sDNA):
        dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}