# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:36:30 2021

@author: swift
"""

import smtplib
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Containment zone alert message"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("cozo.containmentzone@gmail.com", "covid19cozo")
    message  = 'Subject: {}\n\n{}'.format("you are in containment zone", TEXT)
    s.sendmail("cozo.containmentzone@gmail.com", email, message)
    s.quit()