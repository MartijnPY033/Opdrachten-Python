file = open('ticker', 'r')
tickers = {}

def ticker():
    lines = file.readlines()
    key = [] # bedrijfsnaam
    value = [] # ticker symbool


    for i in lines:
        stript = i.strip('\n')
        sep = stript.split(':')
        key.append(sep[0])
        value.append(sep[1])
    for x in range(len(key)):
        tickers[key[x]] = value[x]
    file.close()
    return tickers




def symbol(tickers):
    ticker()
    user_input = input("Geef een bedrijfsnaam: ")
    if user_input in tickers:
        print ("Symbool voor ", user_input, " is: ", tickers[user_input])
    else:
        print (user_input, " geen geldig bedrijf")

symbol(tickers)
