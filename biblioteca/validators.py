from django.core.exceptions import ValidationError


def validar_tamanho_arquivo(arquivo):
    limite = 1024 * 1024
    if arquivo.size > limite:
        raise ValidationError('A capa não pode ter mais de 1 MB.')
