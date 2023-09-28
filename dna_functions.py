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
        complementary_dna = ""
        toTransform = generated_dna
        for base in generated_dna: # for i as there as as many letters to transform 
            complementary_dna += dic[base]
        return complementary_dna
    
