# =========================================================
# CADASTRO DE PRODUTOS
# =========================================================
# PORTUGOL:
# inteiro quantidade
# real precos[100]
# cadeia nomes[100], categorias[100]
# escreva("Quantos produtos?")
# leia(quantidade)
# para i de 0 ate quantidade - 1 passo 1 faca
#     leia(nomes[i], precos[i], categorias[i])
# fimpara

produtos = []
quantidade = int(input("Quantos produtos deseja cadastrar? "))

for _ in range(quantidade):
    nome = input("\nNome do produto: ")
    preco = float(input("Preço do produto: R$ "))
    categoria = input("Categoria do produto: ")
    
    produtos.append({"nome": nome, "preco": preco, "categoria": categoria})

# =========================================================
# FILTRAGEM POR PREÇO
# =========================================================
# PORTUGOL:
# real valor_filtro
# leia(valor_filtro)
# para i de 0 ate quantidade - 1 passo 1 faca
#     se precos[i] > valor_filtro entao
#         escreva(nomes[i], precos[i])
#     fimse
# fimpara

valor_filtro = float(input("\nFiltrar produtos acima de qual valor? R$ "))
produtos_filtrados = [p for p in produtos if p["preco"] > valor_filtro]

# =========================================================
# ORDENAÇÃO
# =========================================================
# PORTUGOL (Bubble Sort para ordem crescente):
# para i de 0 ate quantidade - 1 passo 1 faca
#     para j de 0 ate quantidade - 2 - i passo 1 faca
#         se precos[j] > precos[j+1] entao
#             aux = precos[j]
#             precos[j] = precos[j+1]
#             precos[j+1] = aux
#             # (repetiria a troca para os vetores de nomes e categorias)
#         fimse
#     fimpara
# fimpara

produtos_crescente = produtos.copy()
produtos_crescente.sort(key=lambda x: x["preco"])

produtos_decrescente = sorted(produtos, key=lambda x: x["preco"], reverse=True)

# =========================================================
# CONJUNTO DE CATEGORIAS ÚNICAS
# =========================================================
# PORTUGOL (Simulação manual de conjunto/ignorar repetidos):
# cadeia unicas[100]
# inteiro qtd_unicas = 0
# para i de 0 ate quantidade - 1 passo 1 faca
#     logico existe = falso
#     para j de 0 ate qtd_unicas - 1 passo 1 faca
#         se categorias[i] == unicas[j] entao existe = verdadeiro fimse
#     fimpara
#     se nao existe entao
#         unicas[qtd_unicas] = categorias[i]
#         qtd_unicas = qtd_unicas + 1
#     fimse
# fimpara

categorias_unicas = set(p["categoria"] for p in produtos)

# =========================================================
# TUPLA DE ESTATÍSTICAS
# =========================================================
# PORTUGOL:
# real menor = precos[0], maior = precos[0], soma = 0, media
# para i de 0 ate quantidade - 1 passo 1 faca
#     se precos[i] < menor entao menor = precos[i] fimse
#     se precos[i] > maior entao maior = precos[i] fimse
#     soma = soma + precos[i]
# fimpara
# media = soma / quantidade

precos = [p["preco"] for p in produtos]
estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

# =========================================================
# RELATÓRIO FINAL FORMATADO
# =========================================================
print(f"\n{'='*40}")
print(f"--- RELATÓRIO FINAL ---")
print(f"{'='*40}")
print(f"Total de produtos cadastrados: {len(produtos)}")
print(f"Categorias únicas: {', '.join(categorias_unicas)}")
print(f"Estatísticas de Preço:")
print(f"  - Menor Preço: R$ {estatisticas[0]:.2f}")
print(f"  - Maior Preço: R$ {estatisticas[1]:.2f}")
print(f"  - Preço Médio: R$ {estatisticas[2]:.2f}")

print(f"\n>>> Produtos acima de R$ {valor_filtro:.2f}:")
for p in produtos_filtrados:
    print(f"  * {p['nome']} (R$ {p['preco']:.2f})")

print("\n>>> Produtos em Ordem Crescente de Preço:")
for p in produtos_crescente:
    print(f"  * R$ {p['preco']:.2f} - {p['nome']} [{p['categoria']}]")

print("\n>>> Produtos em Ordem Decrescente de Preço:")
for p in produtos_decrescente:
    print(f"  * R$ {p['preco']:.2f} - {p['nome']} [{p['categoria']}]")
print(f"{'='*40}\n")