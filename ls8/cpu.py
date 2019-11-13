"""CPU functionality."""
import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.memory = bytearray(256)
        self.registers = [0] * 8

        self.pc = 0
        self.ir = [0] * 8
        self.mar = [0] * 8
        self.mdr = [0] * 8
        self.fl = [0] * 8

        # self.stack = StackLambda()

    def ram_read(self, address):
        value = self.memory[address]
        return value

    def ram_write(self, address, value):
        self.memory[address] = value
        return

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

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
            elif instruction == 0x82:
                self.pc += 1
                reg_n = self.ram_read(self.pc)
                self.pc += 1
                value = self.ram_read(self.pc)
                self.pc += 1
                self.registers[reg_n] = value

            elif instruction == 0x47:
                self.pc += 1
                print(int(self.registers[self.ram_read(self.pc)]))
                self.pc += 1
            else:
                print(f"exception: no instruction {instruction}")







        pass
