#!/bin/python3.10 
import requests
import json
import time
import schedule

token = ''
with open('/home/nopo/scripts/git/token.txt', 'r') as file: # put token in file and change the path
    token = file.read().rstrip()
token = "token " + token
prnumbers = []
prnumbers2 = []
headers = ''
username = 'NopoTheGamer'

def getOpenPrs(URL):
    headers = {'Authorization': token, 'accept': 'application/vnd.github.v3+json'}
    r = requests.get(URL, headers=headers)
    data = r.json()
    for x in range(len(data)):
        if data[x]["draft"] is False:
            z = data[x]["number"]
            prnumbers.append(z)
            if getApprovedprs(f"https://api.github.com/repos/notenoughupdates/notenoughupdates/pulls/{str(z)}/reviews",
                              headers):
                prnumbers.remove(prnumbers[x - 1])


def getApprovedprs(URL, headers):
    headers = {'Authorization': token, 'accept': 'application/vnd.github.v3+json'}
    r = requests.get(URL, headers=headers)
    data = r.json()
    for x in range(len(data)):
        if data[x]["state"] == "APPROVED" and data[x]["user"]["login"] == username:
            return True

def getOpenPrsRepo(URL):
    headers = {'Authorization': token, 'accept': 'application/vnd.github.v3+json'}
    r = requests.get(URL, headers=headers)
    data = r.json()
    for x in range(len(data)):
        z = data[x]["number"]
        if data[x]["draft"] is False and z != 660:
            prnumbers2.append(z)
            if getApprovedprsRepo(f"https://api.github.com/repos/notenoughupdates/notenoughupdates-repo/pulls/{str(z)}/reviews",
                              headers):
                prnumbers2.remove(prnumbers2[x - 1])


def getApprovedprsRepo(URL, headers):
    headers = {'Authorization': token, 'accept': 'application/vnd.github.v3+json'}
    r = requests.get(URL, headers=headers)
    data = r.json()
    for x in range(len(data)):
        if data[x]["state"] == "APPROVED" and data[x]["user"]["login"] == username:
            return True


def mainFunc(URL, URL2):
    print("test")
    for x in range(len(prnumbers)):
        prnumbers.remove(prnumbers[x - 1])
    for x in range(len(prnumbers)):
        prnumbers2.remove(prnumbers2[x - 1])
    getOpenPrs(URL)
    getOpenPrsRepo(URL2)

mainFunc("https://api.github.com/repos/notenoughupdates/notenoughupdates/pulls", "https://api.github.com/repos/notenoughupdates/notenoughupdates-repo/pulls")
schedule.every(30).minutes.do(mainFunc, "https://api.github.com/repos/notenoughupdates/notenoughupdates/pulls", "https://api.github.com/repos/notenoughupdates/notenoughupdates-repo/pulls")
while True:
    schedule.run_pending()
    number = len(prnumbers2) + len(prnumbers)
    print(number)
    time.sleep(1860)
