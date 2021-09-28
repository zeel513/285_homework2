from datetime import datetime
import yfinance as yf

def main():
    now = datetime.now()
    choice='y'

    while choice=='y'or choice=='Y':
        print("Please enter a symbol :")
        symbol = input()
        print("Output:")
        companyInfo = yf.Ticker(symbol)
        if companyInfo.history(period="max").empty is False:
            companyName=companyInfo.info['longName']
            twoDaysData = round(companyInfo.history(period='2d'),2)
            yesterdayPrice=twoDaysData['Close'][0]
            todaysPrice=twoDaysData['Close'][1]
            valueChange=round(todaysPrice-yesterdayPrice,2)
            percentChange=round((valueChange/yesterdayPrice)*100,2)
            print(now.strftime("%c"))
            print(companyName)
            print(twoDaysData['Close'][1],valueChange,"(",percentChange,"%)")
        else:
            print("Invalid symbol\n")
        print("\nDo you want to continue searching (y/n)")
        choice=input()

if __name__ == '__main__':
    main()
    