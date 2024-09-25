ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"
def automata_procedure(lexema):
    estado=0
    estados_finales = [9]
    delta= {0:{'p':1},1:{'r':2},2:{'o':3},3:{'c':4},4:{'e':5},5:{'d':6},6:{'u':7},7:{'r':8},8:{'e':9},9:{}}
    
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
    