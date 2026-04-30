# 🛡️ Algoritmo de Auditoria e Análise de Vendas

## 📝 Descrição do Projeto
[cite_start]Este projeto consiste em um protótipo de sistema de auditoria financeira desenvolvido para identificar **discrepâncias de dados (Outliers)** em registros de vendas[cite: 2, 10]. [cite_start]O sistema utiliza conceitos de **margem de tolerância** para monitorar a integridade dos dados e identificar possíveis fraudes, erros ou inconsistências[cite: 8, 9].

[cite_start]O algoritmo processa entradas de valores, calcula a média e valida se os dados individuais ou a média do período ultrapassam limites de segurança pré-estabelecidos, disparando alertas de "Quarentena" ou "Revisão Manual"[cite: 17, 21, 30].

## 🚀 Tecnologias e Conceitos
* [cite_start]**Linguagem:** Python[cite: 13, 16].
* [cite_start]**Normalização:** Processo de ajuste de dados para torná-los comparáveis e menos distorcidos, ignorando valores extremos[cite: 5, 6].
* [cite_start]**Detecção de Outliers:** Identificação de valores que divergem drasticamente da média e podem falsear resultados reais[cite: 3].

## 📊 Lógica de Auditoria
O sistema opera baseado em gatilhos automáticos de segurança definidos no código:

* [cite_start]**Cálculo de Média:** O sistema consolida três valores de entrada para gerar a base de comparação[cite: 13, 17].
* [cite_start]**Controle de Quarentena:** Se a média das vendas ultrapassa o **Limite de Segurança** (padrão de $10.000$), o sistema entra automaticamente em estado de quarentena[cite: 11, 21, 23].
* [cite_start]**Sugestão de Revisão Manual:** O sistema identifica se algum valor individual é significativamente superior à média (ex: maior que $m \times 2$), sugerindo que um humano revise o dado[cite: 27, 30].
* [cite_start]**Ajuste de Sensibilidade:** O auditor tem a opção de alterar o limite de segurança durante a execução para adaptar o sistema a novos cenários[cite: 31, 39].

## 🔧 Como Executar
1. [cite_start]Certifique-se de ter o Python instalado[cite: 13].
2. [cite_start]O script solicitará a entrada de três valores de venda[cite: 13].
3. [cite_start]O sistema exibirá a média e o status da auditoria (OK, Quarentena ou Revisão Sugerida)[cite: 19, 23, 26, 30].
4. [cite_start]Caso necessário, siga as instruções na tela para alterar os limites de segurança[cite: 36, 39].

## ⚠️ Observações de Teste
* [cite_start]**Teste de Estresse:** Em testes com valores como $100, 200$ e $5000$, a média de $1766,66$ manteve o sistema abaixo do limite, mas destacou a importância de ajustar a sensibilidade da detecção de discrepâncias[cite: 53, 54].
* [cite_start]**Melhorias Identificadas:** O código permite que qualquer usuário altere limites (vulnerabilidade) e a lógica de validação poderia ser otimizada com estruturas de repetição (*loops*) em vez de condicionais simples[cite: 56, 57].

---
[Voltar ao início](https://github.com/seu-usuario/seu-repositorio)
