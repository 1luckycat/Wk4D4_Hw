# The championship round of matches is over. Hooray!

# We have diligently recorded all of the results of the matches in an array of tuples. The first
# value in the tuple represents that teams score, the second value in the tuple represents their oponents.
# We need you to build a function to help us determine if that team has won or not. Return True if
# the # of matches that they won is more than they have lost, False otherwise.


# Examples
# Input = [(5,3), (10,7), (2,8), (3,3), (4,1)]
# Output = True 
# Explanation = The team won their 1st, 2nd and last match (for a total of 3 wins) and only lost the 3rd.


# Input = [(1,3), (5,7), (8,4)]
# Output = False
# Explanation = The team lost their first two matches and only won their 3rd and final match. 


def champ(tup):
    win = 0
    lose = 0
    
    for i in tup:
        if i[0] > i[1]:
            win += 1
            print("Win: ", {win})

        elif i[0] < i[1]:
            lose += 1
            print("Loses:", {lose})

    if win > lose:
        return True
    else:
        return False
            


print(champ([(1,1), (5,5), (8,8), (3, 2)]))


# Alex H's answer
def did_i_win(matches):
    ## debug
    win = sum(map(lambda x: x[0] > x[1], matches))
    lose = sum(map(lambda x: x[0] < x[1], matches))
    print(win, lose)
    ## function
    result = sum(map(lambda x: x[0] > x[1], matches)) - sum(map(lambda x: x[0] < x[1], matches))
    return result > 0

print(did_i_win([(1,1), (5,5), (8,8), (3, 2)]))