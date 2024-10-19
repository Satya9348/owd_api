from flask import Flask, render_template_string, send_file
import os
app = Flask(__name__)
# Define the route to display the PDF
@app.route('/pdf/<category>/<id>')
def show_pdf(category, id):
    if category=='All' or id=='All':
        return ''
    else:
        # Define the path to the PDF based on category and id
        file_path = os.path.join('D:/All_projects/PMIS/owd_api/issue', category, id)
        print(os.listdir(file_path)[0])
        pdf_path=os.path.join(file_path,os.listdir(file_path)[0])
        # Check if the file exists
        if os.path.exists(pdf_path):
            # Serve the PDF file
            return send_file(pdf_path, as_attachment=False)
        else:
            return f"PDF not found for category: {category}, id: {id}", 404

if __name__ == '__main__':
    app.run(debug=True)



from flask import Flask, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(order_id,segment,ship_mode):
    subject = 'test'
    body = f'{order_id,segment,ship_mode} has failed'
    to_email = "satya.bisal21@gmail.com"
    from_email = "satyajit.bisal@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    login = "satyajit.bisal@gmail.com"
    password = "lfyh dcud hciq paki"
    # Create the email headers and set the from, to, and subject fields
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    # Attach the email body to the message
    msg.attach(MIMEText(body, 'plain'))
    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS for security
        # Log in to the SMTP server
        server.login(login, password)
        # Send the email
        server.send_message(msg)
        # Close the connection to the SMTP server
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

app = Flask(__name__)

@app.route('/')
def hello_world():
    order_id = request.args.get('order_id')
    segment = request.args.get('segment')
    ship_mode = request.args.get('ship_mode')
    if order_id=='All' or segment=='All' or ship_mode=='All':
        return 'hello'
    else:
        send_mail(order_id,segment,ship_mode)
        return f'The parameter is: {order_id, segment, ship_mode}'

if __name__ == '__main__':
    app.run(debug=True)

