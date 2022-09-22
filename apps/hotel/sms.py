from twilio.rest import Client

account_sid = 'ACe60c92f4f7dc22c0473b15629e727485'
auth_token = '05c9126bb89bdffc785f61d02656ef93'

client = Client(account_sid, auth_token)


message = client.messages.create(
    from_="+17078756100",
    body = "Dios siempre esta conmigo",
    to = '+584121419422',
)

print(message.body)



"""gqwOcu2zd-YwL33fEaMnPg5PdXvZ85W_KQuD1ZdJ"""