# a very garbage brainfuck interpreter in python
# it still has some bugs and weird behavior :/

class bfInterpreter():
    def __init__(self, filename: str):
        self.filename = filename
        self.load_prgm()
        self.byte_array = [0] * 30000
        self.running = True
        self.instruction_ptr = -1
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
        left_bracket_loc = self.instruction_ptr
        if self.byte_array[self.data_ptr] == 0:
            bracket_tally = 1
            while bracket_tally != 0 and self.instruction_ptr < len(self.program) - 1:
                self.instruction_ptr += 1
                if self.program[self.instruction_ptr] == '[':
                    bracket_tally += 1
                elif self.program[self.instruction_ptr] == ']':
                    bracket_tally -= 1
            
            if self.instruction_ptr >= len(self.program):
                raise SyntaxError(f"Did not find matching right bracket to the left bracket at {left_bracket_loc}.")

    def right_bracket(self):
        right_bracket_loc = self.instruction_ptr
        if self.byte_array[self.data_ptr] != 0:
            bracket_tally = 1
            while bracket_tally != 0 and self.instruction_ptr > 0:
                self.instruction_ptr -= 1
                if self.program[self.instruction_ptr] == ']':
                    bracket_tally += 1
                elif self.program[self.instruction_ptr] == '[':
                    bracket_tally -= 1
            
            if self.instruction_ptr < 0:
                raise SyntaxError(f"Did not find matching left bracket to the right bracket at {right_bracket_loc}.")

bfInterpreter(input("Please enter filename with extension here: "))