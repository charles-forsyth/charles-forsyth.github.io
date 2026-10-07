#!/usr/bin/env python


import subprocess                                   `#importing the subprocess module

subprocess.call(['top'])                             #calling external command top
subprocess.call(['ls','-latr'])                      #calling external command ls -latr
subprocess.call(['./dictionary-type-variables.py'])  #calling other python script in same folder
