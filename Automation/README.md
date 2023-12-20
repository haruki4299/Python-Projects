# Python-Projects/Automation

Python Scripts related to automating tasks

## sort_desktop.py

Contains two functionalities. 1. moving files in the desktop to a certain folder and 2. deleting all screenshots from desktop. These are two tasks that I found comes up during work and academics. For example, there were many cases where sending a screenshot to a coworker helped communicate the questions I had. In academics, for example, you can have a lot of files with similar naming like 'MPCS 10000 HW1'. At the end of the term or after a test, I may have a lot of these on my desktop and it would help to be able to just say all files with 'HW' in it should be moved to a folder called Homework.

## How To

`cd` in the terminal to the directory containing the script and simply run `python3 sort_desktop.py`. The script will change the working directory to your mac's desktop. You will be asked to choose between different modes.

When choosing mode 2 (file transfer) you can use the text files in the hw directory for testing. Once you choose mode 2, you can enter 'HW' as the common file name attribute and set some random folder name. All files with HW in their file name will be sorted into the folder.
