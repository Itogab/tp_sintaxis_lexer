from lex import *

VN = ['Program','Block','ConstDecl','ConstAssigList','CAS','VarDecl','IdList','IL','ProcDecl','PD','Statement','StatementList','SL','Condition','Relation','Expression','E','SumOperator','Term','T','MultOperator','Factor']

VT = ['TOKENNUMERAL','TOKENEOF', 'TOKENPROCEDURE','TOKENPARENTESISA','TOKENPARENTESISC','TOKENNUM','TOKENVAR','TOKENCONST','TOKENCALL','TOKENBEGIN','TOKENEND','TOKENIF','TOKENODD','TOKENTHEN','TOKENWHILE','TOKENPUNTOYCOMA','TOKENCOMA','TOKENPUNTO','TOKENESPACIO','TOKENSUMARESTA','TOKENMULTDIV','TOKENASIGN','TOKENOPERADORREL','TOKENID']


SD = {
    'Program': {'TOKENNUMERAL':     ['Block','TOKENNUMERAL'],
                'TOKENCONST':       ['Block','TOKENNUMERAL'],
                'TOKENVAR':         ['Block','TOKENNUMERAL'],
                'TOKENBEGIN':       ['Block','TOKENNUMERAL'],
                'TOKENCALL':        ['Block','TOKENNUMERAL'],
                'TOKENIF':          ['Block','TOKENNUMERAL'],
                'TOKENPROCEDURE':   ['Block','TOKENNUMERAL'],
                'TOKENWHILE':       ['Block','TOKENNUMERAL'],
                'TOKENID':          ['Block','TOKENNUMERAL'],
                'TOKENPARENTESISA': ['Block','TOKENNUMERAL'],
                'TOKENNUM':         ['Block','TOKENNUMERAL'],
                'TOKENPARENTESISC': ['Block','TOKENNUMERAL'],
                'TOKENSUMARESTA':   ['Block','TOKENNUMERAL'],
                'TOKENMULTDIV':     ['Block','TOKENNUMERAL'] },
   'Block':    {'TOKENCONST':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENPUNTOYCOMA':  ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENNUMERAL':     ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENVAR':         ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENBEGIN':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENCALL':        ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENIF':          ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENPROCEDURE':   ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENWHILE':       ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
                'TOKENID':          ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],},
   'ConstDecl':{'TOKENCONST':       ['TOKENCONST','ConstAssigList','TOKENPUNTOYCOMA'],'TOKENVAR':[],'TOKENPUNTOYCOMA':[],'TOKENNUMERAL':[],'TOKENBEGIN':[],'TOKENCALL':[],'TOKENIF':[],'TOKENPROCEDURE':[],'TOKENWHILE':[],'TOKENID':[]},
   'ConstAssigList': {'TOKENID':    ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS']},
   'CAS':      {'TOKENCOMA':        ['TOKENID', 'TOKENOPERADORREL', 'TOKENNUM', 'CAS'],
                'TOKENPUNTOYCOMA':  []},
   'VarDecl':  {'TOKENVAR':         ['TOKENVAR', 'IdList','TOKENPUNTOYCOMA'],
                'TOKENPROCEDURE':   [],
                'TOKENNUMERAL':     [],
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
                'TOKENNUMERAL':     [],
                'TOKENPUNTOYCOMA':  []},
   'PD':       {'TOKENPROCEDURE':   [],
                'TOKENID':          [],
                'TOKENCALL':        [],
                'TOKENBEGIN':       [],
                'TOKENIF':          [],
                'TOKENWHILE':       [],
                'TOKENNUMERAL':     [],
                'TOKENPUNTOYCOMA':  []},
   'Statement':{'TOKENID':          ['TOKENID','TOKENASIGN','Expression'],
                'TOKENCALL':        ['TOKENCALL', 'TOKENID'],
                'TOKENBEGIN':       ['TOKENBEGIN', 'StatementList', 'TOKENEND'],
                'TOKENIF':          ['TOKENIF', 'Condition', 'TOKENTHEN', 'Statement'],
                'TOKENWHILE':       ['TOKENWHILE', 'Condition', 'TOKENDO', 'Statement'],
                'TOKENEND':         [],
                'TOKENNUMERAL':     [],
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
   'Expression': {'TOKENSUMARESTA':['SumOperator','Term','E'],
                  'TOKENPARENTESISA':['Term','E'],
                  'TOKENID':['Term','E'],
                  'TOKENNUM':['Term','E']},
   'E': {'TOKENSUMARESTA':['SumOperator','Term','E'],
         'TOKENOPERADORREL':[],
         'TOKENDO':[],
         'TOKENTHEN':[],
         'TOKENPARENTESISC':[],
         'TOKENEND':[],
         'TOKENNUMERAL':[],
         'TOKENPUNTOYCOMA':[]},
   'SumOperator': {'TOKENSUMARESTA':['TOKENSUMARESTA']},
   'Term': {'TOKENPARENTESISA':['Factor','T'],
            'TOKENID':['Factor','T'],
            'TOKENNUM':['Factor','T']},
   'T': {'TOKENMULTDIV':['MultOperator','Factor','T'],
         'TOKENSUMARESTA':[],
         'TOKENNUMERAL':[],
         'TOKENOPERADORREL':[],
         'TOKENPARENTESISC':[],
         'TOKENEND':[],
         'TOKENPUNTOYCOMA':[],
         'TOKENTHEN':[],
         'TOKENDO':[]},
   'MultOperator': {'TOKENMULTDIV':['TOKENMULTDIV']},
   'Factor': {'TOKENPARENTESISA':['TOKENPARENTESISA','Expression','TOKENPARENTESISC'],
              'TOKENID':['TOKENID'],
              'TOKENNUM':['TOKENNUM']},
}


def parser(codigo_fuente):
    pila = ['Eof','Program']
    error = False
    i = 0
    t = codigo_fuente[i][0]
    tope = pila[len(pila) - 1]
    
    def M(pt,ptope):
        return pt in SD[ptope]
    
    def poner(ppila,pproduccion):
        j = len(pproduccion) - 1
        while j >= 0:
            ppila.append(pproduccion[j])
            j -= 1

    def produccion(pt,ptope):
        return SD[ptope][pt]

    while ((t != 'Eof') or (tope != 'Eof')):
        if tope in VT:
            if tope == t:
                ubicacionTope = len(pila) - 1
                pila.pop(ubicacionTope) #UbiacionTope me permite borrar, en el caso de que hayan repetidos tokens, el ultimo de ellos
                i += 1
            else:
                error = True
                break
        else:
            if (M(t,tope)):
                ubicacionTope = len(pila) - 1
                pila.pop(ubicacionTope)
                poner(pila,produccion(t,tope))
            else:
                error = True
                break
        t = codigo_fuente[i][0]
        tope = pila[len(pila) - 1] 

    if error:
        print('La cadena no pertenece al lenguaje')
    else:
        print('La cadena pertenece al lenguaje')

#No pertenecen
print(parser(lexer('(2)#')))
print(parser(lexer('2>>>>1 holaa finsi#')))
print(parser(lexer('and if then elsehola+*+#')))
print(parser(lexer('====><<>num if termino integral#')))
print(parser(lexer('++++--*////***(end)(procedure)(var)#')))
print(parser(lexer('var abc procedure faltaPuntoYcoma; call a;#')))
print(parser(lexer('procedure x; begin x:=2; end;')))
#Pertenecen
print(parser(lexer('procedure x; begin x:=2; end;#')))
print(parser(lexer('procedure calcT; begin t := 4 * 3; if t > 5 then t := t - 1; end; begin t := t + 2; end#')))
print(parser(lexer('procedure pruebaProcedure; begin if x < 10 then x := x + 1; end; begin z := 3; end#')))
print(parser(lexer('var a,b,c; procedure prueba; call a; begin b := 3; c := 2 end#')))
print(parser(lexer('if numero < 20 then numero := numero + 1#')))