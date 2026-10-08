# Sistema de Análise de Dados - Semana 05

Este projeto lê ficheiros contendo dados de clientes (e-mail, CPF, telefone e data) e utiliza Expressões Regulares (Regex) para validar cada campo, gerando um relatório estruturado no final.

## Justificativa das Validações (Regex)
Os padrões definidos com o módulo `re` do Python visam garantir a integridade da base de dados:
- **E-mail:** Verifica a presença de texto, seguido de `@`, texto para o domínio e `.` seguido de texto (ex: `\w+@\w+\.\w+`).
- **CPF:** Assegura que contém exatamente 11 dígitos, aceitando a formatação com ou sem pontuação (ex: `123.456.789-00`). Utilizei o padrão `\d{3}\.?\d{3}\.?\d{3}-?\d{2}`.
- **Telefone:** Garante o código de área de 2 dígitos e números de telemóvel/fixo brasileiros.
- **Data:** Confirma dias entre 01-31, meses entre 01-12 e anos de 4 dígitos.

## Exceções Tratadas
O sistema utiliza um bloco completo `try/except/else/finally`:
- `FileNotFoundError`: Impede o sistema de quebrar se o ficheiro CSV não existir.
- `KeyError`: Avisa o utilizador se as colunas essenciais estiverem ausentes no cabeçalho do ficheiro.
- `FormatoInvalidoError`: **Exceção personalizada** criada (herdando de `Exception`) para rotular os registos onde os metacaracteres da regex não encontram uma correspondência (dado inválido).

## Exemplo de Entrada e Saída
**Entrada (dados.csv):**
email_errado.com,98765432100,21988887777,32/13/2024

**Saída (Relatório):**
Registos INVÁLIDOS: 1
* Email: email_errado.com | CPF: 98765432100
  Falha: Dados em formato incorreto ou corrompidos.