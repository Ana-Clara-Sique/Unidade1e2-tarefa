from flask import render_template

def autor_controller():
    nome = "João da Silva"
    formacoes =[{"curso": "Engenharia da Computação" , "Instituição": "Universidade XYZ" , "ano":2020} ] 
    experiencias = [{"funcao": "Desenvolvedor de Software" , "empresa": "Tech Solutions", "ano": 2024} ]
    return render_template('autor.html', nome=nome , formacoes=formacoes,experiencias=experiencias)