"""
Example of function that will communicate with the microservices 
architecture.
"""
import time
import json

def get_rates():
    """Function sends request and receives data from microservice."""
    # Send Request
    print("Sending Request")
    with open("pipe.txt", "w") as file:
        file.write("Get Rates")

    # Wait for Response with file name
    received = False
    while not received:
        with open("pipe.txt", "r") as file:
            line = file.read()
            time.sleep(.1)
            if line[:3] == "Get":
                print( "waiting...")
                time.sleep(.1)
            else:
                file_name = line
                print("File Received")
                received = True

    # Process File
    with open(file_name, 'r') as infile:
        rate_data = json.load(infile)
    
    # Clear out pipe and return data to main program
    with open("pipe.txt", "w") as file:
        file.write("")
        file.close()

    return rate_data
