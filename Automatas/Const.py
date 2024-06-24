ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"
def automata_const(lexema):
    estado=0
    estados_finales = [5]
    delta= {0:{'c':1},1:{'o':2},2:{'n':3},3:{'s':4},4:{'t':5},5:{}}
    
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
    