def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    joao = []
    maria = []


    for figurinha_maria in figurinhas_da_maria:
        if (figurinhas_da_maria in figurinhas_do_joao):
            continue
        if (figurinha_maria in maria or figurinha_maria in joao):
            continue
        for figurinha_joao in figurinhas_do_joao:
            if (figurinha_joao in figurinha_maria):
                continue
            if (figurinha_joao in joao or figurinha_joao in maria):
                continue
            maria.append(figurinha_maria)
            joao.append(figurinha_joao)
            break
        return len(maria)

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
