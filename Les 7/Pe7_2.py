def woord():
    while True:
        woord = input('Geef een woord: ')
        proberen = 0
        if len(woord) == 4:
            print (woord + ' heeft ' + str(len(woord)) + ' letters')
            if proberen == 0:
                print('correctie doorgevoerd')
            break
        else:
            print ('Geef een string van vier letters:')






woord()
