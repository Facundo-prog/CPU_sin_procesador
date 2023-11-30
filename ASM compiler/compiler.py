import ply.ply.lex as lex 
import re
import codecs
import os
import sys
import math

pathDirectoryPrograms = os.getcwd() + '/ASM compiler/programs/'
endPathCompiledFile = os.getcwd() + '/ASM compiler/compiled/program.asm'

if os.name == "nt": 
  pathDirectoryPrograms = os.getcwd() + '\\ASM compiler\\programs\\'
  endPathCompiledFile = os.getcwd() + '\\ASM compiler\\compiled\\program.asm'

binaryCount = 0
errorCount = 0
maxAddressMemory = 16
positionLastError = 0
messageLastError = ""


tokens = [
  'ID', 'NUMBER','PCOMA', 'COMMENT', 'POSITION'
]

t_ignore = ' \r'
t_PCOMA = r';'
t_COMMENT = r'\#.*'




instructions = [
  # Control
  'NA',  
  'STOP',

  # Operator
  'CORA',
  'CORB',
  'CORC', 
  'CORD',
  'CODIR', 
  'COALU',

  # Registers
  'CACCRA',
  'CACCRB', 
  'CACCRC',
  'CACCRD',
  'CACCDIR', 
  'CACCALU',

  'CRARB',
  'CRARC',
  'CRARD',
  'CRADIR',
  'CRAALU',

  'CRBRA',
  'CRBRC',
  'CRBRD',
  'CRBDIR',
  'CRBALU',

  'CRCRA',
  'CRCRB',
  'CRCRD',
  'CRCDIR',
  'CRCALU',

  'CRDRA',
  'CRDRB',
  'CRDRC',
  'CRDDIR',
  'CRDALU',

  # Imputs
  'CI1RA',
  'CI1RB',
  'CI1RC', 
  'CI1RD',
  'CI1DIR', 
  'CI1ALU',

  'CI2RA',
  'CI2RB',
  'CI2RC',
  'CI2RD', 
  'CI2DIR', 
  'CI2ALU', 

  'CI3RA',
  'CI3RB',
  'CI3RC',
  'CI3RD', 
  'CI3DIR', 
  'CI3ALU', 

  # Outputs
  'COOUT1',
  'CRAOUT1',
  'CRBOUT1',
  'CRCOUT1',
  'CRDOUT1',
  'CACCOUT1',

  'COOUT2',
  'CRAOUT2',
  'CRBOUT2',
  'CRCOUT2',
  'CRDOUT2',
  'CACCOUT2',

  'COOUT3',
  'CRAOUT3',
  'CRBOUT3',
  'CRCOUT3',
  'CRDOUT3',
  'CACCOUT3',

  'CODOUT',
  'CRADOUT',
  'CRBDOUT',
  'CRCDOUT',
  'CRDDOUT',
  'CACCDOUT',

  # ALU
  'AALUO', 
  'AALURA',
  'AALURB',
  'AALURC',
  'AALURD',

  'NALUO', 
  'NALURA',
  'NALURB',
  'NALURC',
  'NALURD',

  # Jumps
  'JIO', 
  'JIRA',
  'JIRB',
  'JIRC',
  'JIRD',

  'JCCO',
  'JCCRA',
  'JCCRB',
  'JCCRC',
  'JCCRD',

  'JCZO',
  'JCZRA',
  'JCZRB',
  'JCZRC',
  'JCZRD'
]


def t_newline(t):
  r'\n'



def t_ID(t):
  r'[a-zA-Z_][\w_]*'

  foundValue = False
  calculatePosition()

  global positionLastError
  global messageLastError

  for i in range(len(instructions)):
    if t.value == instructions[i]:
      file.write(convertToBinary(i))
      return t
    
  if foundValue == False:
    print("\n\n-------------------- Invalid instruction '%s' --------------------\n\n" %t.value)
    messageLastError = "Invalid instruction " + t.value
    positionLastError = binaryCount

  global errorCount
  errorCount += 1

  return t


def t_NUMBER(t):
  r' \d+'
  t.value = int(t.value)

  binaryValue = convertToBinary(t.value)
  file.write(binaryValue)
  # file.write("\n") # Insertar salto de linea al final

  return t




def calculatePosition():
  result = []
  binaryChain = ""

  global binaryCount
  binaryCount += 1
  n = binaryCount - 1

  for i in range(maxAddressMemory):
    result.append(n & 1)
    n >>= 1
  
  for i in range((maxAddressMemory-1),-1,-1):
    binaryChain += str(result[i])
  
  file.write(binaryChain)





def convertToBinary(number):
  binary = ""
  endBinary = ""
  
  if (number >= 0 and number <= 255):
    while(number > 0):
      if (number%2 == 0):
        binary = "0" + binary
      else:
        binary = "1" + binary
      
      number = int(math.floor(number/2))
    
    for i in range(8 - len(binary)):
      endBinary += "0"

  else:
    binary = "00000000"
    global positionLastError
    global errorCount

    positionLastError = binaryCount
    errorCount += 1

  endBinary += binary
  return endBinary




def t_POSITION(t):
  r'\>\d+'
  
  position = t.value[1:]
  endPosition = int(position)
  print("\n")
  print("Jump to address:", endPosition, "\n")
  
  global binaryCount
  binaryCount = endPosition

  return t




def t_error(t):
  print("Illegal character '%s'" %t.value[0])
  print(t.value[0])
  t.lexer.skip(1)








def searchPrograms(directory):
  folders = []
  numberProgram = 0
  response = False
  countFiles = 1

  for base, dirs, files in os.walk(directory):
    folders.append(files)

  for file in files:
    print(str(countFiles) + ". " + file)
    countFiles += 1

  while response == False:
    numberProgram = input('\nNumber of program: ')
    numberProgram = int(numberProgram)

    if numberProgram <= 0 or numberProgram > files.__len__():
      print("Number of program invalid!")
      exit()

    for file in files:
      if file == files[int(numberProgram)-1]:
        response = True
        break

  print("Program \"%s\" selected\n" %files[int(numberProgram)-1])

  return files[int(numberProgram)-1]




numberProgram = searchPrograms(pathDirectoryPrograms)

prograFile = codecs.open(pathDirectoryPrograms + numberProgram, "r", "utf-8")
chainText = prograFile.read()
prograFile.close()

file = open(endPathCompiledFile, "w")


analyzer = lex.lex()
analyzer.input(chainText)

while True:
  token = analyzer.token()

  if not token : 
    file.close() 
    freeSpace = int((100 * binaryCount) / 32768)
    print("\n\n",binaryCount," bytes (",freeSpace, "%) were occupied out of a total of 32.768 bytes")
    print("'%s' invalid instructions" %errorCount)
    if errorCount > 0: print("Last error at position:",str(positionLastError), "->", messageLastError, "\n\n")
    break

  print(token)



