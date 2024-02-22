#Georemon Russelraj, U2022586A, MA3#

################################################################################ GRAPHICAL USER INTERFACE ######################################################################
#import Tkinter#
from tkinter import *

#--------------------------------------------------------------------------------------Main Window-----------------------------------------------------------------------------#
# open and set properties of main window #
window = Tk()
window.title('Badminton Ladder Challenge')
window.geometry('500x700')
window.configure(background='black')
pagetitle = Label(window, text='Welcome to the Badminton Ladder Competition!')
pagetitle.config(bg = 'black', fg = 'white', font = 'none 14 bold')
pagetitle.pack()

#-------------------------------------------------------------------------------------Ladder Window----------------------------------------------------------------------------#
# open and set properties of ladder window #
def OpenLadder():                                  
    ladder = Toplevel()
    ladder.title('Ladder')
    ladder.geometry('500x700')
    pagetitle2 = Label(ladder, text = 'Ladder Ranking')
    pagetitle2.config(font = 'none 14 bold')
    pagetitle2.pack()
    ladder1 = open('ladder.txt', 'r')
    # keep track of line number for alternate coloring #
    line_ladder_no = 0
    # read the ladder text file and get the most updated ladder #
    for line_ladder in ladder1:
        line_ladder_no += 1                             
        rank = Label(ladder, text = line_ladder)
        if line_ladder_no%2 == 0:
            rank.config(bg = 'gold2')
        else:
            rank.config(bg = 'gold4')
        rank.pack()
    ladder1.close()
    # close ladder window #
    close_window = Button(ladder, text = 'Close', command = ladder.destroy).pack()
# button to call ladder window from main window #
ladder_button = Button(window, text = 'Ladder Ranking', command = OpenLadder).pack()

#------------------------------------------------------------------------------------Challenge Player--------------------------------------------------------------------------#
# Open and set properties of Challenge player window #
def ChallengePlayer():
    challenge = Toplevel()
    challenge.title('Challenge Player')
    challenge.geometry('500x700')
    names = getList(current_ladder)
    clicked1 = StringVar()
    clicked1.set('Select')
    clicked2 = StringVar()
    clicked2.set('Select')
    # choose name of challenger from list of players #
    pagetitle3 = Label(challenge, text = 'Select your name:')
    pagetitle3.config(font = 'none 14 bold')
    pagetitle3.pack()
    dropPlayer = OptionMenu(challenge, clicked1, *names)
    dropPlayer.pack()
    # choose name of challenged from list of players #
    pagetitle31 = Label(challenge, text = 'Select Player to Challenge:')
    pagetitle31.config(font = 'none 14 bold')
    pagetitle31.pack()
    dropChallenge = OptionMenu(challenge, clicked2, *names)
    dropChallenge.pack()
    # enter date of challenge #
    pagetitle32 = Label(challenge, text = 'Enter date you want to challenge in dd-mm-yyyy:\n Example: 04-06-2021')
    pagetitle32.config(font = 'none 14 bold', pady = 10)
    pagetitle32.pack()
    new_date = Entry(challenge)
    new_date.insert(0, 'dd-mm-yyyy')
    new_date.pack()
    # function to execute after pressing submit #
    def ChallengeSuccess():
        specified_date = new_date.get()
        # enter upcoming challenge to a seperate upcoming_challenges.txt file #
        upcoming_challenge = open('upcoming_challenges.txt', 'a')
        # enters the line for setting up the coming challenge which includes the current rank of the player #
        upcoming_new_line = f'{clicked1.get()} {current_ladder.get(clicked1.get())}/{clicked2.get()} {current_ladder.get(clicked2.get())}/{specified_date}'
        print(upcoming_new_line, file = upcoming_challenge)
        upcoming_challenge.close()
        # statements to print to inform user of successful entry #
        label21 = Label(challenge, text = 'Application Sumbitted.')
        label21.pack()
        label22 = Label(challenge, text = 'If your opponent is higher than 3 on the ladder, you can still play the player')
        label22.pack()
        label23 = Label(challenge, text = 'However application will not register your result into the ladder')
        label23.pack()
        newLabel1 = Label(challenge, text = 'Click Back once done')
        newLabel1.pack()
    # executing of function after submit is pressed #
    challenge_submit_button = Button(challenge, text = 'Submit', command = ChallengeSuccess)
    challenge_submit_button.pack()
    # close challenge player window #
    close_window = Button(challenge, text = 'Back', command = challenge.destroy).pack()
# button to call challenge player window from main window #
challenge_button = Button(window, text = 'Challenge Player', command = ChallengePlayer).pack()

#----------------------------------------------------------------------------------View Upcoming Challenge---------------------------------------------------------------------#
# Open and set properties of upcoming Challenges window #
def UpcomingChallenge():
    UChallenge = Toplevel()
    UChallenge.title('Upcoming Challenges')
    UChallenge.geometry('500x700')
    pagetitle7 = Label(UChallenge, text = 'Upcoming challenges')
    pagetitle7.config(font = 'none 14 bold')
    pagetitle7.pack()
    pagetitle72 = Label(UChallenge, text = 'Challenger/Challenged/Date')
    pagetitle72.config(font = 'none 12 bold')
    pagetitle72.pack()
    file = open('upcoming_challenges.txt', 'r')
    # from upcoming_challenges text file, print the data for the user to see #
    for line in file:
        Uchallenge = Label(UChallenge, text = line).pack()
    file.close()
    # close Upcoming challenges window #
    close_window = Button(UChallenge, text = 'Close', command = UChallenge.destroy).pack()
# button to call Upcoming challenges window from main window #
ladder_button = Button(window, text = 'Upcoming Challenges', command = UpcomingChallenge).pack()

#----------------------------------------------------------------------------------------Score Input--------------------------------------------------------------------------#
# Open and set properties of Score Input window #
def ScoreInput():
    scoreInput = Toplevel()
    scoreInput.title('Input Score')
    scoreInput.geometry('500x700')
    pagetitle7 = Label(scoreInput, text = 'Select Challenge')
    pagetitle7.config(font = 'none 14 bold')
    pagetitle7.pack()
    # inform the player that if they choose to forfiet the match, they can keep the score field empty and click submit #
    label75 = Label(scoreInput, text = 'If you choose to forefiet the match, select your challenge and click submit')
    label75.pack()
    clicked4 = StringVar()
    clicked4.set('Select')
    # choose challenge from the available challenges #
    with open('upcoming_challenges.txt', 'r') as f:
        challenge_list = f.readlines()
    challenge_list = [x.strip() for x in challenge_list]
    challenge_select = OptionMenu(scoreInput, clicked4, *challenge_list)
    challenge_select.pack()
    # Input scores for each round #
    label71 = Label(scoreInput, text = 'Enter score of 1st match')
    label71.pack()
    score1 = Entry(scoreInput)
    score1.pack()
    score1.insert(0, '00-00')
    label72 = Label(scoreInput, text = 'Enter score of 2nd match')
    label72.pack()
    score2 = Entry(scoreInput)
    score2.pack()
    score2.insert(0, '00-00')
    label73 = Label(scoreInput, text = 'Enter score of 3rd match')
    label73.pack()
    label74 = Label(scoreInput, text = '(only enter if required)')
    label74.pack()
    score3 = Entry(scoreInput)
    score3.pack()
    score3.insert(0, '00-00')
    # function to enter data into data file and update the ladder #
    def ScoreCalc():
        data_challenge = clicked4.get()
        match1 = score1.get()
        match2 = score2.get()
        match3 = score3.get()
        # new line to add onto data file #
        new_data = f'{data_challenge}/{match1} {match2} {match3}'
        add_data = open('data.txt', 'a')
        print(new_data, file = add_data)
        add_data.close()
        info_data = data_sort(new_data)
        challenger = info_data[0]
        challenged = info_data[2]
        scores = info_data[3]
        date = info_data[1]
        championship(challenger, challenged, scores, date)
        # update ladder with latest standings #
        ladder = open('ladder.txt', 'w')
        for key in current_ladder.keys():
            print(key, file=ladder)
        ladder.close()
        # delete challenge line from temporary upcoming challenge list and update the text file #
        with open("upcoming_challenges.txt", "r") as f:
            lines = f.readlines()
        with open("upcoming_challenges.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != data_challenge:
                    f.write(line)
        label76 = Label(scoreInput, text = 'Ladder has been updated')
        label76.pack()
        label77 = Label(scoreInput, text = 'Press Back to go back to main page')
        label77.pack()
    # function to execute after pressing submit #
    add_submit_button = Button(scoreInput, text = 'Submit', command = ScoreCalc)
    add_submit_button.pack()
    # close score input window #
    close_window = Button(scoreInput, text = 'Back', command = scoreInput.destroy).pack()
# button to call input score window from main window #
challenge_button = Button(window, text = 'Input Score', command = ScoreInput).pack()

#-----------------------------------------------------------------------------------Add to Competition--------------------------------------------------------------------------------#
#Open and set properties of add player window #
def AddLadder():
    add = Toplevel()
    add.title('Join Competition')
    add.geometry('500x700')
    pagetitle4 = Label(add, text = 'Key in your name:\n \
(with initials)\n \
Example: R Georemon')
    pagetitle4.config(font = 'none 14 bold')
    pagetitle4.pack()
    # register new name #
    new_name = Entry(add)
    new_name.pack()
    new_name.insert(0, 'Enter your name')
    pagetitle41 = Label(add, text = 'Enter date you want to join in dd-mm-yyyy:\n \
Example: 04-06-2021')
    pagetitle41.config(font = 'none 14 bold', pady = 10)
    pagetitle41.pack()
    # register date they want to join#
    new_date = Entry(add)
    new_date.insert(0, 'dd-mm-yyyy')
    new_date.pack()
    # function to add player to data and ladder #
    def AddPlayer():
        data2 = open('data.txt', 'a')
        message = 'Hello ' + new_name.get()
        newLabel41 = Label(add, text = message)
        newLabel41.pack()
        newLabel42 = Label(add, text = 'Your name has been added to the ladder on ' + new_date.get())
        newLabel42.pack()
        newLabel43 = Label(add, text = 'Click back to go back to main page')
        newLabel43.pack()
        add_player = new_name.get()
        add_date = new_date.get()
        # add data of new entry to data file #
        add_line = f'+{add_player}/{add_date}'
        print(add_line, file = data2)
        data2.close()
        # called function to process data string #
        info_data = data_sort(add_line)
        try:
            challenger = info_data[0]
        except:
            pass
        try:
            global challenged
            challenged = info_data[2]
        except IndexError:
            pass
        try:                                                                
            scores = info_data[3][:-2]
        except:                                                           
            scores = 0-0
        date = info_data[1]
        # update ladder with latest information #
        ladder = open('ladder.txt', 'w')
        for key in current_ladder.keys():
            print(key, file=ladder)
        ladder.close()
    # action to take after pressing submit button #
    add_submit_button = Button(add, text = 'Submit', command = AddPlayer)
    add_submit_button.pack()
    newLabel1 = Label(add, text = 'Click Back once done')
    # close add player window #
    close_window = Button(add, text = 'Back', command = add.destroy).pack()
# button to add player window from main window #
add_button = Button(window, text = 'Join Competition', command = AddLadder).pack()

#--------------------------------------------------------------------------------------Leave from Competition---------------------------------------------------------------------------#
# Open and set properties of Remove player #
def RemoveLadder():
    remove = Toplevel()
    remove.title('Leave Competition')
    remove.geometry('500x700')
    pagetitle5 = Label(remove, text = 'Click on name to remove:')
    pagetitle5.config(font = 'none 14 bold')
    pagetitle5.pack()
    # select name from current list of registered players #
    names = getList(current_ladder)
    clicked3 = StringVar()
    clicked3.set('Select')
    removePlayer = OptionMenu(remove, clicked3, *names)
    removePlayer.pack()
    # enter date of removal from ladder #
    pagetitle51 = Label(remove, text = 'Enter date you want to leave in dd-mm-yyyy:\n \
Example: 04-06-2021')
    pagetitle51.config(font = 'none 14 bold', pady = 10)
    pagetitle51.pack()
    removeDate = Entry(remove)
    removeDate.insert(0, 'dd-mm-yyyy')
    removeDate.pack()
    # function to remove player from ladder #
    def RemovePlayer():
        global remove_date
        data2 = open('data.txt', 'a')
        message = 'Hello ' + clicked3.get()
        newLabel51 = Label(remove, text = message)
        newLabel51.pack()
        newLabel52 = Label(remove, text = 'Your name has been removed from the ladder')
        newLabel52.pack()
        newLabel53 = Label(remove, text = 'Click back to go back to main page')
        newLabel53.pack()
        remove_player = clicked3.get()
        remove_date = removeDate.get()
        # enter data of removal to data file #
        remove_line = f'-{remove_player} {current_ladder.get(clicked3.get())}/{remove_date}'
        print(remove_line, file = data2)
        data2.close()
        # called function to process data string #
        info_data = data_sort(remove_line)
        try:
            challenger = info_data[0]
        except:
            pass
        try:
            global challenged
            challenged = info_data[2]
        except IndexError:
            pass
        try:                                                                
            scores = info_data[3][:-2]
        except:                                                         
            scores = 0-0
        date = info_data[1]
        # update ladder with latest information #
        ladder = open('ladder.txt', 'w')                                #update ladder
        for key in current_ladder.keys():
            print(key, file=ladder)
        ladder.close()
    # submit button to execute order after pressing #
    remove_submit_button = Button(remove, text = 'Submit', command = RemovePlayer)
    remove_submit_button.pack()
    # close remove player window #
    close_window = Button(remove, text = 'Back', command = remove.destroy).pack()
# button to call remove player window from main window #
remove_button = Button(window, text = 'Leave Competition', command = RemoveLadder).pack()

#--------------------------------------------------------------------------------------------Query-----------------------------------------------------------------------------------#
# Open and set properties of query window
def Query():
    query = Toplevel()
    query.title('Query')
    query.geometry('500x700')
    pagetitle6 = Label(query, text = 'Make a Query')
    pagetitle6.config(font = 'none 14 bold')
    pagetitle6.pack()
    # Open and set properties of Challenges on date window #
    def csd():
        CSD = Toplevel()
        CSD.title('Challenges on Specific Date')
        CSD.geometry('500x700')
        # enter date
        pagetitle = Label(CSD, text = 'Enter the date to see all challenges on that date:')
        pagetitle.config(font = 'none 14 bold')
        pagetitle.pack()
        CSD_box = Entry(CSD)
        CSD_box.insert(0, 'DD-MM-YYYY')
        CSD_box.pack()
        # function to be executed after pressing submit #
        def SCD():
            sd = CSD_box.get()
            # call function to process data entered #
            sdresult = specific_challenge_date(sd)
            label = Label(CSD, text = 'Challenger/Challenged/Date/Match Scores:')
            label.config(font = 'none 12 bold')
            label.pack()
            # print out data of challenges on specific date #
            for r in sdresult:
                slabel = Label(CSD, text = r).pack()
        # execute function after pressing submit #
        CSD_submit = Button(CSD, text = 'Submit', command = SCD).pack()
        # close challenges on date window #
        close_window = Button(CSD, text = 'Back', command = CSD.destroy).pack()
    # button to call ladder window from query window #
    challenge_specific_date = Button(query, text = 'Challenges on a specific date', command = csd).pack()

    # Open and set properties of matches played on date range window
    def Pmd():
        PMD = Toplevel()
        PMD.title('Total matches played on a date range')
        PMD.geometry('500x700')
        pagetitle = Label(PMD, text = 'Enter starting date and ending date:')
        pagetitle.config(font = 'none 14 bold')
        pagetitle.pack()
        # enter date range
        label1 = Label(PMD, text = 'Enter start date:').pack()
        start_date = Entry(PMD)
        start_date.insert(0, 'DD-MM-YYYY')
        start_date.pack()
        label2 = Label(PMD, text = 'Enter end date:').pack()
        end_date = Entry(PMD)
        end_date.insert(0, 'DD-MM-YYYY')
        end_date.pack()
        # function to be executed after pressing submit #
        def pmd():
            s_d = start_date.get()
            e_d = end_date.get()
            # call function to process data entered #
            pmdresult = played_matches_date(s_d, e_d)
            label = Label(PMD, text = 'Challenger/Challenged/Date/Match Scores:')
            label.config(font = 'none 12 bold')
            label.pack()
            # print out all challenges in date range #
            for r in pmdresult:
                plabel = Label(PMD, text = r).pack()
        # function to be executed after pressing submit #
        PMD_submit = Button(PMD, text = 'Submit', command = pmd).pack()
        # close challenges on date range window #
        close_window = Button(PMD, text = 'Back', command = PMD.destroy).pack()
    # button to call challenge date range window from query window #
    challenge_date_range = Button(query, text = 'Challenges in a date range', command = Pmd).pack()

    # Open and set properties of PvP window #
    def Scp():
        SCP = Toplevel()
        SCP.title('Total challenges played against another player')
        SCP.geometry('500x700')
        pagetitle = Label(SCP, text = 'Select name of Players to see challenged dates:')
        pagetitle.config(font = 'none 14 bold')
        pagetitle.pack()
        names = getList(current_ladder)
        clicked3 = StringVar()
        # choosing both players #
        clicked3.set('Select First Player')
        firstPlayer = OptionMenu(SCP, clicked3, *names)
        firstPlayer.pack()
        clicked4 = StringVar()
        clicked4.set('Select Second Player')
        secondPlayer = OptionMenu(SCP, clicked4, *names)
        secondPlayer.pack()
        # function to execute after pressing submit #
        def PCS():
            f_p = clicked3.get()
            s_p = clicked4.get()
            # call function to process data entered #
            r_p = specific_challenge_players(f_p,s_p)
            label = Label(SCP, text = 'Challenger/Challenged/Date/Match Scores:')
            label.config(font = 'none 12 bold')
            label.pack()
            for r in r_p:
                rlabel = Label(SCP, text = r).pack()
        # function to be executed after pressing submit #
        PCS_submit = Button(SCP, text = 'Submit', command = PCS).pack()
        # close PvP window #
        close_window = Button(SCP, text = 'Back', command = SCP.destroy).pack()
    # button to call PvP window from query window #   
    specific_challenge_player = Button(query, text = 'Challenges played by 2 players', command = Scp).pack()

    # Open and set properties of Player data window #
    def Pmp():
        PMP = Toplevel()
        PMP.title('Total matches played by player')
        PMP.geometry('500x700')
        # select name of player from drop down menu #
        pagetitle = Label(PMP, text = 'Select name of player:')
        pagetitle.config(font = 'none 14 bold')
        pagetitle.pack()
        names = getList(current_ladder)
        clicked = StringVar()
        clicked.set('Select First Player')
        Player = OptionMenu(PMP, clicked, *names)
        Player.pack()
        # function to execute after pressing submit #
        def pmp():
            label = Label(PMP, text = 'Challenger/Challenged/Date/Match Scores:')
            label.config(font = 'none 12 bold')
            label.pack()
            p = clicked.get()
            # function to process data #
            match = played_matches_player(p)
            for m in match:
                mLabel = Label(PMP, text = m).pack()
        # function to be executed after pressing submit #
        PMP_submit = Button(PMP, text = 'Submit', command = pmp).pack()
        # close player data window #
        close_window = Button(PMP, text = 'Back', command = PMP.destroy).pack()
    # button to call player data from query window #
    Played_matches_player = Button(query, text = 'Matches played by a player', command = Pmp).pack()

    # Open and set properties of max and min played player #
    def Mplp():
        MPLP = Toplevel()
        MPLP.title('Most and least active Player:')
        MPLP.geometry('500x700')
        # display information #
        pagetitle = Label(MPLP, text = 'Most and least active Player:')
        pagetitle.config(font = 'none 14 bold')
        pagetitle.pack()
        label1 = Label(MPLP, text = 'Most active player:')
        label1.config(font = 'none 12 bold')
        label1.pack()
        # execute function to get max played player #
        label12 = Label(MPLP, text = most_challenge()).pack()
        label2 = Label(MPLP, text = 'Least active player:')
        label2.config(font = 'none 12 bold')
        label2.pack()
        # execute function to get min played palyer #
        label122 = Label(MPLP, text = least_challenge()).pack()
        # close max and min played player window #
        close_window = Button(MPLP, text = 'Back', command = MPLP.destroy).pack()
    # button to max and min played window from query window #    
    Most_and_least_played = Button(query, text = 'Most and least active players', command = Mplp).pack()

    # entering of additional queries to be resolved manually #
    query_box = Entry(query, width = 180)
    query_box.pack()
    query_box.insert(0, 'Enter other Query here')
    # add query to be resolved manually #
    def AddQuery():
        # information compiled onto seperate text file
        query_compile = open('query.txt', 'a')
        print(query_box.get(), file = query_compile)
        label = Label(query, text = 'Query Successfully sent. It may take up to 5 days to get response')
        label.pack()
        label1 = Label(query, text = 'Press Back to go back to main page')
        label1.pack()
    # function to be executed after pressing submit #
    query_submit_button = Button(query, text = 'Submit', command = AddQuery)
    query_submit_button.pack()
    close_window = Button(query, text = 'Back', command = query.destroy).pack()
    label44 = Label(query, text = 'History of all matches:')
    label44.config(font = 'none 12 bold')
    label44.pack()
    # scroll window showing full history of competition #
    scrollbar = Scrollbar(query)
    scrollbar.pack(side=RIGHT, fill = Y)
    listbox = Listbox(query)
    listbox.config(width=80, height=100, yscrollcommand = scrollbar.set)
    listbox.pack()
    with open('data.txt', 'r') as f:
        data_list = f.readlines()
    for i in data_list:
        listbox.insert(END, i)
    scrollbar.config(command=listbox.yview)
    # button to call query window from main window #
query_button = Button(window, text = 'Query', command = Query).pack()

#--------------------------------------------------------------------------------------Functions for queries---------------------------------------------------------------------------#
#function to get compare entered date and data data and get lines with this information#
def specific_challenge_date(d1):
    from datetime import datetime
    d1 = datetime.strptime(d1, '%d-%m-%Y')
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = []
    for line in data:
        if line[0] != '+' and line[0] != '-':
            info = line.split('/')
            dateTemp = info[2]
            dateTemp = dateTemp.strip(' ')
            d2 = datetime.strptime(dateTemp, '%d-%m-%Y')
            if d2 == d1:
                results.append(line)
    return (results)

#function to get info of 2 players who challenged and get lines with this information#
def specific_challenge_players(p1,p2):
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = []
    for line in data:
        if line[0] != '+' and line[0] != '-':
            variables = line.split('/')
            name_pre  = variables[0]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name1 = sur_name + ' ' + main_name
            name_pre  = variables[1]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name2 = sur_name + ' ' + main_name
            res = (p1 == name1 and p2 == name2) or (p1 == name2 and p2 == name1)
            if res == True:
                results.append(line)
    return (results)

#function to get matches payed by one player and get lines with this information#
def played_matches_player(p):
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = []
    for line in data:
        if line[0] != '+' and line[0] != '-':
            variables = line.split('/')
            name_pre  = variables[0]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name1 = sur_name + ' ' + main_name
            name_pre  = variables[1]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name2 = sur_name + ' ' + main_name
            if (name1 == p or name2 == p):
                results.append(line)
    return (results)

#function to get compare entered date range and get lines with this information#
def played_matches_date(d1, d2):
    from datetime import datetime
    d1 = datetime.strptime(d1, '%d-%m-%Y')
    d2 = datetime.strptime(d2, '%d-%m-%Y')
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = []
    for line in data:
        if line[0] != '+' and line[0] != '-':
            info = line.split('/')
            d3 = datetime.strptime(info[2].strip(' '), '%d-%m-%Y')
            if d3 >= d1 and d3 <= d2 and info[3] != '':
                results.append(line)
    return (results)

#function to compare players who played most match with data file#
def most_challenge():
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = {}
    ladder1 = open('ladder.txt', 'r')
    ladder_data = ladder1.readlines()
    ladder_data = [q.strip() for q in ladder_data]
    for name in ladder_data:
        results[name] = 0
    for line in data:
        try:
            if line[0] != '+' and line[0] != '-':
                variables = line.split('/')
                name_pre  = variables[0]
                name_split = name_pre.split()
                sur_name = name_split[0]
                main_name = name_split[1]
                name1 = sur_name + ' ' + main_name
                results[name1] += 1
                name_pre  = variables[1]
                name_split = name_pre.split()
                sur_name = name_split[0]
                main_name = name_split[1]
                name2 = sur_name + ' ' + main_name
                results[name2] += 1
        # if player no longer in competition, ignore them #
        except:
            pass
        max_key = max(results, key = results.get)
    return (max_key)

# function to compare players who played least match with data file #
def least_challenge():
    data1 = open('data.txt', 'r')
    data = data1.readlines()
    data = [q.strip() for q in data]
    results = {}
    ladder1 = open('ladder.txt', 'r')
    ladder_data = ladder1.readlines()
    ladder_data = [q.strip() for q in ladder_data]
    for name in ladder_data:
        results[name] = 0
    for line in data:
        try:
            if line[0] != '+' and line[0] != '-':
                variables = line.split('/')
                name_pre  = variables[0]
                name_split = name_pre.split()
                sur_name = name_split[0]
                main_name = name_split[1]
                name1 = sur_name + ' ' + main_name
                results[name1] += 1
                name_pre  = variables[1]
                name_split = name_pre.split()
                sur_name = name_split[0]
                main_name = name_split[1]
                name2 = sur_name + ' ' + main_name
                results[name2] += 1
        # if player no longer in competition, ignore them #
        except:
            pass
        min_key = min(results, key = results.get)
    return (min_key)

#--------------------------------------------------------------------------------------Current Date----------------------------------------------------------------------------------#
#import current date and time#
import datetime
now = datetime.datetime.now()
dandt = Label(window, text = 'Current date is:')
dandt.pack()
date_and_time = Label(window, text = now.strftime('%d-%m-20%y'), pady = 10)
date_and_time.pack()

#---------------------------------------------------------------------------------------Main Picture---------------------------------------------------------------------------------#
# for main programme picture #
#filename = PhotoImage(file = 'bg.gif')
#background_label = Label(window, image=filename)
#background_label.pack()

################################################################################ END OF GRAPHICAL USER INTERFACE #####################################################################
    
####################################################################################### MAIN PROGRAMME ###############################################################################

data = open('data.txt', 'r')
ladder = open('ladder.txt', 'r')

# total number of players #
tot_player = 0
# current ladder which will get updated over time #
current_ladder = {}                                                     

def getList(dict):
    return list(dict.keys())

# setting default ladder #
for line in ladder:                                                    
    tot_player += 1                                                     
    line = line[:-1]
    current_ladder[line] = tot_player
ladder.close()
# sort ladder in ascending order #
current_ladder = {k: v for k, v in sorted(current_ladder.items(), key = lambda v: v[1])}

# function to add/remove players or get information of challenge such as name of challenger, name of challenged #
def data_sort(a):                                                       
    variables = a.split('/')
    global current_ladder                                               
    global tot_player
    # if plus sign, add player to ladder #
    if variables[0][0] == '+':                                          
        tot_player += 1
        name = variables[0][1:]
        date = variables[-1]
        current_ladder[name] = tot_player
        current_ladder = {k: v for k, v in sorted(current_ladder.items(), key = lambda v: v[1])}
        return (name, date)
    #if negative sign, remove player from ladder
    elif variables[0][0] == '-':                                       
        name_pre = variables[0]
        name_split = name_pre.split()
        sur_name = name_split[0][1:]
        main_name = name_split[1]
        name = sur_name + ' ' + main_name
        date = variables[-1]
        current_pos_player = int(current_ladder.get(name))
        for key, value in current_ladder.items():
            if value > current_pos_player:
                current_ladder[key] = value-1
        del current_ladder[name]
        tot_player -= 1
        current_ladder = {k: v for k, v in sorted(current_ladder.items(), key = lambda v: v[1])}
        return (name, date)
    # if player names are inside ladder, get details such as name of challenger, challenged and scores #
    else:
        try:                                                            
            name_pre  = variables[0]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name1 = sur_name + ' ' + main_name
            name_pre  = variables[1]
            name_split = name_pre.split()
            sur_name = name_split[0]
            main_name = name_split[1]
            name2 = sur_name + ' ' + main_name
            name_challenger = name1
            name_challenged = name2
            date = variables[2]
            scores = variables[3]
            current_ladder = {k: v for k, v in sorted(current_ladder.items(), key = lambda v: v[1])}
            return (name_challenger, date, name_challenged, scores)
        except:
            pass

# function to determin winner of a challenge #
def championship(challenger, challenged, scores, date):                 
    global current_ladder
    win_count_challenger = 0
    win_count_challenged = 0
    challenger_pos = current_ladder.get(challenger)
    challenged_pos = current_ladder.get(challenged)
    # determine eligibility if challenger can challenge challenged #
    if challenger_pos - challenged_pos <= 3:                        
        scores = scores.split()
        # taking score of each round to determine the winner of that round #
        for score in scores:                                        
            score = score.split('-')
            if score[0] > score[1]:
                win_count_challenger += 1
            elif score[0] < score[1]:
                win_count_challenged += 1
            elif score[0] == score[1]:
                win_count_challenger += 1
                win_count_challenged += 1
            elif score[0] == 0 and score[1] == 0:
                current_ladder[challenger] = challenged_pos
                current_ladder[challenged] = challenger_pos
        # determine who won more rounds and if so, swap their positions around #
        if win_count_challenger > win_count_challenged:             
            current_ladder[challenger] = challenged_pos
            current_ladder[challenged] = challenger_pos
        # if challenger fails, no change to order
        else:                                                       
            pass
    # if challenger not eligible to challenge, do nothing and inform the challenger #
    else:                                                           
        pass
    # update ladder with latest information #
    ladder = open('ladder.txt' ,'w')
    for key in current_ladder.keys():
        print(key, file=ladder)
    current_ladder = {k: v for k, v in sorted(current_ladder.items(), key = lambda v: v[1])}
    ladder.close()
    
data.close()

#################################################################################### END OF MAIN PROGRAMME ##############################################################################
