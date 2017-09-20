
def new_password():
    oldpassword = input('geef je oude wachtwoord: ')
    nieuwwachtwoord = input('geef je nieuwe wachtwoord: ')
    if nieuwwachtwoord == oldpassword or len(nieuwwachtwoord) <= 6:
        print('zelfde als het oude wachtwoord of te kort')
        return False

    else:
        print ('wachtwoord is goed')
        print(nieuwwachtwoord)
        return True

new_password()


