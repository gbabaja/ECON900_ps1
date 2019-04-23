# ECON900_ps1
MACHINE LEARNING AND BIG DATA 
	This project consists of two primary parts: (1) webscraping and (2) machine learning exercise. 

(1) WebScraping
	This part of the project is designed to collect data by scraping www.boardgamegeek.com website in two steps.  The first step will request the html of the website using python (see requesthtml_gb.py file).  The second step will will parse the data in the collected html files (see parsehtml_gb.py file).

(2) Machine Learning Exercise
	This part of the project will perform machine learning using collected data in the first part.


GETTING STARTED:

(1) WebScraping
The goal of this part of the exercise is to collect data on name, ratings, voter number, and prices of all boardgames on www.boardgamegeek.com.
	
	1.A Requesting HTML
		The first step of scraping data will require using Selenium because data on prices are added to the page via JavaScript.  Use file named requesthtml_gb.py for this step.  You will need to install Selenium and an appropriate webdriver before starting the exercise. You will also need to import selenium webdriver, keys, os, and time.

		We will need to create a directory (i.e. a folder) for the html files that will be saved. Next, a loop requesting html of each page is created. Note, it is essential to allow some time for the page to fully load (in thise examle time sleep is 60 seconds) and allow some time before navigating to the next page (I chose to put 60 seconds once again).

		The final outcome of this step should be 1062 html files of pages from www.boardgamegeek.com saved in the html_files folder in the selected directory.
	
	1.B Parsing HTML files
		The second step of webscraping will use parsehtml_gb.py file.  You will need to install BeautifulSoup and Pandas for this step and import all appropriate modules. 

		The goal of this part of Webscraping exercise is to extract data on name, ratings, voter number, and prices in the html files.  This step will require some knowledge of the html structure and how to properly search for and extract desired piece of information.  

		The codes for parsing consists of loops.  The first loop is for navigating into desired file. Moreover, because desired information is presented in the table format, we will also determine number of rows in the given html in the same loop. Next loop (i.e. the loop within the first one) allows us to navigate to the exact piece of information that we need in the given row.  Finally, within the row we will try to extract the information. This step could be tricky since some strings will not have any information which may cause the program to erorr out. To avoid "nonetype" related errors, we will put conditions in place: (1) the first condition lets the program to keep running even if it encounters emty strings (in this case a "missed" data point will be recorded in the dataframe), and (2) the second condtion will record the information when it is available in the html.

		Finally, extracted information will be appended to dataframe using pandas and eventually saved into a csv file.
		The final outcome of this step should be a boardgamegeek_dataset.csv (a csv file) which will be located in the parsed_files folder in the selected directory.
		

(2) Machine Learning Exercise
	Machine learning exercise part of the project will refer to the file named machine_learning.py.  You need to install all indicated packages for this file to work.  Specifically, pandas to be ale to work with dataframe, seaborn and matplotlib for plots/graphs, as well as SVC, svm, confustion matrix, classification report, Standard Scaler, train test split, Kmeans, Gaussian Mixture, and metrics from the Scikit-learn software machine learning library.


	For the machine learning exercise, we will try to predict which category the game belongs to. To achieve this goal, we will be using a classification model to classify the games into “good” vs. “bad” games given some characteristics. Specifically, we will use support vector machines or SVM, which is available in Scikit-learn software machine learning library. We will use SVM’s supervised learning method by classification.


	We will begin by loading collected data using pandas. For this exercise the variables of interest are average rating, number of voters, and board game rank (independent variables) and geek rating (outcome variable). We will classify and label our outcome variable and plot the result to visualize it.  Next, we will define our dependent and independent variables and split them into test and train parts. Finally, we will use SVM classifier to predict "good" and "bad" games. 

	As final steps of the machine learning exercise, we will use classification report and confusion matrix to check the performance of the model and  use KMeans clustering and Gaussian Mixture Models to test if clustering the outcome variables into 2 groups is reasonable.


AUTHOR:
Guncha Babajanova for Econ 900: Machine Learning and Big Data class
Last revised date: April 15, 2019

