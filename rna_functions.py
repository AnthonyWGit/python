import random

class RNA:    
    def generate_rna_new(self, generated_dna):
        dic = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} #We will do like complementary DNA but replace all Ts with U 
        toTransform = generated_dna
        for i in range(len(toTransform)):
            toTransform = toTransform.replace(toTransform[i], dic[toTransform[i]])
            toTransform2 = toTransform.replace('T', 'U') #replace all Ts with U
        return toTransform2
    
    def generate_rna_com(self, generated_rna):
        dic = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'} #We will do like complementary DNA but replace all Ts with U 
        toTransform = generated_rna
        for i in range(len(toTransform)):
            toTransform = toTransform.replace(toTransform[i], dic[toTransform[i]])
        return toTransform