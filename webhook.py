from datetime import datetime
import starkbank
import transference

def url_webhooks(): 
    webhook = starkbank.webhook.create(     #receiving the webhook events through the link below
        url="insert your url here",
        subscriptions=[
            "invoice"
        ]
    )

def webhooks():         #transfers the right amount to everyone with the "credited" status
    events = starkbank.event.query(after=datetime.now())
    for event in events:
            if event.log.type == "credited": 
                transference.get_that_money(event.log.invoice.amount) 
