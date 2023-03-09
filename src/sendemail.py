#!/usr/bin/python
# -*-coding:UTF-8-*-

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import smtplib
import json


def send_email(email, password, recipient_email,
               subject, body, file):

    # sent email
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Add attachment
    with open(file, 'rb') as f:
        attachment = MIMEApplication(f.read(),
                                     _subtype='pdf')
        attachment.add_header('Content-Disposition',
                              'attachment',
                              filename=file.split('/')[-1])
        msg.attach(attachment)

    # connect server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)

    # sent email
    server.sendmail(email, recipient_email,
                    msg.as_string())

    # close server
    server.quit()


def run_sent(file):

    # Open need data
    with open('./setting/set.json', 'r',
              encoding='utf-8') as f:
        # Load the JSON data from the file
        set_file = json.load(f)

    c_info = pd.read_csv('./setting/company_info.csv',
                         encoding='cp950', dtype=str)

    # now info
    id_code = file.split('/')[-1].split('.')[0]
    c_info_n = c_info[c_info['id'] == id_code]

    if c_info_n.shape[0] != 1:
        msg = 'ID not found or multiple IDs found'
    else:
        email_n = c_info_n.email.to_list()[0]
        recipient_n = c_info_n.recipient.to_list()[0]
        body_n = set_file['body'].split('<body>')
        body_n[1] = '<p>' + recipient_n + ' 您好</p>' + \
                    body_n[1]
        body_n = '<body>'.join(body_n)
        send_email(email=set_file['email'],
                   password=set_file['password'],
                   recipient_email=email_n,
                   subject=set_file['subject'],
                   body=body_n,
                   file=file)
        msg = 'Email sent successfully'

    return id_code + ' : ' + msg


if __name__ == '__main__':

    msg1 = run_sent(file='C:/Users/wang/Desktop/123456.pdf')
    print(msg1)

