def interpret(e,v):
 t,f,i,c,s="true","false",lambda i:interpret(e[i],v),lambda c:t if c else f,str
 return(v[e]if e in v else e)if type(e)==s else c(i(1)==f)if len(e)==2 else c(\
not i(0)==i(2)==f)if e[1]=="OR"else c(i(0)==i(2)==t)


print(interpret(["cat_asleep", "OR", ["NOT", "cat_gone"]],{"cat_gone" : "true", "cat_asleep" : "true"}))