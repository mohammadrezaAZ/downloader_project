import smtplib as smtp
server = smtp.SMTP_SSL('smtp.gmail.com',465)
server.login('mohammadrezaazhideh@gmail.com','a201522221394')
server.sendmail('mohammadrezaazhideh@gmail.com',
                'mohammadreza22217@gmail.com',
                'hello',
                'how are you'
                )
server.quit()                
