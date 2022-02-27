import starkbank
import keys
import invoices
import webhook
import time

def main():
    timing = 8 #24 hours because at each loop 1 is out until it reaches 0, then it stops
    while timing != 0:
        keys.authenticator()
        invoices.create_invoices()
        webhook.url_webhooks()
        webhook.webhooks()
        timing -= 1 #one is out at each loop, so the loops don't run forever
        time.sleep(10800)   #each loop runs only every 3 hours


if __name__ == '__main__':
        main()
