import smtplib
main=smtplib.SMTP_SSL('smtp.gmail.com',465)
send='mohamedarsath.v@gmail.com'
pswd='remo1234567'
rec='arsathlakkadi@gmail.com'
msg='hi manchan eppdi iruka nii solu'
main.login(send,pswd)
main.sendmail(send,pswd,rec,msg)
print('mail sent machan')
main.quit()