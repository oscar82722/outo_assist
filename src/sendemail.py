#!/usr/bin/python
# -*-coding:UTF-8-*-

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import csv


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

    with open('./setting/company_info.csv', 'r') as f:
        my_reader = csv.reader(f, delimiter=',')
        company_id, company_email, company_name = zip(
            *my_reader)

    # now info
    id_code = file.split('/')[-1].split('.')[0]
    indices = [index for index, value in
               enumerate(company_id) if
               value == id_code]

    if len(indices) == 0:
        msg = 'ID not found in company_info.csv'
    else:
        email_success = list()
        for i in indices:
            email_n = company_email[i]
            recipient_n = company_name[i]
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
            email_success = email_success + [email_n]

        msg = 'Email sent successfully(' + \
              ' , '.join(email_success) + ')'

    return id_code + ' : ' + msg


if __name__ == '__main__':
    msg1 = run_sent(
        file='C:/Users/wang/Desktop/123456.pdf')
    print(msg1)

