matriz = [
    ["C", "A", "R", "R", "O", "S"],
    ["B", "O", "L", "A", "S", "A"],
    ["G", "A", "T", "O", "S", "M"],
    ["P", "E", "I", "X", "E", "D"],
    ["L", "U", "A", "R", "T", "E"],
    ["F", "O", "G", "O", "S", "A"]
]

palavra = input("Digite uma palavra: ").upper()

n_linhas = len(matriz)
n_cols = len(matriz[0])
tam = len(palavra)

for L in range(n_linhas):
    AUX = ""

    for C in range(n_cols):
        AUX += matriz[L][C]

    if palavra in AUX:
        print(palavra, "está na linha:", L, "esquerda -> direita")

for L in range(n_linhas):
    AUX = ""

    for C in range(n_cols - 1, -1, -1):
        AUX += matriz[L][C]

    if palavra in AUX:
        print(palavra, "está na linha:", L, "direita -> esquerda")

for C in range(n_cols):
    AUX = ""

    for L in range(n_linhas):
        AUX += matriz[L][C]

    if palavra in AUX:
        print(palavra, "está na coluna:", C, "cima -> baixo")

for C in range(n_cols):
    AUX = ""

    for L in range(n_linhas - 1, -1, -1):
        AUX += matriz[L][C]

    if palavra in AUX:
        print(palavra, "está na coluna:", C, "baixo -> cima")

AUX = ""

for i in range(min(n_linhas, n_cols)):
    AUX += matriz[i][i]

if palavra in AUX:
    print(palavra, "está na diagonal principal")

AUX = ""

for i in range(min(n_linhas, n_cols)):
    AUX += matriz[i][n_cols - 1 - i]

if palavra in AUX:
    print(palavra, "está na diagonal secundária")
