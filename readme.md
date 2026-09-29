# Fraud Email Detector
## Brief Project Description
The email detector helps user in figuring out either the mail is safe or a scam. 

My email detector analyze a list of safe and phishing emails. Once it trained from it can test any new message user want to test. For the training purpose i have used a dataset for better accuracy. 

The result of the tester are showed right on the screen and saves the result in a local database so user can check them again.

## How the detector runs
- first the datset is loaded
- for better accuracy the data is cleaned
- next comes the part of splitting data into two group testing and training.
- Deciding the model and then training the machine learning model.
- Accuracy check.
- here comes the things where the user give the email for testing.
- result either its safe or suspicious.
- result being saved in database.

## Project files

- script.py – the main script in which all the loading training and testing of dataset and email is performed
- security_logs.db – this file stores all tested emails and their results.
- phishing_texts.csv – the dataset which i have used for training the model.

## Requirements

this project i created on python so the user should have python installed. 

## How to Run the detector

1. first open the project folder. 
2. Install all the required libraries by running:
   pip install pandas scikit-learn

## Run the Script

1. Here you need to run python script.py.
2. It will automatically create a database, load the dataset, split, train and all.
3. It will show total number of email the accuracy score and then will ask to enter email for testing.

## Dataset Source

I have used the dataset in this project is:

Name: David-Egea/phishing-texts

SOURCE: https://huggingface.co/datasets/David-Egea/phishing-texts

## Limitations

Currently the detector only works best with complete sentences or full email.It have problem i n in detecting short phrases for example:"hi" it does not provide the model enough info, so they  might not get as accurate a result.

Its a learning project and can not e used for industrial purposes.
