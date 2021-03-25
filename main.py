import api


def main():
    api.clear()
    api.banner()
    print("""
1) IP
2) IP 2
3) CEP
4) CEP 2
5) CNPJ
6) Banco
7) COVID-19
8) Whois
11) Placa de veículos
12) DDD
S) Sair
    """)
    main_input = input("Escolha uma opção: ")
    if main_input in "1":
        api.clear()
        api.ip()

    elif main_input in "2":
        api.clear()
        api.ip2()

    elif main_input in "3":
        api.clear()
        api.cep()

    elif main_input in "4":
        api.clear()
        api.cep2()

    elif main_input in "5":
        api.clear()
        api.cnpj()

    elif main_input in "6":
        api.clear()
        api.banks()

    elif main_input in "7":
        api.clear()
        api.covid19()

    elif main_input in "8":
        api.clear()
        api.whois()


    elif main_input in "11":
        api.clear()
        api.placa()

    elif main_input in "12":
        api.clear()
        api.ddd()

    elif main_input in "Ss":
        api.clear()

    else:
        api.clear()
        print("Opção invalida.")


if __name__ == '__main__':
    main()
