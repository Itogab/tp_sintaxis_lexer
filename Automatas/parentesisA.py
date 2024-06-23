ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"

def automata_parentesisa(lexema):
    estado = 0
    estadofinal =[1]
    for caracter in lexema:
        if caracter == "(" and estado == 0:
            estado = 1
        else:
            estado = -1
            break
    if estado == -1 :
        return ESTADO_TRAMPA
    elif estado == 1:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL 
