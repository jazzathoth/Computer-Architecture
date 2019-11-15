"""CPU functionality."""
import sys
class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = bytearray(256)
        self.registers = [0] * 8

        self.pc = 0
        self.ir = [0]
        self.mar = [0]
        self.mdr = [0]
        self.fl = [0]

        self.stack = Stack()
        #self.SP = self.stack.stack[-1]

    def ram_read(self, address):
        value = self.memory[address]
        return value

    def ram_write(self, address, value):
        self.memory[address] = value
        return

    def load(self, file):
        """Load a program into memory."""
        read_file = open(file, 'r')
        program = []
        for line in read_file:
            if (line[0] is not "#") and (line[0] is not "\n"):
                program.append(int(line[:8], 2))


        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        for instruction in program:
            self.memory[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.registers[reg_a] += self.registers[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.registers[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        halt = False

        while not halt:
            instruction = self.ram_read(self.pc)

            if instruction == 0x01:
                halt = True
                self.pc += 1
                print("halted")
            elif instruction == 0x82:
                self.pc += 1
                reg_n = self.ram_read(self.pc)
                self.pc += 1
                value = self.ram_read(self.pc)
                self.pc += 1
                self.registers[reg_n] = value
                # print(f"set reg {reg_n} to {self.registers[reg_n]}")
                # print(f"pc = {self.pc}")

            elif instruction == 0x47:
                self.pc += 1
                print(int(self.registers[self.ram_read(self.pc)]))
                self.pc += 1

            elif instruction == 0xa2:
                self.pc += 1
                reg_n1 = self.ram_read(self.pc)
                self.pc += 1
                reg_n2 = self.ram_read(self.pc)
                self.pc += 1
                self.registers[reg_n1] = self.registers[reg_n1] * self.registers[reg_n2]
            elif instruction == 0xa7:
                self.pc += 1
                reg_n1 = self.ram_read(self.pc)
                self.pc += 1
                reg_n2 = self.ram_read(self.pc)
                self.pc += 1
                if self.registers[reg_n1] == self.registers[reg_n2]:
                    self.fl = 1
                elif self.registers[reg_n1] > self.registers[reg_n2]:
                    self.fl = 1 << 1
                elif self.registers[reg_n1] < self.registers[reg_n2]:
                    self.fl = 1 << 2
                else:
                    print(f"Something went wrong. R1: {reg_n1}, R2: {reg_n2}")
            elif instruction == 0x55:
                self.pc += 1
                reg_n = self.ram_read(self.pc)
                self.pc += 1
                if 1 & self.fl == 1:
                    self.pc = self.registers[reg_n]
                    # print(f"jumped, register {reg_n}, to loc {self.registers[reg_n]}")
            elif instruction == 0x56:
                self.pc += 1
                reg_n = self.ram_read(self.pc)
                self.pc += 1
                if 1 & self.fl == 0:
                    self.pc = self.registers[reg_n]
            elif instruction == 0x54:
                self.pc += 1
                reg_n = self.ram_read(self.pc)
                self.pc += 1
                self.pc = self.registers[reg_n]
            else:
                print(f"exception: no instruction {instruction}")







        return
