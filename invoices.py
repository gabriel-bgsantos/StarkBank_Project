import starkbank
import keys
import names    #package names installed from pip
from cpf_generator import CPF   #package cpf-generator installed from pip
from random import randint

def create_invoices():
    for i in range(randint(8, 12)):     #create between 8 to 12 invoices
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=randint(1, 5000),
                name=names.get_full_name(),     #generate a random full name
                tax_id=CPF.generate()           #generate a random brazilian cpf
            )
        ])

        for invoice in invoices:
            print("Invoice Created! ID:", invoice.id)
