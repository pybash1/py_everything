import smtplib
import random
import subprocess
import os
from pytube import YouTube
import playsound


def sendEmail(send_addr, password, recv_addr, body, server, port, sub='No Subject'):
    with smtplib.SMTP(server, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(send_addr, password)

        sub_msg = 'Subject: {}'.format(sub)
        body_msg = '\n\n {}'.format(body)

        final_msg = sub_msg + body_msg

        smtp.sendmail(send_addr, recv_addr, final_msg)
        return True


def emailAddressSlicer(full_addr):
    splitList = full_addr.split('@')
    username = splitList[0]
    domain = splitList[1]
    return username, domain


def ytDownloader(video_url, output_path=str(os.getcwd()), filename='video'): # TODO: [ ] Use output_path and filename
    yt = YouTube(video_url)
    if yt.streams.first().download():
        return True
    else:
        return False


def rollDice(dice_1=True):
    if dice_1 == True:
        rolls = [1, 2, 3, 4, 5, 6]
        return random.choice(rolls)
    else:
        rolls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        return random.choice(rolls)


def timer(seconds, audio_file):
    time = seconds
    for i in range(0, seconds):
        if time <= 0:
            playsound.playsound(audio_file)
        time = time - 1

def startApp(drive, exe_path): # FIX: Use only 1 parameter, exe_path
    command = drive + ': && ' + exe_path
    if subprocess.run(command, shell=True):
        return True
