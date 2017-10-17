import csv


with open('gamers.csv', 'r') as gegevens:
    inlezen = csv.reader(gegevens, delimiter=';')

    for row in inlezen:
        data = str(row[0:3]).split(';')

    def get_score_from_row():
        hoogstescore = data[-1]
        list(hoogstescore)
        return print('De hoogste score is behaald door:', hoogstescore[2:11], 'op:', hoogstescore[15:25], 'score:',
                     hoogstescore[29:31])


get_score_from_row()




