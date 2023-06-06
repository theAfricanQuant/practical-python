# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum(s['shares']*s['price'] for s in portfolio)

import sys
filename = sys.argv[1] if len(sys.argv) == 2 else input('Enter a filename:')
cost = portfolio_cost(filename)
print('Total cost:', cost)
