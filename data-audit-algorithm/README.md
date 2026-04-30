# 🛡️ Algoritmo de Auditoria e Análise de Vendas

## 📝 Descrição do Projeto
Este projeto consiste em um protótipo de sistema de auditoria financeira desenvolvido para identificar **discrepâncias de dados (Outliers)** em registros de vendas. O sistema utiliza conceitos de **margem de tolerância** para monitorar a integridade dos dados e identificar possíveis fraudes, erros ou inconsistências.

O algoritmo processa entradas de valores, calcula a média e valida se os dados individuais ou a média do período ultrapassam limites de segurança pré-estabelecidos, disparando alertas de "Quarentena" ou "Revisão Manual".

## 🚀 Tecnologias e Conceitos
  **Linguagem:** Python.
  **Normalização:** Processo de ajuste de dados para torná-los comparáveis e menos distorcidos, ignorando valores extremos.
  **Detecção de Outliers:** Identificação de valores que divergem drasticamente da média e podem falsear resultados reais.

## 📊 Lógica de Auditoria
O sistema opera baseado em gatilhos automáticos de segurança definidos no código:

**Cálculo de Média:** O sistema consolida três valores de entrada para gerar a base de comparação.
**Controle de Quarentena:** Se a média das vendas ultrapassa o **Limite de Segurança** (padrão de $10.000$), o sistema entra automaticamente em estado de quarentena.
**Sugestão de Revisão Manual:** O sistema identifica se algum valor individual é significativamente superior à média (ex: maior que $m \times 2$), sugerindo que um humano revise o dado.
**Ajuste de Sensibilidade:** O auditor tem a opção de alterar o limite de segurança durante a execução para adaptar o sistema a novos cenários.

## 🔧 Como Executar
1. Certifique-se de ter o Python instalado.
2. O script solicitará a entrada de três valores de venda.
3. O sistema exibirá a média e o status da auditoria (OK, Quarentena ou Revisão Sugerida).
4. Caso necessário, siga as instruções na tela para alterar os limites de segurança.

---
[Voltar ao início](https://github.com/Vinicius-941/portfolio-vinicius-dias-gomes)
