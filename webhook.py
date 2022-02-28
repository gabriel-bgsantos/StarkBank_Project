from datetime import datetime
import starkbank
import transference
import events_info

def url_webhooks(): 
    webhook = starkbank.webhook.create(     #receiving the webhook events through the link below
        url="insert your url here",
        subscriptions=[
            "invoice"
        ]
    )

def webhooks():         #transfers the right amount to everyone with the "credited" status
    events = starkbank.event.query(after=datetime.utcnow())
    for event in events:
            if event.log.type == "credited": 
                transference.get_that_money(event.log.invoice.amount)
                print("Event ID: ",[event]," Transfer requested, amount: ", event.log.invoice.amount) 

    events_info.first_validation()
