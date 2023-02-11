from requests import get

headers = {
    'Authorization': "Bearer live_a333f9dab0fdeadd75a98e6c0f955c",
}
brasileirao = 10
copadobrasil = 2
url = 'https://api.api-futebol.com.br/v1/'


def tabela_br():
    endpoint = f'campeonatos/{brasileirao}/tabela'
    data = get(url + endpoint, headers=headers).json()
    print()
    print(f'{"BRASILEIRÃO":^48}')
    print(f" {'PO':^4}  {'TIME':^15} {'PT':^4} {'JG':^4} {'VT':^4} {'EM':^4} {'DE':^4}")
    for i in range(20):
        if i >= 0 and i < 9:
            pos = '0' + str(data[i]['posicao'])
        else:
            pos = data[i]['posicao']  
             
        time = data[i]['time']['nome_popular']
        
        if data[i]['pontos'] >= 0 and data[i]['pontos'] <= 9:
            pontos = '0' + str(data[i]['pontos'])
        else:
            pontos = data[i]['pontos']
            
        if data[i]['jogos'] >= 0 and data[i]['jogos'] <= 9:
            jogos = '0' + str(data[i]['jogos'])
        else:
            jogos = data[i]['jogos']
            
        if data[i]['vitorias'] >= 0 and data[i]['vitorias'] <= 9:
            vitorias = '0' + str(data[i]['vitorias'])
        else:
            vitorias = data[i]['vitorias']
            
        if data[i]['empates'] >= 0 and data[i]['empates'] <= 9:
            empates = '0' + str(data[i]['empates'])
        else:
            empates = data[i]['empates']
            
        if data[i]['derrotas'] >= 0 and data[i]['derrotas'] <= 9:
            derrotas = '0' + str(data[i]['derrotas'])
        else:
            derrotas = data[i]['derrotas']
        
        print(f'|{pos:^4}| {time:<15}|{pontos:^4}|{jogos:^4}|{vitorias:^4}|{empates:^4}|{derrotas:^4}|')   
    print()

def tabela_cdb():
    # SÓ FUNCIONA A PARTIR DAS OITAVAS DE FINAL!
    endpoint = f'campeonatos/{copadobrasil}'
    data = get(url + endpoint, headers=headers).json()
    fase_id = data['fase_atual']['fase_id']
    
    endpoint = f'campeonatos/{copadobrasil}/fases/{fase_id}'
    data = get(url + endpoint, headers=headers).json()
    fase = data['campeonato']['fase_atual']['nome']

    print(f'{"COPA DO BRASIL":^30}')
    print(fase)

    for i in range (0, len(data['chaves'])):
        print(f'Jogo {i+1}')
        print('Ida  :', data['chaves'][i]['partida_ida']['placar'])
        print('Volta:', data['chaves'][i]['partida_volta']['placar'])
        print()

tabela_br()
tabela_cdb()
