# ❓ Perguntas e Respostas

## Pergunta 1
### O que acontece se não usar `int()` ou `float()` no `input()`?

Se não usar `int()` ou `float()` no `input()`, o Python interpreta os valores como texto. Isso faz com que as operações matemáticas não funcionem corretamente, podendo gerar erros ou apenas concatenar os valores.

---

## Pergunta 2
### Por que usamos `range(1, meses + 1)`?

No Python, `range()` possui limite superior exclusivo. Isso significa que ele para antes do valor final informado. Por isso usamos `meses + 1`, garantindo que o laço execute até o último mês desejado.