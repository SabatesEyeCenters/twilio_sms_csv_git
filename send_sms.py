import csv,datetime
from twilio.rest import Client

# Twilio Account SID and Auth Token
client = Client("TwilioAccountSID", "TwilioAuthToken")
from_num = "+12345678888"
csv_file = "//pathToCSVFile/smsdata.csv"
current_datetime = datetime.datetime.now()

session = ''
if (current_datetime.strftime('%p'))=='AM':
    session = 'this afternoon'
elif (current_datetime.strftime('%p'))=='PM':
    session = 'tomorrow morning'

greeting = ''
if (current_datetime.strftime('%p'))=='AM':
    greeting = 'morning'
elif (current_datetime.strftime('%p'))=='PM':
    greeting = 'evening'
    
with open(csv_file) as sms_data:
    row_count = 0
    csv_reader = csv.reader(sms_data,delimiter=",")

    for each in csv_reader:
        if row_count == 0:
#           skip header row
            row_count += 1
        else:
#           print(f'{each}')#For testing
            client.messages.create(
            to={each[0]}, 
            from_=(from_num), 
            body=(f'Good {greeting} Dr. {each[2]}.\n\
You have {each[5]} appointments scheduled {session} at the {each[3]} on {each[1]}.\n\
The first appointment is at {each[6]}'))
            row_count += 1