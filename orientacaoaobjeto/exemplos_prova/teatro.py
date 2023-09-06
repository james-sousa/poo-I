preco = 5.00
pessoas = 120
variacao = 0.50
custo = 200.00

while preco > 1.00:
    print("Preço = ,quant = , lucro = ",preco,pessoas,(pessoas* preco) - custo)
    preco -= variacao
    pessoas += 26
    lm = (preco * pessoas) - custo

print("Lucro: ",lm)
print("Preço: ",preco)
print("Quantidade: ",pessoas)