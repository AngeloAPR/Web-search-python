from googlesearch import search
import webbrowser

def pesquisar_online(termo_pesquisa):
    resultados = list(search(termo_pesquisa, num_results=5))

    paginas = []
    for i, link in enumerate(resultados, start=1):
        print(f"{i}. {link}")
        paginas.append({'link': link})

    return paginas

def exibir_resultados(resultados):
    print("--- Resultados da pesquisa ---")
    for resultado in resultados:
        print("Link:", resultado['link'])

def main():
    termo_pesquisa = input("Digite o termo de pesquisa: ")
    resultados = pesquisar_online(termo_pesquisa)
    exibir_resultados(resultados)

if __name__ == "__main__":
    main()
