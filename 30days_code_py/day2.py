'''
Input Format

There are lines of numeric input:
The first line has a double, (the cost of the meal before tax and tip).
The second line has an integer, (the percentage of being added as tip).
The third line has an integer, (the percentage of being added as tax).

Output Format

Print The total meal cost is totalCost dollars., where is the rounded integer
result of the entire bill ( with added tax and tip).

Sample Input

12.00
20
8

Sample Output

The total meal cost is 15 dollars.
'''
meal_price = float(input())
tip_percent = int(input())
tax_percent = int(input())

total = meal_price * (1 + (tip_percent + tax_percent) * 0.01)
print('The total meal cost is {0:d} dollars.'.format(round(total)))
