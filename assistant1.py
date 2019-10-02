import pyttsx3
import datetime
import sp_recog as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<18:
		speak("Good Morning!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon!")
	else:
		speak("Good Evening")
	speak("I am deadpool .Please tell me how may I serve you : ")

def takeCommand():
	#it takes microphone input from the user and returns string

	r=sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening..............')
		r.pause_threhold=1
		audio=r.listen(source)
	try:
		print("Recognizing............")
		query=r.recognize_google(audio,language='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)

		print("Say that again please...")
		return "None"
	return query

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('Email Id','Password')
	server.sendmail('Email Id',to,content)
	server.close()






if __name__=="__main__":
	speak(" vishal dut urf BABA)
	wishMe()
	while True:

		# Logic foe executing tasks based on query

		query=takeCommand().lower()
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query=query.replace("wikipedia","")
			results =wikipedia.summary(query, sentences=2)
			speak("Acccording to Wikipedia")
			print(results)
			speak(results)
		elif 'open youtube' in query:
			webbrowser.open('youtube.com')

		elif 'open google' in query:
			webbrowser.open('google.com')
		elif 'open stackoverflow' in query:
			webbrowser.open('stackoverflow.com')
		elif 'play music' in query:
			music_dir='E:\\punjabi songs'
			songs=os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs))]))
		elif 'exit' in query:
			break
		elif 'time' in query:
			strTime= datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir,the time is{strTime}")

		elif 'open code' in query:
			codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(codePath)

		elif 'email to chetan ' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to="chetan.shm98@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("sorry sir , i am not able to send this Email")

		# else:
		# 	speak("you said")
		# 	speak(query)
		# 	speak("say that again")

