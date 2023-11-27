from collections import deque

class Grafo:
    def __init__(self, mapa_de_estados):
        self.mapa_de_estados = mapa_de_estados

    def get_vizinhos(self, v):
        return self.mapa_de_estados[v]

    def h(self, n):
        H = {
            'A': 6,
            'B': 5,
            'C': 4,
            'D': 5,
            'E': 5,
            'F': 3,
            'G': 4,
            'H': 3,
            'I': 2,
            'J': 2,
            'K': 1,
            'L': 0
        }

        return H[n]

    def a_star_algorithm(self, no_inicial, no_final):
        # lista_no_vizinhos_deconhecidos que já foram visitados, masa oa vizinhos ainda não foram visitados, começa no nó inicial
        # lista_no_vizinhos_conhecidos é uma lista de nós que já foram visitados e os vizinhos já foram inspecionados
        lista_no_vizinhos_deconhecidos = set([no_inicial])
        lista_no_vizinhos_conhecidos = set([])

        g = {}

        g[no_inicial] = 0

        pais = {}
        pais[no_inicial] = no_inicial

        while len(lista_no_vizinhos_deconhecidos) > 0:
            n = None
            for v in lista_no_vizinhos_deconhecidos:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v
                    print(n)

            if n == None:
                print('Path does not exist!')
                return None
            
            if n == no_final:
                caminho_final = []

                while pais[n] != n:
                    caminho_final.append(n)
                    n = pais[n]

                caminho_final.append(no_inicial)

                caminho_final.reverse()

                print('Caminho encontrado: {}'.format(caminho_final))
                return caminho_final

           
            for (m, peso) in self.get_vizinhos(n):
                if m not in lista_no_vizinhos_deconhecidos and m not in lista_no_vizinhos_conhecidos:
                    lista_no_vizinhos_deconhecidos.add(m)
                    pais[m] = n
                    g[m] = g[n] + peso

                    if g[m] > g[n] + peso:
                        g[m] = g[n] + peso
                        pais[m] = n

                        if m in lista_no_vizinhos_conhecidos:
                            lista_no_vizinhos_conhecidos.remove(m)
                            lista_no_vizinhos_deconhecidos.add(m)
            lista_no_vizinhos_deconhecidos.remove(n)
            lista_no_vizinhos_conhecidos.add(n)

        print('Caminho não existe!')
        return None
    
mapa_de_estados = {
    'A': [('B', 1), ('E', 1)],
    'B': [('C', 1), ('A', 1)],
    'C': [('D', 1), ('F', 1), ('B', 1)],
    'D': [('C', 1)],
    'E': [('G', 1), ('A', 1)],
    'F': [('I', 1),  ('C', 1)],
    'G': [('H', 1),  ('E', 1)],
    'H': [('I', 1), ('J', 1), ('G', 1)],
    'I': [('F', 1), ('K', 1), ('H', 1)],
    'J': [('K', 1), ('H', 1)],
    'K': [('I', 1), ('J', 1), ('L', 1)],
    'L': [('K', 1)]

}
graph1 = Grafo(mapa_de_estados)
graph1.a_star_algorithm('A', 'L')