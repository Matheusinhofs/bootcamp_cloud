import os
from typing import List
import boto3
from dotenv import load_dotenv

# carregar as variáveis do arquivo .env 
load_dotenv()

# Puxa as configurações da AWS pelo .env
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# Configura o cliente S3
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# LE OS ARQUIVOS

def listar_arquivos(pasta: str) -> List[str]:
    """Lista todos os arquivos em uma pasta local."""
    arquivos: List[str] = []
    for nome_arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_completo):
            arquivos.append(caminho_completo)
    return arquivos

# JOGA OS ARQUIVOS NO S3
def upload_arquivos_para_s3(arquivos: List[str]) -> None:
    """Faz upload dos arquivos listados para o S3."""
    for arquivo in arquivos:
        nome_arquivo: str = os.path.basename(arquivo)
        s3_client.upload_file(arquivo, BUCKET_NAME, nome_arquivo)
        print(f'{nome_arquivo} foi enviado para o S3.')

# DELETAR OS ARQUIVOS LOCAL
def deletar_arquivos_locais(arquivos: List[str]) -> None:
    """Deleta os arquivos locais após o upload."""
    for arquivo in arquivos:
        os.remove(arquivo)
        print(f'{arquivo} foi deletado do local.')

# PIPELINE DE DADOS
def executar_backup(pasta: str) -> None:
    """Executa o processo completo de backup."""
    arquivos: List[str] = listar_arquivos(pasta)
    if arquivos:
        upload_arquivos_para_s3(arquivos)
        deletar_arquivos_locais(arquivos)
    else:
        print("Nenhum arquivo encontrado para backup.")

if __name__ == "__main__":
    PASTA_LOCAL: str = r'C:\Users\Uso Geral\workspace\jornada\bootcamp_cloud\aula_02\teste_projeto'  # Substitua pelo caminho da sua pasta local
    executar_backup(PASTA_LOCAL)
