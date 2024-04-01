from Grafo import GrafoListaAdj

G = GrafoListaAdj()
n = input(int())
G.DefinirN(n)
while(True):
    a, b = input().split(" ")
    if((a=="") or (b=="")):
        break
    a = int(a)
    b = int(b)
    if((a<=n) and (b<=n) and (a>0) and (b>0)):
        G.AdicionarAresta(a,b)
for (u,v) in G.E():
    print((u,v))
