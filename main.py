from lexico import Analisador_Lexico 			# Importo o analisador léxico

arquivo=open("code.txt","r") 					# Abro o arquivo txt com o código
programa = arquivo.read() 						# Leio todos os caracteres do arquivo

codigos, _ = Analisador_Lexico().Reconhecedor(programa)		#Rodo a função que faz a análise léxica, retorna 2 valores (vetor de codigos, vetor para debug)

for t in codigos:
	print (t)    
