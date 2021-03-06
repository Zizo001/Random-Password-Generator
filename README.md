# Random Password Generator
## Table of Contents
* [Overview](#overview)
* [Getting Started](#getting-started)
* [Demo](#demo)
* [Stretch Goal](#stretch-goal)

## Overview
Simple password generator written in python. This program is ideally used as a quick method to generate passwords to use when creating accounts, as well as adding them to a file such as a password vault or a text file (please don't use a text file). It is text based so it can be run on any machine. The characters generated are universally valid for account creation on most websites and should work normally.

The password generated consists of the following:

A-Z

a-z

1-9

!@#$%^&*()_+-={}[].,\<>?"':;

## Getting Started
The only prerequisite to run this is to have python installed. We can check if python is installed using either of the following commands:
```
python --version
python3 --version
```
If python is not installed, then this can easily be done using the installer found on https://www.python.org/downloads/

You can also install it via the command line on Mac OS/Linux using the following command:

```
$ sudo apt-get update
$ sudo apt-get install python3.9
```
To run the program, navigate to the file's directory and run the following command:
```
python RandomPasswordGenerator.py
```

## Demo
When the program is ran, a prompt will greet the user and ask for the length of the password as shown below:

![Initial](https://user-images.githubusercontent.com/54548478/123335250-0c1b6800-d4f9-11eb-8d43-b79432dff8c8.PNG)

The user inputs their desired length and the password is then generated and copied to the clipboard

![Output](https://user-images.githubusercontent.com/54548478/123335249-0c1b6800-d4f9-11eb-9918-9c158dc9b1b9.PNG)

## Stretch Goal
One feature I might implement is to have a password locker (as an excel sheet) be generated. The program will then store the password and other information such as usernames in the excel sheet. I do understand that some users will want a simple password generator, so I will likely include both versions.
