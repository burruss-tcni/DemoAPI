# importing os module
import os
import sys
     
# Get the current working
# current working directory (CWD)
cwd = os.getcwd()

def lambda_handler(event, context):
    #1 - log the event
    print('\n*************This is the event and info**********\n')
    print(event)
    
    # Print the current working
    # directory (CWD)
    print("Current working directory: ", cwd)
    print('\n*******This is the end of the code info***********\n')
    # print(event)
