from datetime import datetime

data = input("Digite a data: ")

def date_to_string_extend(data: str) -> str:
    '''
    Função converte data para data extensa
    '''
    if data_valida(data): 

        dia = data.split("/")[0]
        mes = int(data.split("/")[1])
        ano = data.split("/")[2]

        if mes == 1:
            mes = "Janeiro"
        
        elif mes == 2:
            mes = "Fevereiro"
        
        elif mes == 3:
            mes = "Março"
        
        elif mes == 4:
            mes = "Abril"
        
        elif mes == 5:
            mes = "Maio"
        
        elif mes == 6:
            mes = "Junho"
        
        elif mes == 7:
            mes = "Julho"
        
        elif mes == 8:
            mes = "Agosto"
        
        elif mes == 9:
            mes = "Setembro"
        
        elif mes == 10:
            mes = "Outubro"
        
        elif mes == 11:
            mes = "Novembro"
        
        else:
            mes = "Dezembro"
        
        data = str(dia + " de " + mes + " de " + ano) 

        return data
    return None


def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        return False


print(date_to_string_extend(data))

