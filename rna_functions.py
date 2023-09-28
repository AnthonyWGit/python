import random

class RNA:    
    def generate_rna_new(self, generated_dna):
        dic = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'} #We will do like complementary DNA but replace all Ts with U
        toTransform = ''
        for i in generated_dna: 
            toTransform += dic[i]
        return toTransform
    
    def generate_rna_com(self, generated_rna):
        dic = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'} #We will do like complementary DNA but replace all Ts with U 
        toTransform = ''
        for i in generated_rna:
            toTransform += dic[i]
        return toTransform