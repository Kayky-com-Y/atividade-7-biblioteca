from django.core.exceptions import ValidationError
from datetime import datetime

def validar_ano_publicacao(ano):
    ano_atual = datetime.now().year
    if ano < 1450 or ano > ano_atual:
        raise ValidationError(f'O ano de publicação deve estar entre 1450 e {ano_atual}.')

