def matchi(trablo):
    teams, score = trablo.split(' ')
    team1, team2 = teams.split('-')
    score1, score2 = map(int, score.split(':'))

    if score1 > score2:
        return team1
    elif score1 < score2:
        return team2
    else:
        return "Ничья"

game = input("введи команды и счет:")
print(matchi(game)) 

