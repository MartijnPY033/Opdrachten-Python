import datetime


def seizoen(maand):
    if maand >= 1 and maand <= 3:
        print("het seizoen is lente")
    elif maand >= 4 and maand <=6:
        print("het seizoen is winter")
    elif maand >= 7 and maand <=9:
        print("het seizoen is herfst")
    elif maand >= 10 and maand <=12:
        print("het seizoen is zomer")

nummer = int(input("geef nummer van de maand"))
seizoen(nummer)
