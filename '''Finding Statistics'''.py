'''Finding Statistics

Ramesh, the businessman had a list of data containing the overall transactions in a year. He wanted to calculate the statistics of his transactions i.e. calculating mean, median, and variance of his transactions to keep the track of his business growth over the years.

Let's help Ramesh to calculate the mean, median and variance of the list of transactions given by writing code according to his requirements.

Input format:

Input consists of an array containing the overall transactions done in a year.

Output Format:

The output displays the mean, median and standard deviation of the transactions.


Refer the sample Input and Output for formatting specifications

Sample Input and Output:

Enter the transactions done in each month for last year

4545
232
5565
1232
4512
-7878
-9698
-7785
6624
-5757
7597
-774848

Mean : -64638.25
Median : 732.00
Standard Deviation : 214218.97'''


import numpy as np
transactions = []
for i in range(12):
    transaction = float(input())
    transactions.append(transaction)
# Calculate the mean
mean = np.mean(transactions)
# Calculate the median
median = np.median(transactions)
# Calculate the standard deviation
std_dev = np.std(transactions)
# Print the results
print("Enter the transactions done in each month for last year")
print("Mean : {:.2f}".format(mean))
print("Median : {:.2f}".format(median))
print("Standard Deviation : {:.2f}".format(std_dev))


















