ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"
def automata_num(lexema):
    estado = 0
    estados_finales = [1]
    delta= {0:{'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}
            ,1:{'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}}
    
    for caracter in lexema:
        if caracter in delta[estado].keys():
            estado=delta[estado][caracter]
        elif estado == 1 and caracter.isalpha(): 
            estado = ESTADO_TRAMPA
            break
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    if estado in estados_finales:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL