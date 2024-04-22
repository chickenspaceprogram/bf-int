# a very garbage brainfuck interpreter in python

class bfInterpreter():
    def __init__(self, filename: str):
        self.filename = filename
        self.load_prgm()
        
        self.byte_array = [0] * 30000
        self.running = True
        self.instruction_ptr = 0
        self.data_ptr = 0

        while self.running:
            self.instruction_ptr += 1
            # this if tree is cursed as hell, it is painful to look at. im sorry for your eyeballs

            if self.program[self.instruction_ptr] == '>': # Moves data pointer to the cell on the right
                self.data_ptr = (self.data_ptr + 1) % 30000
            elif self.program[self.instruction_ptr] == '<': # Moves data pointer to the cell on the left
                self.data_ptr = (self.data_ptr - 1) % 30000
            elif self.program[self.instruction_ptr] == '+': # Increments the current cell
                self.byte_array[self.data_ptr] = (self.byte_array[self.data_ptr] + 1) % 256
            elif self.program[self.instruction_ptr] == '-': # Decrements the current cell
                self.byte_array[self.data_ptr] = (self.byte_array[self.data_ptr] - 1) % 256
            elif self.program[self.instruction_ptr] == '.': # Prints the current cell as an ASCII character
                print(chr(self.byte_array[self.data_ptr]), end='')
            elif self.program[self.instruction_ptr] == ',': # Inputs a value from the user into the current cell
                self.byte_array[self.data_ptr] = int(input('Enter a byte in decimal: ')) % 256
            elif self.program[self.instruction_ptr] == '[':
                self.left_bracket()
            elif self.program[self.instruction_ptr] == ']':
                self.right_bracket()
            
            if self.instruction_ptr >= len(self.program) - 1:
                self.running = False

    def load_prgm(self):
        with open(self.filename, 'r') as self.file:
            self.inputted_prgm = self.file.read()
        
        self.valid_chars = ['>', '<', '+', '-', '.', ',', '[', ']']
        self.program = ''
        for char in self.inputted_prgm:
            if char in self.valid_chars:
                self.program += char
    
    def left_bracket(self):
        pass
    
    def right_bracket(self):
        pass


bfInterpreter(input("Please enter filename with extension here: "))