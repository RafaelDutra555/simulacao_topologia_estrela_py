import random
import time


def conexao():
    pc1 = msg()
    roteador = pc1
    return roteador


def msg():
    mensagem = ["oi", "olá", "hey", "supimpa?", "hi", "hello"]
    n_msg = random.randint(1, len(mensagem))
    msg = mensagem[n_msg - 1]
    return msg


def execucao():

    print("\n", "____" * 15, "\n")

    seta = "▶"
    pc2 = [random.randint(1, 8), conexao()]
    pc1 = random.randint(1, 8)
    while pc1 == pc2[0]:
        pc2 = [random.randint(1, 8), conexao()]

    print(
        "\33[105m{}\33[0m computador \33[32m{}\33[0m está conectado".format(seta, pc1))
    print("\33[105m{}\33[0m computador \33[32m{}\33[0m vai fazer conexão com o computador \33[32m{}\33[0m".format(
        seta, pc1, pc2[0]))

    time.sleep(0.6)

    print("\33[105m{}\33[0m O computador \33[32m{}\33[0m está recebendo uma mensagem do computador \33[32m{}\33[0m".format(
        seta,                                                                                                   pc2[0], pc1))
    print("\33[105m{}\33[0m O computador \33[32m{}\33[0m recebeu essa mensagem:".format(
        seta, pc2[0]), '\33[33m', pc2[1], '\33[0m')

    continuar = input("\nContinuar? [s/n] ")
    if continuar == 's' or continuar == 'S':
        execucao()
    elif continuar == 'n' or 'N':
        print("fechando o programa :)")
        time.sleep(0.4)
        exit()


execucao()
