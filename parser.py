from lex import *

VN = ['Program','Block','ConstDecl','ConstAssigList','CAS','VarDecl','IdList','IL','ProcDecl','PD','Statement','StatementList','SL','Condition','Relation','Expression','E','SumOperator','Term','T','MultOperator','Factor']

VT = ['TOKENEOF', 'TOKENPROCEDURE','TOKENPARENTESISA','TOKENPARENTESISC','TOKENNUM','TOKENVAR','TOKENCONST','TOKENCALL','TOKENBEGIN','TOKENEND','TOKENIF','TOKENODD','TOKENTHEN','TOKENWHILE','TOKENPUNTOYCOMA','TOKENCOMA','TOKENPUNTO','TOKENESPACIO','TOKENSUMARESTA','TOKENMULTDIV','TOKENASIGN','TOKENOPERADORREL','TOKENID']

P = {
   'Program': {'TOKENEOF': [], 'TOKENCONST': [] },
   'Block': {},
   'ConstDecl': {},
   'ConstAssigList': {},
   'CAS': {},
   'VarDecl': {},
   'IdList': {},
   'IL': {},
   'ProcDecl': {},
   'PD': {},
   'Statement': {},
   'StatementList': {},
   'SL': {},
   'Condition': {},
   'Relation': {},
   'Expression': {},
   'E': {},
   'SumOperator': {},
   'Term': {},
   'T': {},
   'MultOperator': {},
   'Factor': {},
}


def desc_rec_proc(codigo_fuente):
    estado_parser = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
    estado_parser['lista_tokens'] = codigo_fuente

    def pni(no_terminal):
        for cuerpo_produccion in P[no_terminal]:
            backtracking_index = estado_parser['index']
            procesar(cuerpo_produccion)
            if estado_parser['error']:
                estado_parser['index'] = backtracking_index                
            else:
                break
    
    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
            lexema_actual = estado_parser['lista_tokens'][estado_parser['index']][1]
            print(estado_parser['index'],'-->', caracter_actual,'-->',estado_parser['error'])
            estado_parser['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    estado_parser['index'] += 1                        
                else:
                    estado_parser['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if estado_parser['error']:
                    break
              
    def principal():
        pni('Program')
        caracter_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
        if caracter_actual != 'Eof' or estado_parser['error']:
            print('Caracter Actual:', caracter_actual, 'Error:', estado_parser['error'])
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()

print(desc_rec_proc(lexer('const := alfa;')))