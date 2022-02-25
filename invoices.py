import starkbank
import keys
from names import random_names
from cpf import random_cpf
from random import randint

def create_invoices():
    for i in range(randint(8, 12)):     #create between 8 to 12 invoices
        invoices = starkbank.invoice.create([
            starkbank.Invoice(
                amount=randint(1, 5000),
                name=random_names(),
                tax_id=random_cpf()
            )
        ])

        for invoice in invoices:
            print(invoice)
