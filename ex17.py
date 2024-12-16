while True:
    try:
        comando = input("Digite 'sair' para interromper: ")
        if comando.lower() == 'sair':
            break
    except KeyboardInterrupt:
        print("\nLoop interrompido pelo usuário.")
        break
