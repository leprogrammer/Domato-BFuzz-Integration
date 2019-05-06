#!/usr/bin/python

import os
import subprocess
import sys
import psutil
import logging
import time
from generator import generate_samples, createNewLogger


format = logging.Formatter('%(asctime)s - %(levelname)s  -  %(message)s')
#logging.basicConfig(filename='debug.log', level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)s  -  %(message)s')
#logging.info('Beginning of Log')

def runWebTest():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    outputDirectory = "testCase"
    print("Enter the browser type:  \n 1: Chrome \n 2: Firefox \n 3: Internet Explorer")
    browserType = input('>>')
    timeout = input(
        "Duration the browser process should wait before stopping(>=10 seconds to ensure full load of page):")
    browserType = int(browserType)
    checkValidBrowserType(browserType)

    print("Number of files to generate for a test case: ")
    fileCount = input(">>")
    fileCount = int(fileCount)

    print("Number of test cases:")
    testCaseCount = input(">>")
    testCaseCount = int(testCaseCount)

    for x in range(testCaseCount):
        if not os.path.exists(outputDirectory + str(x)):
            os.mkdir(outputDirectory + str(x))

        outfiles = []
        for i in range(fileCount):
            #logging.info('Beginning of Log for fuzz-' + str(i) + '.html')
            outfiles.append(os.path.join(outputDirectory + str(x), 'fuzz-' + str(i) + '.html'))

        generate_samples(dir_path, outfiles)

        for root, folders, fileList in os.walk(outputDirectory + str(x)):
            for fileName in fileList:
                if not fileName.endswith('.html'):
                    continue
                processCommand = getBrowserApplication(browserType)
                if processCommand is not None:
                    setupExploit(dir_path, fileName, processCommand, root)
                    runExploit(processCommand, timeout, os.path.join(outputDirectory + str(x), fileName))
                else:
                    print("Invalid Browser Type")


def runExploit(processCommand, timeout, fileName):
    timeout = int(timeout)
    print("Executing Command: " + " ".join(processCommand))
    process = subprocess.Popen(processCommand, shell=True)
    #print(process.pid)
    #print(psutil.pids())
    
    #Allow time for page to startup
    time.sleep(timeout)

    #Look at page statistics 
    #monitorProcess(process.pid, fileName)

    print("Killing browser process.... bye bye")
    
    if str(processCommand).find("chrome") != -1:
        subprocess.Popen("taskkill /IM chrome.exe" , shell=True)
    elif str(processCommand).find("firefox") != -1:
        subprocess.Popen("taskkill /IM firefox.exe" , shell=True)
    elif str(processCommand).find("iexplore") != -1:
        subprocess.Popen("taskkill /IM iexplore.exe" , shell=True)
    time.sleep(3)


def setupExploit(dir_path, fileName, processCommand, root):
    filePath = os.path.join(dir_path, root, fileName)
    filePath = filePath.replace("//", "////")
    filePath = "file://" + filePath
    print("Testing with exploit:" + filePath)
    processCommand.append(filePath)


def getBrowserApplication(browserType):
    processCommand = ['start']
    if browserType == 1:
        processCommand.append('chrome')
    elif browserType == 2:
        processCommand.append('firefox')
    elif browserType == 3:
        processCommand.append('iexplore')
    else:
        processCommand = None
    return processCommand


def checkValidBrowserType(browserType):
    if browserType not in [1, 2, 3]:
        print("Incorrect option!!")
        sys.exit(0)

def monitorProcess(processID, fileName):
    page = psutil.Process(pid=processID)
    logger = createNewLogger(fileName, fileName + ".log")    

    logger.debug("CPU Util: " + str(page.cpu_percent(interval=1.0)))
    logger.debug("Memory Util: " + str(page.memory_percent()))
    

if __name__ == '__main__':
    runWebTest()