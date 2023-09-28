#This file will handle all things related to tkinter
from tkinter import * #Import all functions from tkinter
from dna_functions import DNA
from rna_functions import RNA
#creating a window on script execution

class Display:
    def __init__(self, root):
        self.root = root
        root.geometry("500x500")
        root.title("DNA bundle")      
        #elements appear in column in the order we pack them 
        # Create a Text widget for displaying the DNA string
        self.output_text_dna = Text(root, width=30, height=1) #This part actually creates the window in memory ??
        self.output_text_dna.pack() #pack allows us to put it in the main window 

        generate_button_dna = Button(self.root, text="Generate DNA", command=self.generate_and_print_dna)        
        generate_button_dna.pack()

        self.output_text_dna_com = Text(root, width=30, height=1)
        self.output_text_dna_com.pack()
        # this button has to not work in when no dna is generated
        generate_button_dna_com = Button(self.root, text="Generate complementary DNA", command=self.generate_complementary)        
        generate_button_dna_com.pack()

        self.output_text_rna = Text(root, width=30, height=1)
        self.output_text_rna.pack()

        generate_button_rna = Button(self.root, text="Generate RNA", command=self.generate_rna)        
        generate_button_rna.pack()

    def generate_and_print_dna(self):
        dna = DNA() #there is no new Object like in php
        global generated_dna #global var declaration 
        generated_dna = dna.generate_dna()
        print(generated_dna) #python has no echo but uses print() kinda like C 

        # Clear the Text widget before displaying the new result
        self.output_text_dna.delete("1.0", "end") #delete the first line in the widget

        # Insert the DNA string into the Text widget
        self.output_text_dna.insert("1.0", generated_dna) #insert in the first line at the column 0 in the widget
    
    def generate_complementary(self):
        dna = DNA()
        generated_dna_com = dna.generate_complementary(generated_dna)

        self.output_text_dna_com.delete("1.0", "end") #delete the first line in the widget
        self.output_text_dna_com.insert("1.0", generated_dna_com) #insert in the first line at the column 0 in the widget

    def generate_rna(self):
        rna = RNA()
        generated_rna = rna.generate_rna_new(generated_dna)

        self.output_text_rna.delete("1.0", "end") #delete the first line in the widget
        self.output_text_rna.insert("1.0", generated_rna) #insert in the first line at the column 0 in the widget

if __name__ == "__main__":
    root = Tk()
    app = Display(root)
    root.mainloop() # this keeps our window running until the user clicks X 