from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
import re


class Client(BaseModel):
    id_cliente: Optional[int] = Field(0)
    ds_nome: str 
    ds_cpf:str
    ds_email:str

    @field_validator('ds_cpf')
    def validate_cpf(cls, cpf):            
        """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

        Parâmetros:
            cpf (str): CPF a ser validado

        Retorno:
            bool:
                - Falso, quando o CPF não possuir o formato 999.999.999-99;
                - Falso, quando o CPF não possuir 11 caracteres numéricos;
                - Falso, quando os dígitos verificadores forem inválidos;
                - Verdadeiro, caso contrário.

        """

        validacao = ''

        # Verifica a formatação do CPF
        if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
            validacao = False

        # Obtém apenas os números do CPF, ignorando pontuações
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Verifica se o CPF possui 11 números ou se todos são iguais:
        try:
            if len(numbers) != 11 or len(set(numbers)) == 1:
                validacao =  False
        except:
            raise ValueError('Formato incorreto de cpf')

        # Validação do primeiro dígito verificador:
        try:
            sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[9] != expected_digit:
                validacao =  False
        except:
            raise ValueError('Formato incorreto de cpf')

        # Validação do segundo dígito verificador:
        try:
            sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
            expected_digit = (sum_of_products * 10 % 11) % 10
            if numbers[10] != expected_digit:
                validacao =  False
        except:
            raise ValueError('Formato incorreto de cpf')

        if not validacao:
            return cpf
        else:
            raise ValueError('Formato incorreto de cpf')
        


    @field_validator('ds_email')
    def valida_email_simples(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError('Formato incorreto de email. Lembre-se se ter um endereço com @')
