# EX4 - Traduzindo Lógica para Python

## 📌 Código

```python
def processar_vendas():
    total_compra = 0.0
    itens_comprados = 0

    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados? "))

    for i in range(quantidade_tipos):
        produto = input("Nome do produto: ")
        preco = float(input("Preço unitário: "))
        qtd = int(input("Quantidade deste produto: "))

        if preco <= 0 or qtd <= 0:
            print(f"Erro: Valores inválidos para {produto}")
        else:
            subtotal = preco * qtd
            total_compra += subtotal
            itens_comprados += qtd

    if total_compra > 500.00:
        total_final = total_compra * 0.90
        print("Desconto de 10% aplicado!")

    elif total_compra > 200.00:
        total_final = total_compra * 0.95
        print("Desconto de 5% aplicado!")

    else:
        total_final = total_compra

    print(f"Resumo: {itens_comprados} itens. Total a pagar: R$ {total_final:.2f}")


def analisar_clima():
    soma_temperaturas = 0.0
    dias_quentes = 0
    alerta_extremo = False

    for dia in range(1, 8):
        temp = float(input(f"Digite a temperatura do dia {dia}: "))
        soma_temperaturas += temp

        if temp > 35.0:
            dias_quentes += 1

        if temp > 45.0 or temp < -5.0:
            alerta_extremo = True

    media = soma_temperaturas / 7

    print(f"\nMédia semanal: {media:.1f}°C")
    print(f"Dias acima de 35°C: {dias_quentes}")

    if alerta_extremo:
        print("CUIDADO: Condições climáticas perigosas detectadas!")
    else:
        print("Clima dentro da normalidade operacional.")


def sistema_notas_turma():
    total_alunos = int(input("Quantos alunos existem na turma? "))

    for j in range(1, total_alunos + 1):
        print(f"\n--- Processando Aluno {j} ---")

        aluno_nome = input("Nome do aluno: ")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))

        media_aluno = (n1 + n2) / 2

        if media_aluno >= 7.0:
            print(f"{aluno_nome}: Aprovado com média {media_aluno:.1f}")

        elif media_aluno >= 5.0:
            print(f"{aluno_nome}: Recuperação (Média: {media_aluno:.1f})")

        else:
            print(f"{aluno_nome}: Reprovado")


def simulador_poupanca():
    saldo = float(input("Valor inicial do investimento: "))
    taxa = float(input("Taxa de juros mensal (em %): "))
    meses = int(input("Número de meses da simulação: "))

    for m in range(1, meses + 1):
        aporte = float(input(f"\nQuanto deseja depositar no mês {m}? (0 para nenhum): "))

        saldo += aporte

        juros = saldo * (taxa / 100)
        saldo += juros

        print(f"Mês {m}: Saldo atualizado = R$ {saldo:.2f}")

        if saldo > 10000.0:
            print(f"-> Parabéns! Você atingiu a meta de 10k no mês {m}")

    print("-" * 30)
    print(f"Resultado final após {meses} meses: R$ {saldo:.2f}")
```