from lex import *

VN = ['Program','Block','ConstDecl','ConstAssigList','CAS','VarDecl','IdList','IL','ProcDecl','PD','Statement','StatementList','SL','Condition','Relation','Expression','E','SumOperator','Term','T','MultOperator','Factor']

VT = ['TOKENEOF', 'TOKENPROCEDURE','TOKENPARENTESISA','TOKENPARENTESISC','TOKENNUM','TOKENVAR','TOKENCONST','TOKENCALL','TOKENBEGIN','TOKENEND','TOKENIF','TOKENODD','TOKENTHEN','TOKENWHILE','TOKENPUNTOYCOMA','TOKENCOMA','TOKENPUNTO','TOKENESPACIO','TOKENSUMARESTA','TOKENMULTDIV','TOKENASIGN','TOKENOPERADORREL','TOKENID']

SD = {
    'Program': {'TOKENEOF':         ['Block','TOKENEOF'],
                'TOKENCONST':       ['Block','TOKENEOF'],
                'TOKENVAR ':        ['Block','TOKENEOF'],
                'TOKENBEGIN':       ['Block','TOKENEOF'],
                'TOKENCALL':        ['Block','TOKENEOF'],
                'TOKENIF':          ['Block','TOKENEOF'],
                'TOKENPROCEDURE,':  ['Block','TOKENEOF'],
                'TOKENWHILE':       ['Block','TOKENEOF'],
                'TOKENID':          ['Block','TOKENEOF'],
                'TOKENPARENTESISA': ['Block','TOKENEOF'],
                'TOKENNUM':         ['Block','TOKENEOF'],
                'TOKENPARENTESISC': ['Block','TOKENEOF'],
                'TOKENSUMARESTA':   ['Block','TOKENEOF'],
                'TOKENMULTDIV':     ['Block','TOKENEOF'] },
   'Block':    {'TOKENCONST':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENPUNTOYCOMA':  ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENEOF':         ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENVAR':         ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENBEGIN':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENCALL':        ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENIF':          ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENPROCEDURE':   ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENWHILE':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENID':          ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],},
   'ConstDecl':{'TOKENCONST':       ['TOKENCONST','ConstAssigList','TOKENPUNTOYCOMA']},
   'ConstAssigList': {'TOKENID':    ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS']},
   'CAS':      {'TOKENCOMA':        ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS'],
                'TOKENPUNTOYCOMA':  [],},
   'VarDecl':  {'TOKENVAR':         ['TOKENVAR', 'IdList'],
                'TOKENPROCEDURE':   [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  [],
                'TOKENBEGIN':       [],
                'TOKENCALL':        [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENID':          [],},
   'IdList':   {'TOKENID':          ['TOKENID', 'IL']},
   'IL':       {'TOKENCOMA' :       ['TOKENID', 'IL'],
                'TOKENPUNTOYCOMA':  [],},
   'ProcDecl': {'TOKENPROCEDURE':   ['TOKENPROCEDURE', 'TOKENID', 'TOKENPUNTOYCOMA', 'Block','TOKENPUNTOYCOMA', 'ProcDecl'],
                'TOKENID':          [],
                'TOKENCALL':        [],
                'TOKENBEGIN':       [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  [],},
   'PD':       {'TOKENPROCEDURE':   [],
                'TOKENID':          [],
                'TOKENCALL':        [],
                'TOKENBEGIN':       [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  [],},
   'Statement':{'TOKENID':          ['TOKENID','TOKENASIGN','Expression'],
                'TOKENCALL':        ['TOKENCALL', 'TOKENID'],
                'TOKENBEGIN':       ['TOKENBEGIN', 'StatementList', 'TOKENEND'],
                'TOKENIF':          ['TOKENIF', 'Condition', 'TOKENTHEN', 'Statement'],
                'TOKENWHILE':       ['TOKENWHILE', 'Condition', 'TOKENDO', 'Statement'],
                'TOKENEND':         [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  [],},
   'StatementList': 
               {'TOKENEND':         ['StatementList', 'SL''statement','statementlist2'],
                'TOKENID':          ['StatementList', 'SL''statement','statementlist2'],
                'TOKENCALL':        ['StatementList', 'SL''statement','statementlist2'],
                'TOKENBEGIN':       ['StatementList', 'SL''statement','statementlist2'],
                'TOKENIF':          ['StatementList', 'SL''statement','statementlist2'],
                'TOKENWHILE':       ['StatementList', 'SL''statement','statementlist2'],
                'TOKENPUNTOYCOMA':  ['StatementList', 'SL''statement','statementlist2'],},
   'SL':       {'TOKENPUNTOYCOMA':  ['TOKENPUNTOYCOMA','StatementList', 'SL''statement','statementlist2'],
                'TOKENEND':         [],},
   'Condition':{'TOKENSUMARESTA':   ['Expression','Relation', 'Expression'],
                'TOKENPARENTESISA': ['Expression','Relation', 'Expression'],
                'TOKENID':          ['Expression','Relation', 'Expression'],
                'TOKENNUM':         ['Expression','Relation', 'Expression'],
                'TOKENODD':['TOKENODD','Expression',],}, ''
   'Relation': {'TOKENOPERADORREL':['TOKENOPERADORREL']},
   'Expression': {'TOKENSUMARESTA':[],'TOKENPARENTESISA':[],'TOKENID':[],'TOKENNUM':[],},
   'E': {'TOKENSUMARESTA':[],'TOKENOPERADORREL':[],'TOKENDO':[],'TOKENTHEN':[],'TOKENPARENTESISC':[],'TOKENEND':[],'TOKENEOF':[],'TOKENPUNTOYCOMA':[],},
   'SumOperator': {'TOKENSUMARESTA':[]},
   'Term': {'TOKENPARENTESISA':[],'TOKENID':[],'TOKENNUM':[]},
   'T': {'TOKENMULTDIV':['MultOperator','Factor','T'],'TOKENSUMARESTA':[],'TOKENEOF':[],'TOKENOPERADORREL':[],'TOKENPARENTESISC':[],'TOKENEND':[],'TOKENPUNTOYCOMA':[],'TOKENTHEN':[],'TOKENDO':[]},
   'MultOperator': {'TOKENMULTDIV':['TOKENMULTDIV']},
   'Factor': {'TOKENPARENTESISA':['TOKENPARENTESISA','Expression','TOKENPARENTESISC'],'TOKENID':['TOKENID'],'TOKENNUM':['TOKENNUM']},
}


def parser(codigo_fuente):
    datos_parser = {
     'lista_tokens': codigo_fuente,
     'index': 0,
     'error': False
     }
    datos_parser['lista_tokens'] = codigo_fuente
    def pni(no_terminal):
              caracter_actual = datos_parser['lista_tokens'][datos_parser['index']][0]
              if caracter_actual in SD[no_terminal].keys():
                    procesar(SD[no_terminal][caracter_actual])            
              else:       
                    datos_parser['error'] = True
                    print('La cadena no pertenece al lenguaje')
    
    def procesar(cuerpo_produccion):
        for caracter in cuerpo_produccion:
            caracter_actual = datos_parser['lista_tokens'][datos_parser['index']][0]
            datos_parser['error'] = False
            if caracter in VT:
                if caracter == caracter_actual:
                    datos_parser['index'] += 1
                else:
                    datos_parser['error'] = True
                    break
            elif caracter in VN:
                pni(caracter)
                if datos_parser['error']:
                    break
    
    def principal():
          pni('Program')
          caracter_actual = datos_parser['lista_tokens'][datos_parser['index']][0]
          if caracter_actual == '#' and (datos_parser['error']):
               print('La cadena no pertenece al lenguaje')
               return False
          else:
               print ('La cadena pertenece al lenguaje')
               return True
    return principal()

print(lexer('var x, aux;\n\nprocedure cuadrado;\nbegin\n\t aux:=x*x\nend;\n\nbegin\n\t x:= 1;\nwhile x <= 10 do\nbegin\n\tcall cuadrado;\nx := x + 1\nend\nend'))
