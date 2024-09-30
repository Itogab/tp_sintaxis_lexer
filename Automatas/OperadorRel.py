ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_relop(lexema):
    estado = 0
    estados_finales = [1,2,3,4]
    delta = {
        0:{'<':1,'>':2,'=':3},
        1:{'=':3,'>':4},
        2:{'=':3},
        3:{},
        4:{}
    }
    
    for caracter in lexema:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = -1
            break
    
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


