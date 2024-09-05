# Todos los imports
from Automatas.Call import *
from Automatas.Id import *
from Automatas.parentesisA import *
from Automatas.ParentesisC import *
from Automatas.Espacio_en_blanco import *
from Automatas.Numeral import *
from Automatas.Numeros import *
from Automatas.PuntoYComa import *
from Automatas.Coma import *
from Automatas.Operadorsumrest import*
from Automatas.operadormultydiv import*
from Automatas.OperadorRel import *
from Automatas.Punto import *
from Automatas.OperadorAsing import *
from Automatas.begin import *
from Automatas.do import *
from Automatas.end import *
from Automatas.If import *
from Automatas.odd import *
from Automatas.then import *
from Automatas.While import *
from Automatas.Var import * 
from Automatas.Const import *
#

ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA" 
TOKENS_POSIBLES = [('TOKENPARENTESISA',automata_parentesisA),('TOKENPARENTESISC',automata_parentesisC),('TOKENNUM',automata_num),('TOKENVAR',automata_var),('TOKENCONST',automata_const),('TOKENCALL',automata_call),('TOKENBEGIN',automata_begin),('TOKENEND',automata_end),('TOKENIF',automata_if),('TOKENODD',automata_odd),('TOKENTHEN',automata_then),('TOKENWHILE',automata_while),('TOKENPUNTOYCOMA',automata_puntoYcoma),('TOKENCOMA',automata_coma),('TOKENPUNTO',automata_punto),('TOKENID',automata_id),('TOKENESPACIO',espacio_en_blanco),('TOKENSUMARESTA',automata_sumrest),('TOKENMULTDIV',automata_multdiv),('TOKENASIGN',automata_asign),('TOKENPUNTO',automata_punto),('TOKENOPERADORREL',automata_relop),('TOKENNUMERAL',automata_numeral)]

def lexer(codigo_fuente):
    tokens = [] # listada de tokens que devolverá el lexer correspondiente al código fuente ingresado, se inicializa vacia
    posicion_actual = 0   # carácter actual en el código fuente que se esta procesando
    while posicion_actual < len(codigo_fuente):

        comienzo_lexema = posicion_actual # el siguiente lexema comienza en la última posición procesada
        posibles_tokens = [] # categorías de tokens posibles para el lexema actual
        posibles_tokens_con_un_caracter_mas = [] # categorías de tokens posibles para el lexema actual mas el próximo caracter
        lexema = "" # Se inicializa el siguiente lexema
        var_aux_todos_en_estado_trampa = False

        while not var_aux_todos_en_estado_trampa:
            var_aux_todos_en_estado_trampa = True
            topeDelLexema = lexema
            lexema = codigo_fuente[comienzo_lexema:posicion_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []
            
            if topeDelLexema != lexema:
                for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                    simulacion_afd = afd(lexema) # simula la ejecución de cada AFD para el lexema actual agregando un carácter
                    if simulacion_afd == ESTADO_FINAL:
                        posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                        var_aux_todos_en_estado_trampa = False
                    elif simulacion_afd == ESTADO_NO_FINAL:
                        var_aux_todos_en_estado_trampa = False
                posicion_actual = posicion_actual + 1
                 #Convierte la posición simulada en la actual, ya sea para continuar avanzando en 
                                                  # en el lexema actual, o convertir en la posición inicial del próximo
            lexema = codigo_fuente[comienzo_lexema:posicion_actual - 1]
        

        if len(posibles_tokens) == 0:
            raise Exception("ERROR:TOKEN DESCONOCIDO " + lexema)


        if posibles_tokens[0] != 'TOKENESPACIO':
            un_tipo_de_token = posibles_tokens[0] # Mientras haya posibilidad de avanzar, ya sea por estar en un estado final o no 
                                              # final el algoritmo avanza, con lo cual siempre devuelve el lexema más largo que 
                                              # coincide con un token; En caso de haber más de uno, devuelve el primero de la lista
                                              # según la precedencia elegida por el creador del lexer en TOKENS_POSIBLES
            token = (un_tipo_de_token, lexema)
            tokens.append(token)
            
        posicion_actual = comienzo_lexema + len(lexema)
    return tokens

print(lexer("var hola := 2 + 2a"))
