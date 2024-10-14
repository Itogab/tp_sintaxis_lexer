from lex import *

VN = ['Program','Block','ConstDecl','ConstAssigList','CAS','VarDecl','IdList','IL','ProcDecl','PD','Statement','StatementList','SL','Condition','Relation','Expression','E','SumOperator','Term','T','MultOperator','Factor']

VT = ['TOKENPROCEDURE','TOKENPARENTESISA','TOKENPARENTESISC','TOKENNUM','TOKENVAR','TOKENCONST','TOKENCALL','TOKENBEGIN','TOKENEND','TOKENIF','TOKENODD','TOKENTHEN','TOKENWHILE','TOKENPUNTOYCOMA','TOKENCOMA','TOKENPUNTO','TOKENESPACIO','TOKENSUMARESTA','TOKENMULTDIV','TOKENASIGN','TOKENPUNTO','TOKENOPERADORREL','TOKENID']

P = {'Program':[['Block','TOKENEOF']],
     'Block':[['ConstDecl','VarDecl','ProcDecl','Statement'],['ConstDecl'],['VarDecl'],['ProcDecl'],['Statement'],['ConstDecl','VarDecl'],['ConstDecl','ProcDecl'],['ConstDecl','Statement'],['VarDecl','ProcDecl'],['VarDecl','Statement'],['ProcDecl','Statement'],['ConstDecl','VarDecl','ProcDecl'],['ConstDecl','VarDecl','Statement'],['VarDecl','ProcDecl','Statement'],['ConstDecl','ProcDecl','Statement']],
     'ConstDecl':[['TOKENCONST','ConstAssigList','TOKENPUNTOYCOMA']],
     'CAS':[['TOKENCOMA','TOKENID','TOKENOPERADORREL','CAS'],['TOKENCOMA','TOKENID','TOKENOPERADORREL']],
     'VarDecl':[['TOKENVAR','IdList']],
     'IdList':[['TOKENID','IL'],['TOKENID']],
     'IL':[['TOKENCOMA','TOKENID','IL'],['TOKENCOMA','TOKENID']],
     'ProcDecl':[['PD']],
     'PD':[['TOKENPROCEDURE','TOKENID','TOKENPUNTOYCOMA','Block','TOKENPUNTOYCOMA','PD'],['TOKENPROCEDURE','TOKENID','TOKENPUNTOYCOMA','TOKENPUNTOYCOMA','PD'],['TOKENPROCEDURE','TOKENID','TOKENPUNTOYCOMA','Block','TOKENPUNTOYCOMA'],['TOKENPROCEDURE','TOKENID','TOKENPUNTOYCOMA','TOKENPUNTOYCOMA']],
     'Statement':[['TOKENID','TOKENASIGN','Expression'],['TOKENCALL','TOKENID'],['TOKENBEGIN','StatementList','TOKENEND'],['TOKENBEGIN','TOKENEND'],['TOKENIF','Condition','TOKENTHEN','Statement'],['TOKENIF','Condition','TOKENTHEN'],['TOKENWHILE','Condition','TOKENDO','Statement'],['TOKENWHILE','Condition','TOKENDO']],
     'StatementList':[['Statement','SL'],['Statement'],['SL']],
     'SL':[['TOKENPUNTOYCOMA','Statement','SL'],['TOKENPUNTOYCOMA','Statement'],['TOKENPUNTOYCOMA','SL']],
     'Condition':[['Expression','Relation','Expression'],['TOKENODD','Expression']],
     'Relation':[['TOKENOPERADORREL']],
     'Expression':[['SumOperator','Term','E'],['SumOperator','Term'],['Term','E'],['Term']],
     'E':[['SumOperator','Term','E'],['SumOperator','Term']],
     'SumOperator':[['TOKENSUMARESTA']],
     'Term':[['Factor','T'],['Factor']],
     'T':[['MultOperator','Factor','T'],['MultOperator','Factor']],
     'MultOperator':[['TOKENMULTDIV']],
     'Factor':[['TOKENPARENTESISA','Expression','TOKENPARENTESISC'],['TOKENID'],['TOKENNUM']],
    'S':[['Token(','S','Token)','S'],['Token(','Token)','S'],['Token(','S','Token)'],['Token(','Token)']]
}


def desc_rec_proc(codigo_fuente):
    estado_parser = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
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
            #lexema_actual = estado_parser['lista_tokens'][estado_parser['index']][1]
            #print(estado_parser['index'],'-->', caracter_actual,'-->',estado_parser['error'])
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
        pni('S')
        caracter_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
        if caracter_actual != 'Eof' or estado_parser['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()

print(desc_rec_proc(lexer('(())())')))