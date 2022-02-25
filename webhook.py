from datetime import datetime
import starkbank
import transfer

def url_webhooks():
    webhook = starkbank.webhook.create(
        url="url",
        subscriptions=[
            "invoice"
        ]
    )

def webhooks():
    daytoday = datetime.today()
    events = starkbank.event.query(after=daytoday)
    credited_invoices_list = list()
    
    for event in events:
        if "credited" in event.log.type:
            invoice_id = event.log.invoice.id
            
            if invoice_id not in credited_invoices_list:    #if this id isn't on the list, transfer the amount and add the id on the list
                transfer.transfering(event.log.invoice.amount)
                credited_invoices_list.append(invoice_id)
            else:
                if invoice_id in credited_invoices_list:
                    credited_invoices_list.remove(invoice_id)
