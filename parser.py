from lex import *

VN = ['Program','Block','ConstDecl','ConstAssigList','CAS','VarDecl','IdList','IL','ProcDecl','PD','Statement','StatementList','SL','Condition','Relation','Expression','E','SumOperator','Term','T','MultOperator','Factor']

VT = ['TOKENEOF', 'TOKENPROCEDURE','TOKENPARENTESISA','TOKENPARENTESISC','TOKENNUM','TOKENVAR','TOKENCONST','TOKENCALL','TOKENBEGIN','TOKENEND','TOKENIF','TOKENODD','TOKENTHEN','TOKENWHILE','TOKENPUNTOYCOMA','TOKENCOMA','TOKENPUNTO','TOKENESPACIO','TOKENSUMARESTA','TOKENMULTDIV','TOKENASIGN','TOKENOPERADORREL','TOKENID']

SD = {
    'Program': {'TOKENEOF':         ['Block','TOKENEOF'],
                'TOKENCONST':       ['Block','TOKENEOF'],
                'TOKENVAR':         ['Block','TOKENEOF'],
                'TOKENBEGIN':       ['Block','TOKENEOF'],
                'TOKENCALL':        ['Block','TOKENEOF'],
                'TOKENIF':          ['Block','TOKENEOF'],
                'TOKENPROCEDURE':   ['Block','TOKENEOF'],
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
   'ConstDecl':{'TOKENCONST':       ['TOKENCONST','ConstAssigList','TOKENPUNTOYCOMA'],'TOKENVAR':[],'TOKENPUNTOYCOMA':[],'TOKENEOF':[],'TOKENBEGIN':[],'TOKENCALL':[],'TOKENIF':[],'TOKENPROCEDURE':[],'TOKENWHILE':[],'TOKENID':[]},
   'ConstAssigList': {'TOKENID':    ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS']},
   'CAS':      {'TOKENCOMA':        ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS'],
                'TOKENPUNTOYCOMA':  []},
   'VarDecl':  {'TOKENVAR':         ['TOKENVAR', 'IdList','TOKENPUNTOYCOMA'],
                'TOKENPROCEDURE':   [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  [],
                'TOKENBEGIN':       [],
                'TOKENCALL':        [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENID':          []},
   'IdList':   {'TOKENID':          ['TOKENID', 'IL']},
   'IL':       {'TOKENCOMA' :       ['TOKENCOMA','TOKENID', 'IL'],
                'TOKENPUNTOYCOMA':  []},
   'ProcDecl': {'TOKENPROCEDURE':   ['TOKENPROCEDURE', 'TOKENID', 'TOKENPUNTOYCOMA', 'Block','TOKENPUNTOYCOMA', 'ProcDecl'],
                'TOKENID':          [],
                'TOKENCALL':        [],
                'TOKENBEGIN':       [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  []},
   'PD':       {'TOKENPROCEDURE':   [],
                'TOKENID':          [],
                'TOKENCALL':        [],
                'TOKENBEGIN':       [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  []},
   'Statement':{'TOKENID':          ['TOKENID','TOKENASIGN','Expression'],
                'TOKENCALL':        ['TOKENCALL', 'TOKENID'],
                'TOKENBEGIN':       ['TOKENBEGIN', 'StatementList', 'TOKENEND'],
                'TOKENIF':          ['TOKENIF', 'Condition', 'TOKENTHEN', 'Statement'],
                'TOKENWHILE':       ['TOKENWHILE', 'Condition', 'TOKENDO', 'Statement'],
                'TOKENEND':         [],
                'TOKENEOF':         [],
                'TOKENPUNTOYCOMA':  []},
   'StatementList': 
               {'TOKENEND':         ['Statement', 'SL'],
                'TOKENID':          ['Statement', 'SL'],
                'TOKENCALL':        ['Statement', 'SL'],
                'TOKENBEGIN':       ['Statement', 'SL'],
                'TOKENIF':          ['Statement', 'SL'],
                'TOKENWHILE':       ['Statement', 'SL'],
                'TOKENPUNTOYCOMA':  ['Statement', 'SL']},
   'SL':       {'TOKENPUNTOYCOMA':  ['TOKENPUNTOYCOMA','Statement', 'SL'],
                'TOKENEND':         []},
   'Condition':{'TOKENSUMARESTA':   ['Expression','Relation', 'Expression'],
                'TOKENPARENTESISA': ['Expression','Relation', 'Expression'],
                'TOKENID':          ['Expression','Relation', 'Expression'],
                'TOKENNUM':         ['Expression','Relation', 'Expression'],
                'TOKENODD':['TOKENODD','Expression']},
   'Relation': {'TOKENOPERADORREL':['TOKENOPERADORREL']},
   'Expression': {'TOKENSUMARESTA':['SumOperator','Term','E'],'TOKENPARENTESISA':['Term','E'],'TOKENID':['Term','E'],'TOKENNUM':['Term','E']},
   'E': {'TOKENSUMARESTA':['SumOperator','Term','E'],'TOKENOPERADORREL':[],'TOKENDO':[],'TOKENTHEN':[],'TOKENPARENTESISC':[],'TOKENEND':[],'TOKENEOF':[],'TOKENPUNTOYCOMA':[]},
   'SumOperator': {'TOKENSUMARESTA':['TOKENSUMARESTA']},
   'Term': {'TOKENPARENTESISA':['Factor','T'],'TOKENID':['Factor','T'],'TOKENNUM':['Factor','T']},
   'T': {'TOKENMULTDIV':['MultOperator','Factor','T'],'TOKENSUMARESTA':[],'TOKENEOF':[],'TOKENOPERADORREL':[],'TOKENPARENTESISC':[],'TOKENEND':[],'TOKENPUNTOYCOMA':[],'TOKENTHEN':[],'TOKENDO':[]},
   'MultOperator': {'TOKENMULTDIV':['TOKENMULTDIV']},
   'Factor': {'TOKENPARENTESISA':['TOKENPARENTESISA','Expression','TOKENPARENTESISC'],'TOKENID':['TOKENID'],'TOKENNUM':['TOKENNUM']},
}


def parser(codigo_fuente):
    estado_parser = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
     
    def pni(no_terminal):
              caracter_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
              if caracter_actual in SD[no_terminal].keys():
                    procesar(SD[no_terminal][caracter_actual])            
              else:       
                    estado_parser['error'] = True
    def procesar(cuerpo_produccion):
        for caracter in cuerpo_produccion:
            caracter_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
            estado_parser['error'] = False
            if caracter in VT:
                if caracter == caracter_actual:
                    estado_parser['index'] += 1
                else:
                    estado_parser['error'] = True
                    break
            elif caracter in VN:
                pni(caracter)
                if estado_parser['error']:
                    break
    def principal():
          pni('Program')
          token_actual = estado_parser['lista_tokens'][estado_parser['index']][0]
          if token_actual == '#' and (estado_parser['error']): #or datos_parser['romper']:
               print('La cadena no pertenece al lenguaje')
               return False
          else:
               print ('La cadena pertenece al lenguaje')
               return True
        
    return principal()

print(parser(lexer('(2)')))
print(parser(lexer('x:=2')))
print(parser(lexer('2>>>>1 holaa finsi')))
print(parser(lexer('====><<>num if termino integral')))
print(parser(lexer('++++--*////***(end)(procedure)(var)')))
print(parser(lexer('begin call if while')))
print(parser(lexer('procedure x; begin x:=2; end;')))
print(parser(lexer('and if then elsehola+*+')))
print(parser(lexer('')))

print(lexer('var x, aux;\n\nprocedure cuadrado;\nbegin\n\t aux:=x*x\nend;\n\nbegin\n\t x:= 1;\nwhile x <= 10 do\nbegin\n\tcall cuadrado;\nx := x + 1\nend\nend'))
