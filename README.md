# CloudFunc-Benchmark: Golang vs Python

## Sobre o Projeto

Este repositório abriga o CloudFunc-Benchmark, um estudo aprofundado que compara o desempenho e a eficiência de custo das Google Cloud Functions escritas em Golang e Python. Utilizando o Google Cloud Pub/Sub como mecanismo de disparo de eventos, nosso objetivo é fornecer uma análise comparativa detalhada para orientar desenvolvedores e arquitetos de sistemas na escolha de tecnologias para implementações serverless.

## Objetivos

- **Comparação de Desempenho**: Avaliar o tempo de execução, uso de memória e latência de cold start entre funções serverless escritas em Golang e Python.
- **Análise de Eficiência de Custo**: Examinar o impacto da linguagem de programação na eficiência de custo operacional das Cloud Functions.
- **Benchmarking com Pub/Sub**: Utilizar o Google Cloud Pub/Sub como gatilho para ativar as Cloud Functions e analisar seu impacto no desempenho e nos custos.

## Como Começar

### Pré-requisitos

- Uma conta no Google Cloud Platform (GCP).
- O Google Cloud SDK instalado e configurado.
- Conhecimento básico em Golang e Python.

### Configuração

1. **Clone o Repositório**:

    ```bash
    git clone https://github.com/[seu-usuario]/CloudFunc-Perf-GoVsPy.git
    ```

2. **Configure seu ambiente GCP**:

    Siga as instruções disponíveis na [Documentação do Google Cloud](https://cloud.google.com/docs) para configurar seu projeto e habilitar as APIs necessárias.

### Execução

[Inclua instruções detalhadas sobre como executar os benchmarks, com os comandos necessários e quaisquer configurações específicas.]

## Estrutura do Projeto

O projeto é organizado nas seguintes pastas:

- **analytics**: Contém o projeto utilizado para extrair os dados de desempenho dos containers, simulando o ambiente das Google Cloud Functions.
- **python**: Inclui o scraping realizado em Python, com detalhes para execução.
- **golang**: Armazena o scraping feito em Golang, também com instruções para execução.

## Benchmarking e Análise

[Insira aqui a análise baseada no artigo que desenvolvemos, incluindo pontos chave e descobertas relevantes.]

## Contribuindo

Sua contribuição é muito valiosa! Se tiver melhorias ou sugestões, por favor, crie uma issue ou envie um pull request.

