import smtplib
import random
import subprocess
import os
import playsound # type: ignore
from . import error
from typing import List, Union


def sendEmail(sendAddr: str, password: str, recvAddr: str, body: str, server: str, port: int, sub: str = 'No Subject') -> bool:
    with smtplib.SMTP(server, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(sendAddr, password)

        subMsg: str = 'Subject: {}'.format(sub)
        bodyMsg: str = '\n\n {}'.format(body)

        finalMsg: str = subMsg + bodyMsg

        smtp.sendmail(sendAddr, recvAddr, finalMsg)
        return True


def emailAddressSlicer(fullAddr: str) -> tuple:
    splitList: List[str] = fullAddr.split('@')
    username: str = splitList[0]
    domain: str = splitList[1]
    return (username, domain)

def rollDice(dice1=True):
    if dice1 == True:
        rolls: List[int] = [1, 2, 3, 4, 5, 6]
        return random.choice(rolls)
    else:
        rolls: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        return random.choice(rolls)


def timer(seconds: int, audioFile: str):
    time: int = seconds
    for i in range(0, seconds):
        if time <= 0:
            playsound.playsound(audioFile)
        time: int = time - 1

def startApp(exePath: str):
    command: str = exePath
    if subprocess.run(command, shell=True):
        return True
    else:
        raise error.startAppFailedError
