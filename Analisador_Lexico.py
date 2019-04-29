import sys

class Token:

    def __init__(self, palavra, lex_cod, linha):
        self.palavra = palavra      # Palavra reconhecida (Token)
        self.lex_cod = lex_cod      # Código do Token
        self.linha = linha          # Linha

    def __str__(self):
        return str(self.palavra) + "\t" + str(self.lex_cod) + "\t" + str(self.linha)
        # Saida:     Token            Código                  Nº Linha


class Analisador_Lexico:
    def __init__(self):
        # PALAVRAS RESERVADAS
        self.palavras_reservadas = ["while", "void", "string", "return", "main", "literal" "integer", "int", "inicio", "if", "for", "float", "fim", "else", "double", "do", "cout" , "cin", "char" ]  # Callfuncao também?
        self.codigo_reservadas = [1,2,3,4,11,12,13,14,15,16,18,19,20,21,22,23,24,25,26]  # Codigos dos Tokens              


    def Reconhecedor(self, programa, i=0):
        num_linha = 1           # Linha atual de leitura
        token = ""              # Palavra (Token)
        tam = len(programa)     # Tamanho do programa
        i = 0                   # Contador de Caracter
        lex_cod = 0             # Código do Token
        resultado = []          # Lista de Tokens

        while i <= tam-1:       # Enquanto o caracter atual for menor que o total de caracter do arquivo...

            if programa[i].isdigit(): # Verifica se o caracter é digito (número)

                token += programa[i]                                              
                i+=1
                lex_cod = "5" #INTEIRO

                while i < tam-1:    # Continua verificando o próximo caracter

                    if programa[i].isdigit(): 
                        token += programa[i]     # Se número continua adicionando ao Token
                        i+=1
                    elif programa[i] == ".":     # Se houver um ponto, significa que é um float 
                        token += programa[i]     # Adiciona o ponto ao token
                        i+=1
                        lex_cod = "19" #FLOAT

                        while i < tam - 1:               # Verificar se há mais números após o ponto
                            if programa[i].isdigit():
                                token += programa[i]     # Enquanto ouver mais números, vai adicionando
                                i+=1
                            else:
                                break                    
                        break                            # Para o while se não for digito               
                    else:                                
                        break


            elif programa[i].isalpha():      # Se não for número, verifica se é uma letra...
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter

                while i < tam-1:             # Enquanto continuar sendo letra, número ou underline, continua adicionando caracter ao token
                    if programa[i].isalpha() or programa[i].isdigit() or programa[i] is "_":
                        token += programa[i]
                        i+=1
                    else:
                        break                # Se não for nenhum desses, para o while          

                if token in self.palavras_reservadas:           # Verfica se o token é uma das palavras reservadas da linguagem
                    pos = self.palavras_reservadas.index(token)      # Pega a posição do vetor dentro da lista de palavras reservadas
                    lex_cod = self.codigo_reservadas[pos]            # Retorna o código do token referente a posição da lista


            elif programa[i] == "+":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "37"                 # Código do Token Somador (+)

                if programa[i] == "+":       # Verifica se o proximo também é um +     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "36"             # Código do Token Incrementador (++)


            elif programa[i] == "-":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "37"                 # Código do Token Subtrator (-)

                if programa[i] == "-":       # Verifica se o proximo também é um +     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "36"             # Código do Token Descrementador (++)
                                                      

            elif programa[i] is "*":         # Se for um multiplicador
                token = programa[i]
                lex_cod = "44"                 # Código do token de multiplicação
                i+=1


            elif programa[i] is "/":         # Se for um divisor (/)
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "42"                 # Código do Token divisor (/)

                if programa[i] is "/":       # Verifica se existe a segunda '/'
                    i+=1
                    while i < tam-1:         # Ignora os caracters até a quebra de linha
                        if programa[i] is "\n":
                            i+=1
                            num_linha += 1   # Incrimenta o localizador da linha atual
                            break
                        i+=1
                    continue


            elif programa[i] == "<":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "35"                 # Código do Token comparador Menor (<)

                if programa[i] == "=":       # Verifica se o proximo é um =     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "33"             # Código do Token comparador menor ou igual (<=)     

                if programa[i] == "<":       # Verifica se o proximo é outro <     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "33"             # Código do Token << (count)      


            elif programa[i] == ">":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "30"                 # Código do Token comparador maior (>)

                if programa[i] == "=":       # Verifica se o proximo é um =     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "29"             # Código do Token comparador maior ou igual (>=)     

                if programa[i] == ">":       # Verifica se o proximo é outro >     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "28"             # Código do Token >> (cin)             



            elif programa[i] == "=":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                lex_cod = "32"                 # Código do Token igual (=)

                if programa[i] == "=":       # Verifica se o proximo também é um =     
                    token += programa[i]     # Se for, adiciona ao token
                    i+=1                     # Avança para o proximo caracter
                    lex_cod = "31"             # Código do Token comparador igual (==)

            elif programa[i] == "!":
            
                token += programa[i]         # Se for, adiciona ao token
                i+=1                         # Avança para o proximo caracter
                if programa[i] == "=":    
                    i+=1
                    lex_cod = "31"              # Código do Token comparador diferente (!=)
                else:
                    i+=1
                    print("ERRO Léxico: Token '!' inesperado na linha: "+str(num_linha))    # Se não tiver != em sequência gera um erro


            elif programa[i] == "\n":        # Contagem de linhas
                num_linha += 1
                i+=1
                continue

            elif programa[i].isspace():      # Se o próximo caracter for espaço, ignora e continue para o próximo
                i+=1
                continue

            elif programa[i] is "{":          # Verifica se alguma chave foi aberta
                backup = i                    # Backup da posição atual para voltar depois                    
                while i < tam -1:
                    i+=1
                    if programa[i] is "}":    # Verifica se a chave aberta foi fechada
                        lex_cod = "39"          # Código do '{'
                        resultado.append(Token( programa[backup], lex_cod, num_linha))  # Se for aberto e fechado corretamente, adiciona o { no resultado

                        token = programa[i]   # Token '}'
                        lex_cod = "38"          # Código do '}'
                        i=backup+1
                        break
                else:
                        i=backup+1
                        print("ERRO Léxico: Chave aberta mas não fechada na linha: "+str(num_linha))
                        break
                continue

            elif programa[i] is "(":          # Verifica se algum parentese foi aberto
                backup = i                    # Backup da posição atual para voltar depois
                while i < tam -1:
                    i+=1
                    if programa[i] is ")":    # Verifica se o parentese foi efchado
                        lex_cod = "46"          # Código do '('
                        resultado.append(Token( programa[backup], lex_cod, num_linha))  # Se for aberto e fechado corretamente, adiciona o ( no resultado

                        token = programa[i]   # Token ')'
                        lex_cod = "45"          # Código do ')'
                        resultado.append(Token( token, lex_cod, num_linha))  # Se for aberto e fechado corretamente, adiciona o ) no resultado
                        i=backup+1
                        break
                else:
                        i=backup+1
                        print("ERRO Léxico: Chave aberta mas não fechada na linha: "+str(num_linha))
                        break
                continue    


            elif programa[i] is "/":     # Verificar se é início de comentário em bloco
                i+=1
                if programa[i] is "*":
                    ln = num_linha
                    while i < tam -1:
                        i+=1

                        if programa[i] is "*":   # Verificar se é fim de comentário
                            i+=1
                            if programa[i] is "/": # Confirma o '*/'
                                i+=1
                                break

                        elif programa[i] is "\n":
                            num_linha += 1       # Se quebrar linha, conta como linha nova e continua buscando fim do comentario
                    else:
                            print("ERRO Léxico: Comentário aberto e não fechado, inicio na linha: "+str(ln))  # Erro se não for fechado
                            i+=1
                            break
                    continue



            else:       # Caso seja algum caracter que não esteja definido na linguagem

                print("ERRO Léxico: Token '" + programa[i] + "' não é aceito. Erro na linha: " + str(num_linha))
                break
            

            resultado.append(Token(token, lex_cod, num_linha))  # Adiciona resultado na lista (vetor resultado)
            token = ""                                          # Reseta o token para continuar a leitura

        return resultado   # Retorna o vetor contendo (Token, Código, Linha)


        # FUNÇÃO MAIN

if __name__ == "__main__": # Só executa se for chamado direto no prompt como principal
    with open(sys.argv[1],"r") as programa:         # Recebe o arquivo do primeiro argumento e lê ele. Ex.: "CMD:> Analisador_Lexico.py meu_programa.txt"
        for tk in Analisador_Lexico().Reconhecedor(programa.read()):
            print (tk)
