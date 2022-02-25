import starkbank
import keys

def get_that_money(amount):
    transfers = starkbank.transfer.create([
        starkbank.Transfer(
            amount=amount,
            tax_id="20.018.183/0001-80",
            name="Stark Bank S.A.",
            bank_code="20018183",
            branch_code="0001",
            account_number="6341320293482496",
            account_type="payment"
        )
    ])

    for transfer in transfers:        
            if "created" in transfer.status:
                print("The transfer was completed!\n", transfer)
            else:
                print ("There was an error, the transfer couldn't be completed...")
