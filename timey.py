import csv
from datetime import datetime, timedelta


from collections import defaultdict

taskDurations = defaultdict(timedelta)
startTime = ""
stopTime = ""
currentTask = ""

def calculateDifference():
    return stopTime - startTime

def parseDuration(time_str):
    return datetime.strptime(time_str, "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")

def startEntry(newTask):
    global currentTask
    global startTime
    startTime = datetime.now().replace(microsecond=0) 
    currentTask = newTask


def stopEntry():
    global stopTime
    stopTime = datetime.now().replace(microsecond=0)


def saveEntry():
    newEntry = [str(startTime), str(stopTime), currentTask, calculateDifference()]
    with open('togglsucks.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(newEntry)
    
    print("You've spend", calculateDifference(), "on", currentTask)


def daySummary():
    global taskDurations
    with open('togglsucks.csv', 'r') as file:
        datareader = csv.reader(file)
        for row in datareader:
            task = row[2]
            duration = parseDuration(row[3])
            taskDurations[task] += duration
import csv
from datetime import datetime, timedelta


from collections import defaultdict

taskDurations = defaultdict(timedelta)
startTime = ""
stopTime = ""
currentTask = ""

def calculateDifference():
    return stopTime - startTime

def parseDuration(time_str):
    return datetime.strptime(time_str, "%H:%M:%S") - datetime.strptime("00:00:00", "%H:%M:%S")

def startEntry(newTask):
    global currentTask
    global startTime
    startTime = datetime.datetime.now().replace(microsecond=0) 
    currentTask = newTask


def stopEntry():
    global stopTime
    stopTime = datetime.datetime.now().replace(microsecond=0)


def saveEntry():
    newEntry = [str(startTime), str(stopTime), currentTask, calculateDifference()]
    with open('togglsucks.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(newEntry)
    
    print("You've spend", calculateDifference(), "on", currentTask)


def daySummary():
    global taskDurations
    with open('togglsucks.csv', 'r') as file:
        datareader = csv.reader(file)
        for row in datareader:
            task = row[2]
            duration = parseDuration(row[3])
            taskDurations[task] += duration
    
    for task, total_duration in taskDurations.items():
        print(f"{task}: {total_duration}")

def getCommand(command):
    if (command == "start"):
        newTask = input("Task:")
        startEntry(newTask)
    
    elif (command == "stop"):
        stopEntry()

    elif (command == "save"):
        saveEntry()
    
    elif (command == "sum"):
        daySummary()


while True:
    command = input("$:")
    getCommand(command)
    
    for task, total_duration in taskDurations.items():
        print(f"{task}: {total_duration}")

def getCommand(command):
    global A
    if (command == "start"):
        newTask = input("Task:")
        startEntry(newTask)
    
    elif (command == "stop"):
        stopEntry()

    elif (command == "save"):
        saveEntry()
    
    elif (command == "sum"):
        daySummary()
    
    elif (command == "quit"):
       A = False

A = True
while A:
    
    command = input("$:")
    getCommand(command)
