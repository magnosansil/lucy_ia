import speech_recognition as sr
import json

def abrir_programa(programa):
    return f"Abrindo {programa} \n"

def fechar_programa(programa):
    return f"Fechando {programa}\n"

def pesquisar_sistema(programa):
    return f"Pesquisando no sistema: {programa}\n"

def pesquisar_google(tema):
    return f"Pesquisando no Google sobre: {tema}\n"

def desligar_lucy():
    return "Lucy está desligando. Até a próxima!\n"

def processar_comando(comando, config):
    resultado = f"Você falou: {comando.decode('latin-1')}\n" 

    comando = comando.decode('latin-1').lower()  


    # Remover "lucy" do comando
    comando = comando.replace("lucy", "").strip()

    if comando.startswith("pesquisar no google"):
        tema = comando.replace("pesquisar no google", "").strip()
        resultado += pesquisar_google(tema)
        return resultado
    elif comando.startswith("desligar"):
        resultado += desligar_lucy()
        print(resultado)  # Exibir a mensagem de desligamento
        exit()  # Encerrar o programa
    else:
        for acao in config["acoes"]:
            if acao["nome"] in comando:
                for objeto in acao["objetos"]:
                    if objeto in comando:
                        if acao["nome"] == "abrir":
                            resultado += abrir_programa(objeto)
                        elif acao["nome"] == "fechar":
                            resultado += fechar_programa(objeto)
                        elif acao["nome"] == "pesquisar no sistema":
                            resultado += pesquisar_sistema(objeto)
                        return resultado

    return resultado + "Desculpe, mas não reconheço este comando, tente outro\n"

def main():
    # Carregando configurações do arquivo JSON
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Inicializando o reconhecedor de fala
    r = sr.Recognizer()

    # Mensagem de apresentação
    print("Olá, eu sou a Lucy, sua assistente virtual. Em que posso ajudar?\n")

    while True:
        with sr.Microphone() as source:
            print("Diga um comando:\n")
            audio = r.listen(source, timeout=8)

        try:
            comando = r.recognize_google(audio, language="pt-BR").capitalize()
            print(processar_comando(comando, config))
        except sr.UnknownValueError:
            print("Nenhum comando detectado após 8 segundos.\n")
        except sr.RequestError:
            print("Erro na solicitação. Verifique sua conexão com a Internet.\n")

if __name__ == "__main__":
    main()