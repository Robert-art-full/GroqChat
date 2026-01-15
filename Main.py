from genai_client import gerar_resposta

def main():
    print("🤖 Chat com Groq (Digite 'sair' para encerrar as perguntas)\n")

    while True:
        pergunta = input("Você: ")

        if pergunta.lower() == "sair":
            break

        try:
            resposta = gerar_resposta(pergunta)
            print(f"\nIA: {resposta}\n")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    main()
