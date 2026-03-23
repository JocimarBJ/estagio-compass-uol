import boto3
import os
from dotenv import load_dotenv

# ======================== ANÁLISES ========================
# - Consistência das avaliações entre gêneros
# - Influência do formato (filme/série) na consistência
# - Influência do engajamento na estabilidade das avaliações
# - Impacto da popularidade na dispersão das notas
# - Influência de franquias na consistência

# ======================== CONFIG ========================
# Carrega variáveis do .env
load_dotenv()
print("[.env] ENV carregado")

api_key = os.getenv("API_KEY_TMDB")
print("[KEYS] API Key carregada:", "OK" if api_key else "ERRO")

# Acesso ao S3
access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token = os.getenv("AWS_SESSION_TOKEN")
region = os.getenv("AWS_DEFAULT_REGION")
bucket=os.getenv("BUCKET_NAME")

s3 = boto3.client("s3",
                  aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key,
                  aws_session_token=session_token,
                  region_name=region
                  )
print("[AWS S3] Conectado ao S3!")

# ======================== ETAPA 1 - EXPORT CSV LOCAL ==========================
# Upload dos Arquivos CSV (presentes na pasta etapa-1)
s3.upload_file("movies.csv", bucket, f"raw/local/csv/movies/2026/03/20/movies.csv")
print("[UPLOAD] movies.csv uploaded from local")

s3.upload_file("series.csv", bucket, f"raw/local/csv/series/2026/03/20/series.csv")
print("[UPLOAD] series.csv uploaded from local")