import ply.ply.lex as lex 
import re
import codecs
import os
import sys
import math

directorioTests = os.getcwd() + '/tests/'
archivoCompilado = os.getcwd() + '/archivosSD/programa.asm'
contadorBinario = 0
erroresEncontrados = 0
direccionMaximaMemoria = 15;
posicionUltimoError = 0;


#Tokens a detectar
tokens = [
    'ID', 'NUMBER','PCOMA', 'COMMENT', 'POSITION'
]



#Intrucciones permitidas en el programa
instrucciones = [
    # CONTROL
    'NA',  
    'STOP',

    # DATOS
    'CORA',
    'CORB',
    'CORC', 
    'CODIR', 
    'COALU',

    # REGISTROS
    'CACRA',
    'CACRB', 
    'CACRC',
    'CACDIR', 
    'CACALU',

    'CRARB',
    'CRARC',
    'CRADIR',
    'CRAALU',

    'CRBRA',
    'CRBRC',
    'CRBDIR',
    'CRBALU',

    'CRCRA',
    'CRCRB',
    'CRCDIR',
    'CRCALU',

    # ENTRADAS
    'CIRA',
    'CIRB',
    'CIRC', 
    'CIDIR', 
    'CIALU',

    'CI2RA',
    'CI2RB',
    'CI2RC', 
    'CI2DIR', 
    'CI2ALU', 

    # SALIDAS
    'COOUT',
    'CACOUT',
    'CRAOUT',
    'CRBOUT',
    'CRCOUT',

    'COOUT2',
    'CACOUT2',
    'CRAOUT2',
    'CRBOUT2',
    'CRCOUT2',
    'COOUT3',
    'CACOUT3',
    'CRAOUT3',
    'CRBOUT3',
    'CRCOUT3',

    'CODOUT',
    'CACDOUT',
    'CRADOUT',
    'CRBDOUT',
    'CRCDOUT',

    # ALU
    'AALUO', 
    'AALUA',
    'AALUB',
    'AALUC',

    'NALUO', 
    'NALUA',
    'NALUB',
    'NALUC',

    #SALTOS
    'JIO', 
    'JIRA',
    'JIRB',
    'JIRC',

    'JCCO',
    'JCCRA',
    'JCCRB',
    'JCCRC',

    'JCZO',
    'JCZRA',
    'JCZRB',
    'JCZRC'
]

cantidadInstrucciones = len(instrucciones) #cantidad de instrucciones



t_ignore = ' \t'
t_PCOMA = r';'
t_COMMENT = r'\#.*'





def t_newline(t):
    r'\n'



def t_ID(t):
    r'[a-zA-Z_][\w_]*'

    valorEncontrado = False
    calcularPosicion()

    global posicionUltimoError

    for i in range(cantidadInstrucciones):
        if t.value == instrucciones[i]:
            file.write(convertirABinario(i))
            return t
        
    if valorEncontrado == False:
        print("\n\n-------------------- Intrucción '%s' invalida  --------------------\n\n" %t.value)
        posicionUltimoError = contadorBinario
 
    global erroresEncontrados
    erroresEncontrados += 1
    return t


def t_NUMBER(t):
    r' \d+'
    t.value = int(t.value)

    valorBinario = convertirABinario(t.value)
    file.write(valorBinario)
    #file.write("\n") # Insertar salto de linea al final

    return t




def calcularPosicion():
    resultado = []
    cadenaBinaria = ""
    global contadorBinario
    contadorBinario += 1
    n = contadorBinario - 1

    for i in range(direccionMaximaMemoria):
        resultado.append(n & 1)
        n >>= 1
    
    for i in range((direccionMaximaMemoria-1),-1,-1):
        cadenaBinaria += str(resultado[i])
    
    file.write(cadenaBinaria)





def convertirABinario(numero):
    binario = ""
    binarioFinal = ""
    
    if (numero >= 0 and numero <= 255):
        while(numero > 0):
            if (numero%2 == 0):
                binario = "0" + binario
            else:
                binario = "1" + binario

            numero = int(math.floor(numero/2))
        
        for i in range(8 - len(binario)):
            binarioFinal += "0"
    else:
        binario = "00000000"
        global posicionUltimoError
        global erroresEncontrados

        posicionUltimoError = contadorBinario
        erroresEncontrados += 1

    binarioFinal += binario
    return binarioFinal




def t_POSITION(t):
    r'\>\d+'
    
    posicion = t.value[1:]
    posFinal = int(posicion)
    print("Salto a la posición:", posFinal)
    
    global contadorBinario
    contadorBinario = posFinal

    return t




def t_error(t):
    print(" Caracter ilegal '%s'" %t.value[0])
    t.lexer.skip(1)








def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont+1
 
    while respuesta == False:
        numArchivo = input('\nNumero de test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

    return files[int(numArchivo)-1]


archivo = buscarFicheros(directorioTests)
test = directorioTests + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

file = open(archivoCompilado, "w")


analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()

    if not tok : 
       file.close() 
       espacioLibre = int((100*contadorBinario) / 32768)
       print("\n\nSe ocuparon ",contadorBinario," bytes (",espacioLibre,"%) de un total de 32.768")
       print("Se encontraron '%s' instrucciones erroneas" %erroresEncontrados) 
       print("Ultimo error en la posicion: " + str(posicionUltimoError) + "\n\n")
       break

    print(tok)



