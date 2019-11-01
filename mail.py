import smtplib, time

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("facebookalpha9@gmail.com", "fakeaccount")
SUBJECT = "Malicious Activity"
TEXT = "FROM: Lucas Williams, Coursera Curator\nDear Student,\nYour activity has been flagged as malicious by our bots. Please confirm your identity to continue usage.\nRegards,\nTeam Coursera"
msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) 
for i in range (0,5000):
    server.sendmail("facebooklpha9@gmail.com", "anant16129@iiitd.ac.in", msg)
    print ("Success, mail "+str(i+1)+" sent")
    time.sleep(2)
server.quit()
