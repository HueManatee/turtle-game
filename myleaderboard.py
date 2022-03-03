#searches for the score based on where numSearch tells it to look (it looks for commas)
def searchScore(numSearch):
    view = open('a122_leaderboard.txt', 'r')
    text = view.read()
    pos = 0
    numList = [0,1,2,3,4,5,6,7,8,9]
    while(pos <10):
        x = numList[pos]
        if ((text[numSearch+4]==str(x)) and (text[numSearch+4]==str(x))):
            return((int(text[numSearch+2])*100) + (int(text[numSearch+3])*10)) + (int(text[numSearch+4]))
        pos +=1
    pos =0
    while(pos <10):
        x = numList[pos]        
        if((text[numSearch+3])==str(x) and (text[numSearch+3])==str(x)):
            return((int(text[numSearch+2])*10) + (int(text[numSearch+3])))
        pos +=1
    return((int(text[numSearch+2])))
    
#returns index for specified value             
def searchName(nameSearch, numToadd):
    view = open('a122_leaderboard.txt', 'r')
    text = view.read()
    return nameSearch + numToadd
    
#returns value of indices to move based on digits
def digits(numScore):
    if (numScore>=0 and numScore<=9):
        return 2
    elif(numScore>=10 and numScore<=99):
        return 3
    else:
        return 4





#compares the newest score with scores on leaderboard, edits file to show in program
def checkScore(newscore, newname, firstN, firstS, secondN, secondS, thirdN, thirdS, fourthN, fourthS, fifthN, fifthS):
    global scoreList
    if(newscore>firstS):
        fifthN = fourthN
        fifthS = fourthS
        fourthN = thirdN
        fourthS = thirdS
        thirdN = secondN
        thirdS = secondS
        secondN = firstN
        secondS = firstS
        firstN = newname
        firstS = newscore
    elif(newscore>secondS):
        fifthN = fourthN
        fifthS = fourthS
        fourthN = thirdN
        fourthS = thirdS
        thirdN = secondN
        thirdS = secondS
        secondN = newname
        secondS = newscore
    elif(newscore>thirdS):
        fifthN = fourthN
        fifthS = fourthS
        fourthN = thirdN
        fourthS = thirdS
        thirdN = newname
        thirdS = newscore
    elif(newscore>fourthS):
        fifthN = fourthN
        fifthS = fourthS
        fourthN = newname
        fourthS = newscore
    elif(newscore>fifthS):
        fifthN = newname
        fifthS = newscore
    file = open('a122_leaderboard.txt', 'w')    
    file.write('Leaderboard:' + '\n' + firstN + ', ' + str(firstS) + '\n' + secondN + ', ' + str(secondS) + '\n' + thirdN + ', ' + str(thirdS) + '\n' + fourthN + ', ' + str(fourthS) + '\n' + fifthN + ', ' + str(fifthS) + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n' + '\n')
    file.close()
    return True



#appends name and score to the text file
def addScore(name,score):
    view = open('a122_leaderboard.txt', 'r')
    text = view.read()
    #print(text)

    '''searchList = [firstSearch,secondSearch,thirdSearch,fourthSearch,fifthSearch]
    moveIndex = -1
    for search in searchList:
        search = text.find(',', moveIndex+1)
        moveIndex +=1

    for score in searchList:
        score

    for digits in '''
    firstSearch = text.find(',')
    secondSearch = text.find(',', firstSearch+1)
    thirdSearch = text.find(',', secondSearch+1)
    fourthSearch = text.find(',', thirdSearch+1)
    fifthSearch = text.find(',', fourthSearch+1)

    firstScore = searchScore(firstSearch)
    firstDigits = digits(firstScore)

    secondScore = searchScore(secondSearch)
    secondDigits = digits(secondScore)
   
    thirdScore = searchScore(thirdSearch)
    thirdDigits = digits(thirdScore)
    
    fourthScore = searchScore(fourthSearch)
    fourthDigits = digits(fourthScore)

    fifthScore = searchScore(fifthSearch)

    #print(firstScore)
    #print(secondScore)
    #print(thirdScore)
    #print(fourthScore)
    #print(fifthScore)
    
    name1Start = text.find(':')
    name1End = text.find(str(firstScore))
    
    name2End = text.find(str(secondScore))

    name3End = text.find(str(thirdScore))

    name4End = text.find(str(fourthScore))

    nameSearch2 = text.find(',', firstSearch+1)
    nameSearch3 = text.find(',', secondSearch+1)
    nameSearch4 = text.find(',', thirdSearch+1)
    nameSearch5 = text.find(',', fourthSearch+1)

    #First Name
    firstName = text[searchName(name1Start, 2):(searchName(name1End, -2))]
    #Second Name
    secondName = text[searchName(name1End, firstDigits):(searchName(nameSearch2, 0))]
    #Third name
    thirdName = text[searchName(name2End, secondDigits):(searchName(nameSearch3, 0))]
    #Fourth Name
    fourthName = text[searchName(name3End, thirdDigits):(searchName(nameSearch4, 0))]
    #Fifth Name
    fifthName = text[searchName(name4End, fourthDigits):(searchName(nameSearch5, 0))]
    
    checkScore(score, name, firstName, firstScore , secondName, secondScore, thirdName, thirdScore, fourthName, fourthScore, fifthName, fifthScore)
    file = open('a122_leaderboard.txt', 'r')
    text = file.read()
    return text