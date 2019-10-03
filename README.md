# Bank_Credit_Score
Data Science PROJECT 
Client: Bank GoodCredit | Category: Banking - Risk 
This project contains only brief information of the project for more information E-mail me @ http://srikantvaijapur@gmail.com
Business Case: 
 Bank wants to predict credit score for current credit card customers. The credit score will denote a customer’s credit worthiness and help the bank in reducing credit default risk. 
 Target variable → 
 Bad_label:
 0 –  Customer has Good credit history
 1 –  Customer has Bad credit history  
ASSUMPTIONS:
Provided Data set is imbalanced
Existing Data set:
Client provided Customer accnt , Enquiery Details , Customer_Demographics
	-Bussiness requirement wants to predict the Target variable wheather the customer has Good credit history or Bad credit history  
Steps to predict the Good or Bad credit history:
Data set is provided by SQL server with USERNAME<PASSWORD<HOST<PORT by the clint.
Step 1:
	import the data set to jupiter  and convert it to CSV file.so that it will become convinent to analyze the data.
Step 2: 
	After converting to csv , open the fie in xl-sheet or in Tableau
Step 3:
	Analyze the data clenly and amke out your seperate table to take into consideration
DATA CLEANING & DATA MINING (in brief)
1.Read the CSV_file
2.Remove the irrelevant columns
3.Replace the data with ['?','*','$',' ','  ',''] with Nan
4.Drop the duplicate columns
Enquiery File Transform(Data Mining)
1.Read the CSV of cust_enquiery
2.Take relevant columns 
3.Add one more column of enq_eqn_amt(which add the no of transction made by every single customer)
4.Groupby customer_no(which is included in all 3 dataset)
5.join the customer_no and df_amt,df_count
6.save the file
Account File Transformation
1.Read the file
2.Take the relevant columns
3.fill NaN with '0'
4.Group by Customer_no
5.Save the file
 > JOINING THE DATA
1.join all the 3 files with left join
Processing the Data
1.Convet the categorical data to numerical data by label Encoder 
2.Take Bad_label as Target Variable/Dependent Variable
3.Other columns are independent Variable
4.Train & test the Data from sklearn.model_selection
Applying ML algorithm
	Fit the model with Random Forest algorithm and after traing with Random Forest, find out accuracy and y_predict
Plot the Graph
	plot the graph with feature importance and with independent Variables
Result:
Achived 96.13% accuracy by Random Forest model fit method
Tools Used:
1.Sql server
2.Excel
3.Jupyter
4.ML Algorithm
