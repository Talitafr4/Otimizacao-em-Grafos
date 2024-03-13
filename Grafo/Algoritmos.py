def SubconjRec(S, Esc, i):
	if i == len(Esc):
		yield tuple([S[j] for j in range(len(Esc)) if Esc[j]])
	else:
		for x in SubconjRec(S, Esc, i+1):
			yield x
		Esc[i] = True
		for x in SubconjRec(S, Esc, i+1):
			yield x
		Esc[i] = False
		
		
def Subconj(S):
	L = [x for x in S]
	for x in SubconjRec(L, [False]*len(L), 0):
		yield x
	

def ArranjosRec(S, k, Esc, Usado, i):
	if i == k:
		yield tuple([S[j] for j in Esc])
	else:
		for prox in [j for j in range(len(S)) if not Usado[j]]:
			Esc[i], Usado[prox] = prox, True
			for x in ArranjosRec(S, k, Esc, Usado, i+1):
				yield x
			Esc[i], Usado[prox] = None, False	
		
def Arranjos(S, k):
	L = [x for x in S]
	for x in ArranjosRec(L, k, [None]*k, [False]*len(L), 0):
		yield x

def CombinacoesRec(S, k, Esc, Usado, i):
	if i == k:
		yield tuple([S[j] for j in Esc])
	else:
		for prox in [j for j in range(0 if i==0 else Esc[i-1]+1, len(S)) if not Usado[j]]:
			Esc[i], Usado[prox] = prox, True
			for x in CombinacoesRec(S, k, Esc, Usado, i+1):
				yield x
			Esc[i], Usado[prox] = None, False	
		
def Combinacoes(S, k):
	L = [x for x in S]
	for x in CombinacoesRec(L, k, [None]*k, [False]*len(L), 0):
		yield x

def ProdCartesiano(S, R):
	R = [x for x in R]
	for x in S:
		for y in R:
			yield (x, y)

