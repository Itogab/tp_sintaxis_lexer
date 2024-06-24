ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"
def automata_var(lexema):
    estado=0
    estados_finales = [3]
    delta= {0:{'v':1},1:{'a':2},2:{'r':3},3:{}}
    
    for caracter in lexema:
        if caracter in delta[estado].keys():
            estado=delta[estado][caracter]
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL
    