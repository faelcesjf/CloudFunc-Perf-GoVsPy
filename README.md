# CloudFunc-Benchmark: Golang vs Python

## Sobre o Projeto

Este projeto investiga o desempenho e a eficiência de custos de Google Cloud Functions escritas em Golang e Python, utilizando o Google Cloud Pub/Sub como um mecanismo de disparo de eventos. Nosso objetivo é fornecer uma análise comparativa detalhada que ajude desenvolvedores e arquitetos de sistemas a tomar decisões informadas sobre a escolha de tecnologias para suas soluções serverless.

## Objetivos

- **Comparar Desempenho**: Avaliar o tempo de execução, uso de memória e latência de inicialização entre Golang e Python em Cloud Functions.
- **Analisar Eficiência de Custo**: Estudar o impacto da escolha da linguagem no custo operacional das Cloud Functions, com uma análise de custo estimado versus custo real após a implementação.
- **Benchmarking com Pub/Sub**: Utilizar Google Cloud Pub/Sub para disparar as Cloud Functions e analisar o impacto no desempenho e custo.

## Como Começar

### Pré-requisitos

- Conta no Google Cloud Platform (GCP)
- Google Cloud SDK instalado e configurado
- Conhecimento básico em Golang e Python

### Configuração

1. **Clone o Repositório**

    ```bash
    git clone https://github.com/seu-usuario/CloudFunc-Perf-GoVsPy.git
    ```

2. **Configure o GCP**

    Siga as instruções disponíveis na [Documentação do Google Cloud](https://cloud.google.com/docs) para configurar seu projeto e habilitar as APIs necessárias.

### Execução

[Explique como executar os benchmarks, incluindo comandos necessários e qualquer configuração específica.]

## Estrutura do Projeto

[Descreva a estrutura de diretórios do projeto, explicando o propósito de cada pasta e arquivo importante.]

## Benchmarking e Análise

[Detalhe como os testes de benchmark serão executados e como os resultados serão analisados. Inclua informações sobre as métricas de desempenho e eficiência de custos que serão medidas.]

## Contribuindo

Encorajamos contribuições! Se você tem sugestões para melhorar o benchmark ou a análise, por favor, abra uma issue ou envie um pull request.

## Licença

MIT License

Copyright (c) [2024] [Rafael de Carvalho Clemente Oliveira]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


