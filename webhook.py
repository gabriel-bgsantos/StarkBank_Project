from datetime import datetime
import starkbank
import transference

def url_webhooks():
    webhook_url = input("Insert here your Webhook's URL: ") 
    try:
        webhook = starkbank.webhook.create(     #receiving the webhook events through the link inserted above
            url=webhook_url,
            subscriptions=[
                "invoice"
            ]
        )
    except:     #making sure a valid URL is inserted
        print("Invalid URL !")
        answer = input("Do you want to continue? [Y/n]: ")
        if answer in ["Y", "y"]:
            url_webhooks()
        elif answer in ["N", "n"]:
            print("The program is being closed...")
            exit()
        else:
            print("Invalid character - Try again")
            url_webhooks()
            

#The function below depends on frequent Webhook queries in order to make and store new transfers
def webhooks():  
    date = datetime.now().strftime("%Y-%m-%d") #making it a string
    events = starkbank.event.query(after=date)
    for event in events:
        
        if event.log.type == "credited":    #if the event has the "credited" type status, request a Transfer and store the Event's ID
            file = open("./StarkBank_Test/credited_list.txt", "r+")  #open the file used to store Events' IDs, then read it and goes to the file's last line (r+)
            
            if str(event.id) not in file.read():    #if the ID isn't on the file list, request the transfer and store the current Event's ID
                transference.get_that_money(event.log.invoice.amount)
                print("\nEvent ID: ", event.id, "transfer requested, amount:", event.log.invoice.amount) 
                file.write(event.id)
                file.write(" - ")   #just formating the .txt
                file.write(date)
                file.write("\n")
                file.close()
                print("Event ID: ", event.id, "added to the list!\n")
            else:
                file.close()
                print("Event ID: ", event.id, "already on the list.")
        
        else:
            pass
