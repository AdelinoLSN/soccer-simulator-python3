import time
from main import main

dados = []

x = 0
while x < 100:
    x += 1
    print()
    dados.append(main())

def analise():
    resultados = {}
    resultados['placares'] = {}

    for dado in dados:
        if (dado.team_a_score > dado.team_b_score):
            try:
                resultados[dado.team_a.name] += 1
            except:
                resultados[dado.team_a.name] = 1
        elif (dado.team_a_score < dado.team_b_score):
            try:
                resultados[dado.team_b.name] += 1
            except:
                resultados[dado.team_b.name] = 1
        else:
            try:
                resultados['empate'] += 1
            except:
                resultados['empate'] = 1

        try:
            resultados['placares'][str(dado.team_a_score)+'x'+str(dado.team_b_score)] += 1
        except:
            resultados['placares'][str(dado.team_a_score)+'x'+str(dado.team_b_score)] = 1

    placares = resultados.pop('placares')

    print()
    print (resultados)
    placares = (dict(sorted(placares.items(), key=lambda item: item[1], reverse=True)))
    for placar in placares:
        print (placar+" - "+str(placares[placar]))

analise()