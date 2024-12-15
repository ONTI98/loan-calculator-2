
#loan calculator
#Calculator for calculating equal monthly payments
#user gets prompted top insert variables

#variables

L=float(input("Enter total loan amount :"))
i=float(input ("Enter Interest rate (for an interest of 5%, i=0.05) :"))
n=float(input("How many years will it take to pay off the loan? :"))


#will first calculate the total amount needed to be paid over the given number
#of years
 
#formula


A= (L*(1 + i * n))
print ("total amount payable after interest will be {:.2f}". format(A))

#total  amount is A
#fomular for calculating the monthly installments

#n2 should be number of months in the loan duration_
n2=n *12 
monthly_payment= A / n2
print("monthly repayments will amount to {:.2f}" .format(monthly_payment))









    
    

 