import starkbank

def first_validation():     #this function makes the first question showed and its validations
    while True:
        first_question = input("Do you want to fully see an Event's info? [Y/n]: ")
        if first_question in ["y", "Y"]:       
            events_validation()
        elif first_question in ["n", "N"]:     
            print("The program is being closed...")
            exit()
        else:
            print("Invalid character")
            second_validation()      

def events_validation():     #this function makes the event's ID question and its validations, if typed correctly it shows all the info of the event's id
    event_id = input("Insert the Event's ID [EXIT to cancel]: ")
    
    #the if below need a fix once it just works when typed a valid event's id on the query
    if (len(event_id)) == 16:   #all the event's id have the same amount of numbers: 16, so this line makes sure the default is followed
        print("----SEARCHING THE EVENT, JUST WAIT...----")
        print(starkbank.event.get(event_id))    #it gets the event from the query and prints it
    elif event_id in ["exit", "EXIT"]:
        print("The program is being closed...")
        exit() 
    else:
        print("Invalid Event's ID")
        events_validation()  #if the input is invalid, return to the beginning of this function
    
def second_validation():    #this one just make sure if you really want to continue or not
    second_question = input("Do you want to continue?: [Y/n] ")
    if second_question in ["y", "Y"]:
        return
    elif second_question in ["n", "N"]:
        print("The program is being closed...")
        exit()
    else:
        print("Invalid character")
        return
