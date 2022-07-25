# CS361-Mortgage-Microservice

### Description
This microservice is a web scraper that will grab up-to-date mortgage interest rates from the Internet to be used in my partner Josh's individual project.

## File Descriptions

**main.py**

An example of my partner's main program making a function call to the microservice to begin scraping.  By the end, the program will receive the data in the form of a dictionary that can be used by the rest of the program.

**get_rates.py**

An example function that would be called by the main program.  The function sends a request to the microservice via the communication pipeline.  The function receives the file location of the data from the microservice via the communication pipe, opens the JSON file, and finally returns a dictionary object to the main program.

##### Requesting Data

##### Receiving Data

**mortgageratesscrapermain.py**

The microservice is "listening" for the command to start scraping from the pipe.txt file.  Once it sees the code word to start, the microservice uses Beautiful Soup 4 to scrape information from bankrate.com about mortgage products of various lengths, as well as both purchase and refinance options.  It places this information into a nested dictionary and writes the dictionary to a JSON file.  Finally, the microservice writes the file name of the json file to the communication pipe so that the main program can retrieve the data.

**pipe.txt**

We are using a simple txt file communication pipeline between our main program and the microservice.  The txt file will be updated with a command to the microservice to start and then the microservice will update the txt pipeline with the file name of the generated data.  Finally, the txt file will be cleared so it can be used the next time.

**rate_data.json**

An example generated data set showing what the scraped data looks like.

**requirements.txt**

Contains the installation requirements to make the microservice work in python.

## UML Sequence Diagram



## Video Demonstration

