from django.http import HttpResponse
from django.http import JsonResponse

def test1(request,number,string):
    return HttpResponse('Olá, ' + string + '. O número digitado foi: ' + str(number))

def readFromDb(name):
    lista_nomes = [
        {'nome': 'Marcus', 'idade': 35},
        {'nome': 'Mariana', 'idade': 26},
        {'nome': 'João', 'idade': 29},
        {'nome': 'Levy', 'idade': 26}
    ]

    pessoa = {'nome': 'Não encontrado', 'idade': 'none'}

    for person in lista_nomes:
        if person['nome'] == name:
            pessoa = person

    return pessoa

def funcname(request,name):

    return JsonResponse(readFromDb(name))