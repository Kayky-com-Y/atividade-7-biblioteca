from django.core.exceptions import ValidationError
from datetime import datetime

def validar_ano_publicacao(ano):
    ano_atual = datetime.now().year
    if ano < 1450 or ano > ano_atual:
        raise ValidationError(f'O ano de publicação deve estar entre 1450 e {ano_atual}.')

def validar_tamanho_arquivo(arquivo):
    limite_bytes = 1 * 1024 * 1024  # 1 MB
    if arquivo.size > limite_bytes:
        raise ValidationError('O arquivo não pode ser maior que 1 MB.')