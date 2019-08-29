###################################################
#       IFMG Campus Formiga - CC - 6° Periodo     #
# Desenvolvido por: Jefferson Marques Costa Alves #
# Git: jeffersonmca                               #
#           Desenvolvido em: 2019.2               #
###################################################
#
# Predios do sub problema
#
predios = [
	[0, 8, 5],
	[2, 10, 9],
	[1, 4, 7],
	[11, 5, 15],
	[15, 3, 17],
	[17, 11, 20],
	[19, 17, 22],
	[14, 3, 28],
	[25, 13, 30]
]
#
# Cada posicao da tripla representa uma determinada informacao
#	A primeira posicao(0)(ESQ): Indica o inicio do predio
#	A segunda  posicao(1)(ALT): Indica a altura do predio
#	A terceira posicao(2)(DIR): Indica o fim do predio
ESQ = 0
ALT = 1
DIR = 2
#
# Dada uma sequencia de triplas que representam predios retangulares
# Determinar a silhueta dos predios, ou seja, skyline
#
def skyline(predios, novoPredio):
	# Insere no vetor de predios o novo predio
	predios.append(novoPredio)
	# Pega o inicio do primeiro predio
	esquerda = min(predio[ESQ] for predio in predios)
	# Pega o fim do ultimo predio
	direita  = max(predio[DIR] for predio in predios)
	# Variavel auxiliar
	ultimaAltura = None
	# Vetor que ira armazenar a solucao final do problema
	solucao = []
	# Laco do inicio do primeiro predio ate o fim do ultimo predio
	for i in range(esquerda, direita + 1):
		# Pega as alturas de acordo com o i que esta sendo iterado no laco
		alturas = [predio[ALT] for predio in predios if predio[ESQ] <= i < predio[DIR]]
		# Escolhe a maior altura dentre as selecionadas e caso nao tiver nenhuma da como resposta o zero
		altura = max(alturas) if alturas else 0
		if altura != ultimaAltura:
			solucao += [i, altura]
			ultimaAltura = altura
	# Retorna como resposta a solucao encontrada
	return solucao
#
# Predio a ser inserido
#
novoPredio = [8, 6, 23]
print(skyline(predios, novoPredio))