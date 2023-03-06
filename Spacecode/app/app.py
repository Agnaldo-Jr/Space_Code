from flask import Flask, render_template, request, redirect, url_for
import smtplib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_email', methods=['POST'])
def send_email():

    to_address = request.form['to_address']
    subject = request.form['subject']
    message = request.form['message']

    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    email_address = 'yourmail@mail.com'
    password = 'mailpassword'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, password)

    email_message = f"""\
    Subject: {subject}

    {message}
    """
    server.sendmail(email_address, to_address, email_message)
    server.quit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
