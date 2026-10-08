import re
import csv

# 1. Exceção Personalizada
class FormatoInvalidoError(Exception):
    """Exceção levantada quando um registo não cumpre as regras de formatação (Regex)."""
    pass

# 2. Funções de Validação com Regex (Expressões Regulares)
def validar_email(email):
    # Verifica o formato padrao@dominio.com
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))

def validar_cpf(cpf):
    # Aceita formato 123.456.789-00 ou 12345678900
    padrao = r"^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$"
    return bool(re.match(padrao, cpf))

def validar_telefone(telefone):
    # Aceita (11) 98765-4321 ou 11987654321
    padrao = r"^\(?\d{2}\)?\s?(?:9\d{4}|\d{4})-?\d{4}$"
    return bool(re.match(padrao, telefone))

def validar_data(data):
    # Aceita DD/MM/AAAA ou DD-MM-AAAA
    padrao = r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[012])[-/]\d{4}$"
    return bool(re.match(padrao, data))

# 3. Tratamento de Exceções e Leitura de Ficheiro
def analisar_dados(caminho_arquivo):
    registros_validos = []
    registros_invalidos = []
    total_registros = 0
    
    try:
        # with open garante o fechamento automático do ficheiro
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            
            # Valida se as colunas esperadas existem para evitar KeyError posterior
            colunas_esperadas = ['email', 'cpf', 'telefone', 'data']
            if not all(coluna in leitor_csv.fieldnames for coluna in colunas_esperadas):
                raise KeyError(f"Faltam colunas. O arquivo deve conter: {', '.join(colunas_esperadas)}")

            for linha in leitor_csv:
                total_registros += 1
                
                email_ok = validar_email(linha['email'])
                cpf_ok = validar_cpf(linha['cpf'])
                tel_ok = validar_telefone(linha['telefone'])
                data_ok = validar_data(linha['data'])
                
                # Se tudo estiver correto, adiciona aos válidos
                if email_ok and cpf_ok and tel_ok and data_ok:
                    registros_validos.append(linha)
                else:
                    # Lança e captura a nossa exceção personalizada para simular o requisito
                    try:
                        raise FormatoInvalidoError("Dados em formato incorreto ou corrompidos.")
                    except FormatoInvalidoError as erro:
                        linha['motivo_erro'] = str(erro)
                        registros_invalidos.append(linha)

    # Tratamento de erros comuns
    except FileNotFoundError:
        print(f"\n[ERRO CRÍTICO] O arquivo '{caminho_arquivo}' não foi encontrado na pasta.")
    except KeyError as e:
        print(f"\n[ERRO DE ESTRUTURA] {e}")
    except ValueError as e:
        print(f"\n[ERRO DE VALOR] Falha ao processar os dados: {e}")
    except Exception as e:
        print(f"\n[ERRO INESPERADO] Ocorreu um problema desconhecido: {e}")
    
    else:
        # 4. Relatório Formatado (executa se não houver erros críticos (ex: FileNotFoundError))
        print(f"\n{'='*55}")
        print(f"--- RELATÓRIO DE ANÁLISE DE DADOS ---")
        print(f"{'='*55}")
        print(f"Total de registos processados : {total_registros}")
        print(f"Registos VÁLIDOS             : {len(registros_validos)}")
        print(f"Registos INVÁLIDOS           : {len(registros_invalidos)}\n")
        
        if registros_invalidos:
            print(">>> Detalhe dos registos com falha de validação:")
            for reg in registros_invalidos:
                print(f"  * Email: {reg['email']} | CPF: {reg['cpf']}")
                print(f"    Falha: {reg.get('motivo_erro')}")
        print(f"{'='*55}\n")
    
    finally:
        # Bloco finally é sempre executado
        print("[SISTEMA] Processo de análise finalizado.\n")

if __name__ == "__main__":
    analisar_dados("dados.csv")