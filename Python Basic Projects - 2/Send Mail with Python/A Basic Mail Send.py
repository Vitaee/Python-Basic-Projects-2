import smtplib


content = "word,sentence etc."

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.ehlo()

mail.starttls()

mail.login("your gmail","password")

mail.sendmail("your gmail","friend's gmail",content)
