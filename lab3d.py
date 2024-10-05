#!/usr/bin/env python3

'''Lab 3 Inv 2: Using os and subprocess modules'''

# Author ID: [124876228]



import os

import subprocess



# Testing os.system()

print("Testing os.system():")

os.system('ls')

os.system('whoami')

os.system('ifconfig')



ls_return = os.system('ls')

print('The contents of ls_return:', ls_return)

whoami_return = os.system('whoami')

print('The contents of whoami_return:', whoami_return)

ifconfig_return = os.system('ifconfig')

print('The contents of ifconfig_return:', ifconfig_return)



# Testing an invalid command

ipconfig_return = os.system('ipconfig')

print('The contents of ipconfig_return:', ipconfig_return)



# Testing os.popen()

print("\nTesting os.popen():")

ls_return = os.popen('ls')

print('The contents of ls_return:', ls_return)



whoami_return = os.popen('whoami')

print('The contents of whoami_return:', whoami_return)



ifconfig_return = os.popen('ifconfig')

print('The contents of ifconfig_return:', ifconfig_return)



whoami_return = os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:', whoami_contents)

ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:', ipconfig_contents)

# Using subprocess.Popen()
print("\nUsing subprocess.Popen():")
p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = p.communicate()
print(output)
print(output[0])

# Convert stdout to a string and strip off the newline characters
stdout = output[0].decode('utf-8').strip()
print(stdout)

# Defining the free_space function
def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print("\nFree space on root directory:")
    print(free_space())
