import smtplib

overflow=bool(input())

if overflow ==True:
    sender = 'ap226865@gmail.com'
    receivers = ['emptybindemo@mail.com']
    password="password"
    message ="Alert!!\n The bin at a particular public place is full and has to be collected soon...\n Thank you!"
    try:
        smtpObj = smtplib.SMTP("smtp.gmail.com",int(587))
        smtpObj.starttls()
        smtpObj.login(sender,password)
        smtpObj.sendmail(sender, receivers, message)         
        print("Overflow reported succesfully!")
        
    except Exception as e:
        print("Error: unable to send email : "+str(e))
        

