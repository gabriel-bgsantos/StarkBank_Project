import starkbank
import keys
import invoices
import webhook
import time

def main():
    while(True):
        keys.authenticator()
        invoices.create_invoices()
        webhook.url_webhooks()
        webhook.webhooks()
        time.sleep(10800) #it runs every 3 hours

if __name__ == '__main__':
        main()
