#if you want to send sms to a number, first add it into twilio (only for trial accounts) , later you can send sms to any number without entering it. 
#edit the senders email id,password , account_sid and auth_token in other.py file
#OTPgenerator generates OTP , this is used in OTP_email and OTP_phone.
#

import smtplib
from twilio.rest import Client
from email.message import EmailMessage
import math
import random

from other import user_email_id,user_pwd,account_sid,auth_token,from_phone,nums



client=Client(account_sid,auth_token)

def OTP_generator():                 #this is faster but IS GIVING AN ERROR SO IGNORE FOR NOW
    digits = "123456789"             #i will work on this for now , ignore this one
    OTP = ""                       

    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def OTPgenerator():                 #selects a random number from a list(nums) in other.py file
    otp=random.choice(nums)         #this method will be used only for testing purposes.
    return otp

def OTP_email():
    email_input=input("Enter Email ID:")
    usr_mail=user_email_id          #the account which sends OTP , edit values in other.py
    usr_pwd=user_pwd                # "" password, edit values in other.py
    otp=OTPgenerator()
    content='Hello Use This OTP to sign in to your SS RPA account! Do not Share this code: '+str(otp)

    
    msg=EmailMessage()
    msg['Subject']='OTP Verification For SS RPA Login.'
    msg['From']=usr_mail
    msg['To']=email_input
    msg.set_content(content)

    with smtplib.SMTP('smtp.gmail.com',587) as smtp:    #make sure to enable "less secure apps" on google before sending (not recievig) mail , link:https://myaccount.google.com/lesssecureapps
       smtp.ehlo()
       smtp.starttls()
       smtp.ehlo()

       smtp.login(usr_mail,usr_pwd)
       smtp.send_message(msg)
    print("Enter OTP sent to your mail id:")
    num_input=input()
    if num_input==otp:
      print("Successfull")       #if otp matches then "do something"
    else:
      print("Unsuccessful Attempt") # if not then "do something else"

def OTP_phone():
    phone_num=input("Enter your Phone number(For India Only):")
    phone_number='+91' + str(phone_num)                    #right now, for indian numbers only
    otp=OTPgenerator()
    msg='Your One Time Password(OTP) for SS RPA is:' +str(otp) +' Do Not Share This Code!'
    message=client.messages \
             .create(
                 body=msg,
                 from_=str(from_phone),
                 status_callback='http://postb.in/1234abcd', #you can use this too maybe(?)
                 to=str(phone_number)
                 )
    print("Enter OTP here:")
    a=str(input())
    if a== str(otp):
        print("Successfull")
    else:
        print("Unsuccessfull")






