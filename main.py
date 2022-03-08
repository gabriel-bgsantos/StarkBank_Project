import starkbank
import keys
import invoices
import webhook
import time

def main():
    timing = 8 #24 hours because at each loop 1 is out until it reaches 0, then it stops
    while timing != 0:
        print("--- New loop starting ---")
        keys.authenticator()
        invoices.create_invoices()
        
        #the if below prevents the asking of new Webhook URLs after the first loop (which throws the "URL is already being used" error)
        if timing == 8:
            webhook.url_webhooks()
        else:
            pass
        
        webhook.webhooks()
        timing -= 1 #one is out at each loop, so the loops don't run forever
        print("Finishing this loop. Loops remaining:", timing,"\nJust wait...\n")
        time.sleep(10800)   #each loop runs only every 3 hours
    
    print("All loops have ended, the program is being closed...")

if __name__ == '__main__':
        main()
