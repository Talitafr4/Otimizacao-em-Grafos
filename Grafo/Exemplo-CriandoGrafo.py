import Grafo
from Algoritmos import Combinacoes, Subconj

def ImprimeVizinhos(G, Tipo="*"):
	for u in range(1, N+1):
		print ("L[",u,"]{0} = ".format(Tipo), end=" ")
		for v in G.N(u, Tipo, Fechada=True):
			if isinstance(v, int):
				print (v, end=" ") 
			else:
				print (v.Viz, end=" ")
		print()

G = Grafo.GrafoListaAdj(orientado = False)
G.Ler(textoAuxilio=False)
G.Desenhar()


G = Grafo.GrafoListaAdj(orientado = False)
N = 5
G.DefinirN(N)
G.AdicionarAresta(1,2,'label="abc" color=blue')
G.AdicionarAresta(1,3,'label="def"')
G.AdicionarAresta(1,5,'label="ghi"')
G.AdicionarAresta(3,4,'color=red')
G.AdicionarAresta(4,5)
G.Desenhar("desenho1.png", reduzirTempo=False)
ImprimeVizinhos(G)
print

G = Grafo.GrafoListaAdj(orientado = True)
N = 5
G.DefinirN(N)
G.DefinirAtrV(1, 'label="Raiz" fillcolor=yellow shape=box')
G.DefinirAtrV(2, 'shape=doublecircle')
G.DefinirAtrV(4, 'shape=point')
G.AdicionarAresta(1,2)
G.AdicionarAresta(1,3)
G.AdicionarAresta(1,5)
G.AdicionarAresta(3,4)
G.AdicionarAresta(4,3)
G.AdicionarAresta(4,5)
G.AdicionarAresta(5,1)
G.Desenhar("desenho2.png", reduzirTempo=False)
ImprimeVizinhos(G, "+")
ImprimeVizinhos(G, "-")
print()



G = Grafo.GrafoMatrizAdj(orientado = False)
N = 5
G.DefinirN(N)
G.AdicionarAresta(1,2,'label="abc" color=blue')
G.AdicionarAresta(1,3,'label="def"')
G.AdicionarAresta(1,5,'label="ghi"')
G.AdicionarAresta(3,4,'color=red')
G.AdicionarAresta(4,5)
G.Desenhar("desenho3.png", reduzirTempo=False)
ImprimeVizinhos(G)
print()

G = Grafo.GrafoMatrizAdj(orientado = True)
N = 5
G.DefinirN(N)
G.AdicionarAresta(1,2)
G.AdicionarAresta(1,3)
G.AdicionarAresta(1,5)
G.AdicionarAresta(3,4)
G.AdicionarAresta(4,3)
G.AdicionarAresta(4,5)
G.AdicionarAresta(5,1)
G.Desenhar("desenho4.png", reduzirTempo=False)
ImprimeVizinhos(G, "+")
ImprimeVizinhos(G, "-")
print()

#listando todas as cliques
G = Grafo.GrafoMatrizAdj(orientado = False)
N = 5
G.DefinirN(N)
G.AdicionarAresta(1,2)
G.AdicionarAresta(1,3)
G.AdicionarAresta(2,3)
G.AdicionarAresta(1,4)
G.AdicionarAresta(3,5)
G.Desenhar("desenho5.png", reduzirTempo=False)

for S in Subconj(G.V()):
	clique = True
	for [u,v] in Combinacoes(S, 2):
		if not G.EhAresta(u,v):
			clique = False
			break
	if clique:
		print (S)


