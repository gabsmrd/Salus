import os
from random import choice, shuffle
import string
from django.conf import settings
from django.template.loader import render_to_string
from io import BytesIO
from weasyprint import HTML


def gerar_senha_aleatoria(tamanho):
    caracteres_especiais = string.punctuation   
    caracteres = string.ascii_letters
    numeros_list = string.digits

    sobra = 0
    qtd = tamanho // 3
    if not tamanho % 3 == 0:
        sobra = tamanho - qtd

    letras = ''.join(choice(caracteres) for _ in range(qtd + sobra))
    numeros = ''.join(choice(numeros_list) for _ in range(qtd))
    especiais = ''.join(choice(caracteres_especiais) for _ in range(qtd))

    senha = list(letras + numeros + especiais)
    shuffle(senha)

    return ''.join(senha)


def gerar_pdf_exames(exame, paciente, senha):
    path_template = os.path.join(settings.BASE_DIR, 'templates/partials/senha_exame.html')
    template_render = render_to_string(path_template, {'exame': exame, 'paciente': paciente, 'senha': senha})

    path_output = BytesIO()

    HTML(string=template_render).write_pdf(path_output)
    path_output.seek(0)
    
    return path_output
