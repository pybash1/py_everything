import smtplib
import random
import subprocess
import os
from pytube import YouTube
import playsound
from . import error


def sendEmail(sendAddr, password, recvAddr, body, server, port, sub='No Subject'):
    with smtplib.SMTP(server, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sendAddr, password)

        subMsg = 'Subject: {}'.format(sub)
        bodyMsg = '\n\n {}'.format(body)

        finalMsg = subMsg + bodyMsg

        smtp.sendmail(sendAddr, recvAddr, finalMsg)
        return True


def emailAddressSlicer(fullAddr):
    splitList = fullAddr.split('@')
    username = splitList[0]
    domain = splitList[1]
    return (username, domain)


def ytDownloader(videoUrl, outputPath=str(os.getcwd()), filename='video'): # TODO: [ ] Use output_path and filename
    yt = YouTube(videoUrl)
    if yt.streams.first().download():
        return True
    else:
        return False


def rollDice(dice1=True):
    if dice1 == True:
        rolls = [1, 2, 3, 4, 5, 6]
        return random.choice(rolls)
    else:
        rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        return random.choice(rolls)


def timer(seconds, audioFile):
    time = seconds
    for i in range(0, seconds):
        if time <= 0:
            playsound.playsound(audioFile)
        time = time - 1

def startApp(exePath):
    command = exePath
    if subprocess.run(command, shell=True):
        return True
    else:
        raise error.startAppFailedError
