# pcost.py

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum(s.cost() for s in portfolio)

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} portfoliofile')
    filename = args[1]
    print('Total cost:', portfolio_cost(filename))

if __name__ == '__main__':
    import sys
    main(sys.argv)
