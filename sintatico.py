class Pilha:
	def __init__(self):
		self.dados = []
 
	def empilha(self, elemento):
		self.dados.append(elemento)
 
	def desempilha(self):
		if not self.vazia():
			return self.dados.pop(0)
 
	def vazia(self):
		return len(self.dados) == 0

	def topo(self): 
		return self.dados[0]

	def mostrar(self):
		print(self.dados)	

class Analisador_Sintatico:

	def __init__(self):
		self.regras = [
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],# Regra 0
		[2,11,39,52,53,54,38,0,0,0,0,0,0,0,0,0], # Regra 1
		[7,55,41,56,41,57,0,0,0,0,0,0,0,0,0,0], # Regra 2
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 3
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 4
		[43,7,55,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 5
		[13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 6
		[19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 7
		[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 8
		[26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 9
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 10
		[59,41,56,41,57,0,0,0,0,0,0,0,0,0,0,0], # Regra 11
		[7,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 12
		[60,7,61,39,52,53,54,4,46,62,45,38,53,0,0,0], # Regra 13
		[13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 14
		[2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 15
		[26,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 16
		[19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 17
		[3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 18
		[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 20
		[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 21
		[9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 22
		[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 23
		[10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 24
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 25
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 26
		[46,63,45,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 27
		[56,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 28
		[56,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 29
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 30
		[15,65,40,66,20,0,0,0,0,0,0,0,0,0,0,0], # Regra 31
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 32
		[65,40,66,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 33
		[7,32,67,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 34
		[10,32,67,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 35
		[8,32,67,0,0,0,0,0,0,0,0,0,0,0,0,0], # Regra 36
		[67,32,67,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra37
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra38
		[27,7,68,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra39
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra40
		[46,69,70,45,0,0,0,0,0,0,0,0,0,0,0,0],#Regra41
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra42
		[43,69,70,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra43
		[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra44
		[10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra45
		[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra46
		[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra47
		[7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra48
		[16,46,7,71,38,45,39,65,40,66,45,72,0,0,0,0],#Regra49
		[21,38,65,40,66,45,0,0,0,0,0,0,0,0,0,0],#Regra50
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra51
		[1,46,7,71,45,38,65,40,66,0,0,0,0,0,0,0],#Regra52
		[31,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra53
		[48,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra54
		[30,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra55
		[29,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra56
		[35,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra57
		[33,73,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra58
		[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra59
		[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra60
		[10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra61
		[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra62
		[7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra63
		[18,46,7,32,73,40,7,71,40,74,45,39,65,40,66,38],#Regra64
		[36,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra65
		[49,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra66
		[23,39,65,40,66,38,1,46,7,71,45,0,0,0,0,0],#Regra67
		[25,28,7,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra68
		[24,34,12,75,0,0,0,0,0,0,0,0,0,0,0,0],#Regra69
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra70
		[34,7,76,75,0,0,0,0,0,0,0,0,0,0,0,0],#Regra71
		[34,12,75,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra72
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra73
		[43,7,76,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra74
		[79,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra75
		[27,7,68,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra76
		[37,79,80,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra77
		[50,79,80,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra78
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra79
		[81,82,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra80
		[17,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra81
		[44,81,82,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra82
		[42,81,82,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra83
		[5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra84
		[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra85
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra86
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra87
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#Regra88
		[67,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]#Regra89


		self.tabela_parsing=[[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],
		[19],[20],[21],[22],[23],[24],[25],[26],[27],[28],[29],[30],[31],[32],[33],[34],[35],[36],[37],[38],[39],
		[40],[41],[42],[43],[44],[45],[46],[47],[48],[49],[50], #Somente para ficar com a mesma codificação da gramática

		[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#51
		[0,0,3,3,0,0,0,2,0,0,0,0,0,3,0,3,0,0,0,3,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],#52
		[0,0,13,13,0,0,0,0,0,0,0,0,0,13,0,19,0,0,0,13,0,0,0,0,0,0,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#53
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#54
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,5,0,0,0,0,0,0,0],#55
		[0,0,0,8,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,7,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#56
		[0,0,10,10,0,0,0,11,0,0,0,0,0,10,0,10,0,0,0,10,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0],#57
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#58
		[0,0,0,0,0,0,0,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#59
		[0,0,15,18,0,0,0,0,0,0,0,0,0,14,0,0,0,0,0,17,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,26,0,0,0,0,0,0,27,0,0,0,0],#60
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,0,0,0,0,0,0,27,0,0,0,0],#61
		[0,0,0,24,0,20,21,0,23,22,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,0,0,0,0,0],#62
		[0,0,0,28,0,0,0,0,0,0,0,0,0,28,0,0,0,0,0,28,0,0,0,0,0,0,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#63
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,29,0,0,0,0,30,0,0,0,0,0],#64
		[0,52,0,0,0,37,37,37,37,0,37,0,0,0,0,0,49,0,64,0,0,0,0,67,69,68,0,39,0,0,0,0,0,0,0,0,0,0,0,0,38,0,0,0,0,0,37,0,0,0,0],#65
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,33,0,0,0,0,0,0,0,0,0,0,0,0],#66
		[0,0,0,0,0,75,75,75,75,0,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,76,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,0,0,0,0],#67
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0,0,0,0,0,0,0,40,0,0,0,0,40,41,0,0,0,0],#68
		[0,0,0,0,0,44,46,48,47,0,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#69
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,43,0,52,0,0,0,0,0],#70
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,55,53,0,58,57,0,0,0,0,0,0,0,0,0,0,0,0,0,54,0,0],#71
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,0,0,0,0,0,0,0,0,0,0],#72
		[0,0,0,0,0,59,60,63,68,0,61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#73
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,65,0,0,0,0,0,0,0,0,0,0,0,0,66,0],#74
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,72,0,0,0,0,0,70,0,0,0,0,0,0,0,0,0,0],#75
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,73,0,0,0,0,0,73,0,0,74,0,0,0,0,0,0,0],#76
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#77
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],#78
		[0,0,0,0,0,80,80,80,80,0,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,0,0,0,0,0],#79
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,79,0,0,0,0,77,0,0,79,0,0,0,0,79,0,0,0,0,78],#80
		[0,0,0,0,0,84,85,86,88,0,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,89,0,0,0,0],#81
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,81,0,0,0,0,81,0,0,81,0,83,0,82,0,0,81,0,0,81]] #82


	def Verificador_Sinstatico(self, entrada):
		inicial= 51 # Bloco Incial
		codigos_lex = entrada 
		tamanho = len(codigos_lex)
		i = 0
		p = Pilha()
		p.empilha(inicial)
		while i <= tamanho-1:	
			top = p.topo()
			print(str(top) + "==" +str(codigos_lex[i]) )  #DEBUG

			if top == codigos_lex[i]:
				print(p.desempilha())
				i=i+1
				


			elif self.tabela_parsing[top][codigos_lex[i]] > 0 : #FAZER: ou se for nula
				if(codigos_lex[i] <= 50 and top >=51):
					p.desempilha()
					num_regra = self.tabela_parsing[top][codigos_lex[i]]
					vetor_regra = self.regras[num_regra] 
					j = 0

					while j < len(vetor_regra):
						token = vetor_regra[j]
						if token != 0 :
							p.empilha(token)
							
						j = j+1
				
				else:
					print("Token inesperado")

			else:
				print("erro")
				i=i+1
			p.mostrar()#DEBUG


		if p.vazia() and i == (tamanho):
			print("Finalizado sem erros")
		


#Main
if __name__ == "__main__": # Só executa se for chamado direto no prompt como principal

	codigos_lex = [2, 11, 39, 9, 32, 5, 40, 15, 46, 9, 31, 5, 45, 39, 9, 32, 9, 36, 40, 38, 38] #Entrada do léxico
	Analisador_Sintatico().Verificador_Sinstatico(codigos_lex)

