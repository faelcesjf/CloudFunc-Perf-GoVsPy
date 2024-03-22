# Usa a imagem oficial do Python como base.
FROM python:3.8-slim

# Define o diretório de trabalho no container.
WORKDIR /app

# Copia os arquivos da função para o diretório de trabalho.
COPY . .

# Instala o Functions Framework.
RUN pip install functions-framework

# Instala as dependências adicionais, se houver.
# Descomente a linha abaixo e ajuste conforme necessário.
RUN pip install -r requirements.txt

# Expõe a porta em que o Functions Framework ouve por padrão.
EXPOSE 8080

# Define o comando para iniciar o Functions Framework e servir sua função.
CMD ["functions-framework", "--target=main", "--debug"]

