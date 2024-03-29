# log-analysis
Reporting tool using Python to connect to the "news" Postgres database to display query results in a plain text format using the psycopg2 module. 

### Objective
Three questions to answer:
1. What are the top 3 articles based on page views?
2. Who are the most popular authors based on page views of across all articles?
3. Which days had request error greater then 1% based on HTTP status code?

### Prerequesites
* VirtualBox
* Vagrant
* Python3

### Structure
The ```python3 jb-log-analysis.py``` imports the psycopg2 module to connect to the postgres database. Three separate queries extract the data from the articles, authours, and log tables in the news database. The script then prints the results of those queries to a text file named **results.txt**. The results of the queries are in the order of the questions.

### Instructions
In terminal run the following commands:
1. ```vagrant up```
2. ```vagrant ssh```
3. ```cd /vagrant```
4. ```git clone https://github.com/jbacon24/log-analysis.git```
5. ```cd log-analysis```
6. ```python3 jb_logs_analysis.py```
