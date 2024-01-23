import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import openpyxl
#!pip install openpyxl
# Function to send email
def send_email(to_address, to_name, company_name):
    # Your email credentials and SMTP server information
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = ' ' # your email goes here
    password = ' ' # your application password here

    

   # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = to_address
    msg['Subject'] = 'Exploring Job Opportunity'

    # Customize the email body with the recipient's name and company name
    body = f"Dear {to_name},\n\n" \
           f"I trust this email finds you well.\n\n" \
           f"I am reaching out to express my interest in potential opportunities at {company_name}. " \
           f"With my background in this industry, I am confident in my ability to bring valuable insights and contribute " \
           f"to your team's success.\n\n" \
           f"I would welcome the chance to discuss how my skills align with the goals of {company_name}.\n\n" \
           f"Thank you for your time, and I look forward to the possibility of connecting.\n\n" \
           f"Best regards,\n" \
           f"XYZ\n" \
           f"Ph: 1234567\n" \
           f"{username}"

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    
    # Add attachment
    attachment_path = ''# your resume path here
    attachment_filename = '' #resume namme here
    
    with open(attachment_path, 'rb') as attachment:
        part = MIMEApplication(attachment.read(), Name=attachment_filename)
        part['Content-Disposition'] = f'attachment; filename="{attachment_filename}"'
        msg.attach(part)
    

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to_address, msg.as_string())

excel_file_path = '' #path to your excel sheet
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

for row in sheet.iter_rows(min_row=2, values_only=True):
    print(row)
    email, name, company = row
    # Send email
    send_email(email, name, company)
