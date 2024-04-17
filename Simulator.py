final = []
instructions = []
reg_dict = {
  "00000":"zero", "00001":"ra", "00010":"sp" ,  "00011":"gp", "00100":"tp",
    "00101":"t0", "00110":"t1",  "00111":"t2",  "01000":"s0", "01000":"fp",
    "01001":"s1", "01010":"a0",  "01011":"a1",  "01100":"a2", "01101":"a3",
    "01110":"a4", "01111":"a5",  "10000":"a6",  "10001":"a7", "10010":"s2",
    "10011":"s3", "10100":"s4",  "10101":"s5",  "10110":"s6", "10111":"s7",
    "11000":"s8", "11001":"s9", "11010":"s10", "11011":"s11", "11100":"t3",
    "11101":"t4", "11110":"t5", "11111":"t6"
}


reg_value = {'zero': "0b00000000000000000000000000000000", 'ra': "0b00000000000000000000000000000000", 'sp': "0b00000000000000000000000000000000", 'gp': "0b00000000000000000000000000000000", 'tp': "0b00000000000000000000000000000000", 't0': "0b00000000000000000000000000000000", 't1': "0b00000000000000000000000000000000",
  't2': "0b00000000000000000000000000000000", 's0': "0b00000000000000000000000000000000", 'fp': "0b00000000000000000000000000000000", 's1': "0b00000000000000000000000000000000", 'a0': "0b00000000000000000000000000000000", 'a1': "0b00000000000000000000000000000000", 'a2': "0b00000000000000000000000000000000",
    'a3': "0b00000000000000000000000000000000", 'a4': "0b00000000000000000000000000000000", 'a5': "0b00000000000000000000000000000000", 'a6': "0b00000000000000000000000000000000", 'a7': "0b00000000000000000000000000000000", 's2': "0b00000000000000000000000000000000", 's3': "0b00000000000000000000000000000000",
      's4': "0b00000000000000000000000000000000", 's5': "0b00000000000000000000000000000000", 's6': "0b00000000000000000000000000000000", 's7': "0b00000000000000000000000000000000", 's8': "0b00000000000000000000000000000000", 's9': "0b00000000000000000000000000000000", 's10': "0b00000000000000000000000000000000",
        's11': "0b00000000000000000000000000000000", 't3': "0b00000000000000000000000000000000", 't4': "0b00000000000000000000000000000000", 't5': "0b00000000000000000000000000000000", 't6': "0b00000000000000000000000000000000"}

datamemory = {
"0x00010000":"0b00000000000000000000000000000000","0x00010004":"0b00000000000000000000000000000000","0x00010008":"0b00000000000000000000000000000000","0x0001000c":"0b00000000000000000000000000000000","0x00010010":"0b00000000000000000000000000000000","0x00010014":"0b00000000000000000000000000000000","0x00010018":"0b00000000000000000000000000000000","0x0001001c":"0b00000000000000000000000000000000","0x00010020":"0b00000000000000000000000000000000","0x00010024":"0b00000000000000000000000000000000","0x00010028":"0b00000000000000000000000000000000","0x0001002c":"0b00000000000000000000000000000000","0x00010030":"0b00000000000000000000000000000000","0x00010034":"0b00000000000000000000000000000000","0x00010038":"0b00000000000000000000000000000000","0x0001003c":"0b00000000000000000000000000000000","0x00010040":"0b00000000000000000000000000000000","0x00010044":"0b00000000000000000000000000000000","0x00010048":"0b00000000000000000000000000000000","0x0001004c":"0b00000000000000000000000000000000","0x00010050":"0b00000000000000000000000000000000","0x00010054":"0b00000000000000000000000000000000","0x00010058":"0b00000000000000000000000000000000","0x0001005c":"0b00000000000000000000000000000000","0x00010060":"0b00000000000000000000000000000000","0x00010064":"0b00000000000000000000000000000000","0x00010068":"0b00000000000000000000000000000000","0x0001006c":"0b00000000000000000000000000000000","0x00010070":"0b00000000000000000000000000000000","0x00010074":"0b00000000000000000000000000000000","0x00010078":"0b00000000000000000000000000000000","0x0001007c":"0b00000000000000000000000000000000"
             }
#code for R-type instruction
def execute_r_type_instruction(instruction, rd, rs1, rs2, registers):
    global pc
    pc = pc + 4
    rd=int(rd,2)
    rs1=int(rs1,2)
    rs2=int(rs2,2)
    if instruction == "ADD":
        registers[rd] = registers[rs1] + registers[rs2]
    elif instruction == "SUB":
        registers[rd] = registers[rs1] - registers[rs2]
    elif instruction == "SLT":
        registers[rd] = 1 if registers[rs1] < registers[rs2] else 0
    elif instruction == "SLTU":
        registers[rd] = 1 if registers[rs1] < registers[rs2] else 0
    elif instruction == "XOR":
        registers[rd] = registers[rs1] ^ registers[rs2]
    elif instruction == "SLL":
        registers[rd] = registers[rs1] << registers[rs2]
    elif instruction == "SRL":
        registers[rd] = registers[rs1] >> registers[rs2]
    elif instruction == "OR":
        registers[rd] = registers[rs1] | registers[rs2]
    elif instruction == "AND":
        registers[rd] = registers[rs1] & registers[rs2]

#code for I-type instruction
def execute_i_type_instruction(instruction, rd, rs1, imm, registers):
    global pc
    rd=int(rd,2)
    rs1=int(rs1,2)
    imm=int(imm,2)
    if instruction == "ADDI":
        registers[rd] = registers[rs1] + imm
        pc = pc + 4
    elif instruction == "LW":
        registers[rd] = datamemory[registers[rs1] + imm]   
        pc = pc + 4
    elif instruction == "SLTIU":
        registers[rd] = 1 if registers[rs1] < imm else 0
        pc = pc + 4
    elif instruction == "JALR":
        registers[rd] = pc + 4
        pc = registers[rs1] + imm 
#code for S-type instruction
def execute_s_type_instruction(instruction, rs1, rs2, imm, registers):
    global pc
    pc = pc + 4
    rs1=int(rs1,2)
    rs2=int(rs2,2)
    imm=int(imm,2)
    if instruction == "SW":
        datamemory[registers[rs1] + imm] = registers[rs2]                             

#code for B-type instruction
def execute_b_type_instruction(instruction, rs1, rs2, imm, registers):
    global pc
    temp1=twos_complement_bin_to_int(sext(imm,False))
    rs1 =int(rs1,2)
    rs2= int(rs2,2)
    if instruction == "BEQ":
        if registers[rs1] == registers[rs2]:
            
            pc = pc +temp1 
        else :
            pc = pc + 4
    elif instruction == "BNE":
        if registers[rs1] != registers[rs2]:
            pc = pc + temp1
        else :
            pc = pc + 4
    elif instruction == "BLT":
        if registers[rs1] < registers[rs2]:
            pc = pc + temp1
        else :
            pc = pc + 4
    elif instruction == "BLTU":
        if registers[rs1] < registers[rs2]:
            pc = pc + temp1
        else :
            pc = pc + 4
    elif instruction == "BGE":
        if registers[rs1] >= registers[rs2]:
            pc = pc + temp1
        else :
            pc = pc + 4
    elif instruction == "BGEU":
        if registers[rs1] >= registers[rs2]:
            pc = pc + temp1
        else :
            pc = pc + 4
    else:
        pc = pc + temp1

#code for U-type instruction
def execute_u_type_instruction(instruction, rd, imm, registers):

    global pc
    rd=int(rd,2)
    imm=int(imm,2)
    pc = pc + 4
    if instruction == "LUI":
        registers[rd] = imm << 12
    elif instruction == "AUIPC":
        registers[rd] = pc + imm << 12

#code for J-type instruction
def execute_j_type_instruction(instruction, rd, imm, registers):   
    global pc 
    rd=int(rd,2)
    temp1=twos_complement_bin_to_int(sext(imm,False))
    if instruction == "JAL":
        registers[rd] = pc + 4
        pc = pc + temp1
   

registers = [0] * 32  # Initialize registers
def twos_complement_bin_to_int(binary_str):

    if binary_str[0] == '1':

        num = int(binary_str, 2)

    else:
        
        return int(binary_str, 2)


def sext(num,integer=True):
    signbit=num[0]
    extra=32-len(num)
    if(integer):
        return int(extra*signbit+num,2) #change
    return extra*signbit+num


# Function to sign-extend immediate values
def sign_extend(imm, bits):
    if imm & (1 << (bits - 1)):
        imm -= 1 << bits
    return imm

# Update the program counter (pc)
def update_pc(pc, imm):
    return pc + 4

#input binary num
pc = 0
# Function to decode and execute instructions
def execute_instruction(binary, pc, registers):
    # global pc  # Add this line to modify the global pc value
    opcode = binary[-7::]
    
    # R-type instruction
    if opcode == "0110011":
        funct7 = binary[:7]
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        rd = binary[20:25]
        instruction = binary[:7]
        pc = pc + 4
        if funct3 == "000":
            if funct7 == "0000000":
                instruction = "ADD"
            elif funct7 == "0100000":
                instruction = "SUB"
        elif funct3 == "010":
            instruction = "SLT"
        elif funct3 == "011":
            instruction = "SLTU"
        elif funct3 == "100":
            instruction = "XOR"
        elif funct3 == "001":
            instruction = "SLL"
        elif funct3 == "101":
            instruction = "SRL"
        elif funct3 == "110":
            instruction = "OR"
        elif funct3 == "111":
            instruction = "AND"
        execute_r_type_instruction(instruction, rd, rs1, rs2, registers)
        x = (registers[int(rd, 2)])
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        y = rd
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        return ("0b" + format(x, '032b'))

    # I-type instruction
    if opcode == "0000011" or opcode == "0010011" or opcode == "1100111":
        imm = binary[:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "0000011":
            instruction = "LW"
        elif opcode == "0010011" and funct3 == "000":
            instruction = "ADDI"
        elif opcode == "0010011" and funct3 == "011":
            instruction = "SLTIU"
        elif opcode == "1100111":
            instruction = "JALR"
        execute_i_type_instruction(instruction, rd, rs1, imm, registers)
        x = (registers[int(rd, 2)])
        y = rd
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        final.append(("0b" + format(x, '032b')))
        return "0b" + format(x, '032b')

    # S-type instruction
    if opcode == "0100011":
        imm = binary[:7] + binary[20:25]
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        instruction = binary[:7]
        if funct3 == "010":
            instruction = "SW"
        execute_s_type_instruction(instruction, rs1, rs2, imm, registers)


    # B-type instruction
   if opcode == "1100011":
        imm = binary[-32]+binary[-8]+binary[-31:-25]+binary[-12:-8]+"0"
        rs2 = binary[7:12]
        rs1 = binary[12:17]
        funct3 = binary[17:20]
        instruction = binary[:7]
        if funct3 == "000":
            instruction = "BEQ"
        elif funct3 == "001":
            instruction = "BNE"
        elif funct3 == "100":
            instruction = "BLT"
        elif funct3 == "110":
            instruction = "BLTU"
        elif funct3 == "101":
            instruction = "BGE"
        elif funct3 == "111":
            instruction = "BGEU"
        execute_b_type_instruction(instruction, rs1, rs2, imm, registers)
        return

    # U-type instruction
    if opcode == "0110111" or opcode == "0010111":
        imm = binary[:20]
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "0110111":
            instruction = "LUI"
        elif opcode == "0010111":
            instruction = "AUIPC"
        execute_u_type_instruction(instruction, rd, imm, registers)
        x = (registers[int(rd, 2)])
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        return "0b" + format(x, '032b')

    # J-type instruction
    if opcode == "1101111":
        imm = binary[-32]+binary[-20:-12]+binary[-21]+binary[-31:-21]+"0"
        rd = binary[20:25]
        instruction = binary[:7]
        if opcode == "1101111":
            instruction = "JAL"
        execute_j_type_instruction(instruction, rd, imm, registers)
        x = (registers[int(rd, 2)])
        y = int(rd,2)
        reg_value[reg_dict[y]] = "0b" + format(x, '032b')
        final.append("0b" + format(x, '032b'))
        print("Result of", instruction, "operation:","0b"+format(x,'032b'))
        return "0b" + format(x, '032b')


# Read instructions from file
with open("input.txt", "r") as file:
    print("File Opened")
    for line in file:
        (execute_instruction(str(line.strip().strip("\n")),pc,registers))
        print("pc : ",pc)
        print(reg_value)   
        # print(answer)
        # final.append(answer)


# # Process instructions
with open("output.txt","w") as o:
    for i in final:
        o.write(i)
        o.write("\n")

