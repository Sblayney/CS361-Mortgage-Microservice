# CS361-Mortgage-Microservice

### Description
This microservice is a web scraper that will grab up-to-date mortgage interest rates from the Internet to be used in my partner Josh's individual project.

## File Descriptions

**main.py**

An example of my partner's main program making a function call to the microservice to begin scraping.  By the end, the program will receive the data in the form of a dictionary that can be used by the rest of the program.

**get_rates.py**

An example function that would be called by the main program.  The function sends a request to the microservice via the communication pipeline.  The function receives the file location of the data from the microservice via the communication pipe, opens the JSON file, and finally returns a dictionary object to the main program.

##### Requesting Data

To request data from the web scraper microservice, a function (in this case getrates()) opens up the pipe.txt file and writes "Get Rates" in it.  The microservice will be "listening" for that phrase to be written in the pipe and once it sees it, it will start and retrieve data on mortgage interest rates for various products from bankrate.com

```python
def get_rates():
    """Function sends request and receives data from microservice."""
    # Send Request
    print("Sending Request")
    with open("pipe.txt", "w") as file:
        file.write("Get Rates")
```

##### Receiving Data

Once the microservice sees the call from the communication pipe, it parses data from bankrate.com using Beautiful Soup.  The data is then selectively grabbed depending on what information is needed and how it is formatted in html and is placed in a dictionary.  The dictionary is exported as a json file and the microservice returns the filename of the json file to the pipe text file.  The main program or function that originally called the microservice can then open the json file and import the information as a dictionary.

**mortgageratesscrapermain.py**

The microservice is "listening" for the command to start scraping from the pipe.txt file.  Once it sees the code word to start, the microservice uses Beautiful Soup 4 to scrape information from bankrate.com about mortgage products of various lengths, as well as both purchase and refinance options.  It places this information into a nested dictionary and writes the dictionary to a JSON file.  Finally, the microservice writes the file name of the json file to the communication pipe so that the main program can retrieve the data.

**pipe.txt**

We are using a simple txt file communication pipeline between our main program and the microservice.  The txt file will be updated with a command to the microservice to start and then the microservice will update the txt pipeline with the file name of the generated data.  Finally, the txt file will be cleared so it can be used the next time.

**rate_data.json**

An example generated data set showing what the scraped data looks like.

**requirements.txt**

Contains the installation requirements to make the microservice work in python.

## UML Sequence Diagram

![UML](https://user-images.githubusercontent.com/86209705/180905419-235890b8-3aba-45ed-91f1-b81a9b2c0d0b.PNG)

## Video Demonstration

https://media.oregonstate.edu/media/t/1_wiyvdvti
