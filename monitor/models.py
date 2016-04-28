from __future__ import unicode_literals
from django.db import models

from django.utils import timezone

from os import environ
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate
from email.mime.text import MIMEText

# Create your models here (basically database tables).

class Computer(models.Model):
	computer_name = models.CharField(max_length=100, primary_key=True)
	ip = models.CharField(max_length=25)
	activity = models.DateTimeField('latest activity')
	email_sent = models.BooleanField(default=True)

	def __str__(self):
		return self.computer_name

	def sendMail(self, eto='j.bang@unsw.edu.au', efrom=u'python.error@gmail.com', esubject=u'One of the workers is ill', mess='', csvPath = None, csvName = None):
		
		#login
		smtp_user = environ['PYTHON_MAIL_USER']
		smtp_pwd = environ['PYTHON_MAIL_PASS']
		smtp_port = 587
		smtp_host = 'smtp.gmail.com'
		smtpserver = smtplib.SMTP(smtp_host, smtp_port)	
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo
		smtpserver.login(smtp_user, smtp_pwd)

		#make email
		msg = MIMEMultipart()
		msg['From'] = efrom
		msg['To'] = eto
		msg['Subject'] = esubject
		msg['Date'] = formatdate(localtime = True)
		msg.attach(MIMEText(mess))
		if csvName is not None:
			with open(csvPath + csvName, 'rb') as inFile:
				csvText = ''.join(inFile.readlines())
			csvAtt = MIMEText(csvText, 'csv')
			csvAtt.add_header('Content-Disposition', 'attachment', filename = csvName)
			msg.attach(csvAtt)

		#send it
		smtpserver.sendmail(efrom, eto, msg.as_string())
		smtpserver.close()
		return True    


	def isAlive(self):
		alive = (timezone.now() - self.activity < timezone.timedelta(minutes=10))
		if alive:
			self.email_sent = False
		else:
			txt = self.computer_name + ' appears to be offline.'
			self.sendMail(mess=txt, esubject=txt)
			self.email_sent = True
		return alive


#class Activity(models.Model):
	#computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
	#activity = models.DateTimeField('accessed jefit')

	#def __str__(self):
		#return str(self.activity)

	#def isAlive(self):
		#return self.activity >= timezone.now() - datetime.timedelta(minutes=5)