from matplotlib import fontconfig_pattern
import pygad
import numpy
import pandas as pd 
import numpy
from pandas import *
import yfinance as yf
import random
from random import randrange
from datetime import datetime
#tweets_df1 = pd.DataFrame(users_list_info, columns=['User','Followers', 'Num_Tweets', 'Num_public_lists', 'Followers_friend', 'Age_account'])
# making dataframe 


def gain(acp_today, acp_yesterday):
    return ((acp_today - acp_yesterday) / (acp_yesterday) )


df = pd.read_csv("srcrape_tweets_user_information_2.csv") 
############################### SORT ##############################
########################## Creating the Ranks ###########################

ranks_followers = []
ranks_tweets = []
ranks_public_list = []
ranks_racio = []
ranks_age = []

########################## By Followers ###########################

df_followers = df.sort_values(by=['Followers'], ascending=False)
rank_1 = df_followers.iloc[:40]
rank_2 = df_followers.iloc[40:80]
rank_3 = df_followers.iloc[80:120]
rank_4 = df_followers.iloc[120:160]
rank_5 = df_followers.iloc[160:200]
rank_6 = df_followers.iloc[200:240]
rank_7 = df_followers.iloc[240:280]
rank_8 = df_followers.iloc[280:320]
rank_9 = df_followers.iloc[320:340]
rank_10 = df_followers.iloc[340:380]
rank_11 = df_followers.iloc[380:420]
rank_12 = df_followers.iloc[420:460]
rank_13 = df_followers.iloc[460:500]
rank_14 = df_followers.iloc[540:580]
rank_15 = df_followers.iloc[580:630]
rank_16 = df_followers.iloc[620:660]
rank_17 = df_followers.iloc[660:700]
rank_18 = df_followers.iloc[700:740]
rank_19 = df_followers.iloc[740:780]
rank_20 = df_followers.iloc[780:800]
ranks_followers = {'Name': 'Followers', 1: rank_1, 2: rank_2, 3: rank_3, 4: rank_4, 5:rank_5,
6: rank_6, 7: rank_7, 8:rank_8, 9: rank_9, 10: rank_10, 11: rank_11, 12: rank_12, 13: rank_13, 
14: rank_14, 15:rank_15, 16: rank_16, 17: rank_17, 18: rank_18, 19: rank_19, 20: rank_20}

###################################################################

##########################3 By Num Tweets #########################

df_num_tweets = df.sort_values(by=['Num_Tweets'], ascending=False)
rank_1 = df_num_tweets.iloc[:40]
rank_2 = df_num_tweets.iloc[40:80]
rank_3 = df_num_tweets.iloc[80:120]
rank_4 = df_num_tweets.iloc[120:160]
rank_5 = df_num_tweets.iloc[160:200]
rank_6 = df_num_tweets.iloc[200:240]
rank_7 = df_num_tweets.iloc[240:280]
rank_8 = df_num_tweets.iloc[280:320]
rank_9 = df_num_tweets.iloc[320:340]
rank_10 = df_num_tweets.iloc[340:380]
rank_11 = df_num_tweets.iloc[380:420]
rank_12 = df_num_tweets.iloc[420:460]
rank_13 = df_num_tweets.iloc[460:500]
rank_14 = df_num_tweets.iloc[540:580]
rank_15 = df_num_tweets.iloc[580:630]
rank_16 = df_num_tweets.iloc[620:660]
rank_17 = df_num_tweets.iloc[660:700]
rank_18 = df_num_tweets.iloc[700:740]
rank_19 = df_num_tweets.iloc[740:780]
rank_20 = df_num_tweets.iloc[780:800]

ranks_tweets = {'Name': 'Tweets', 1: rank_1, 2: rank_2, 3: rank_3, 4: rank_4, 5:rank_5,
6: rank_6, 7: rank_7, 8:rank_8, 9: rank_9, 10: rank_10, 11: rank_11, 12: rank_12, 13: rank_13, 
14: rank_14, 15:rank_15, 16: rank_16, 17: rank_17, 18: rank_18, 19: rank_19, 20: rank_20}
###################################################################

##########################3 By Num_public_lists ###################
df_num_public_lists = df.sort_values(by=['Num_public_lists'], ascending=False)

rank_1 = df_num_public_lists.iloc[:40]
rank_2 = df_num_public_lists.iloc[40:80]
rank_3 = df_num_public_lists.iloc[80:120]
rank_4 = df_num_public_lists.iloc[120:160]
rank_5 = df_num_public_lists.iloc[160:200]
rank_6 = df_num_public_lists.iloc[200:240]
rank_7 = df_num_public_lists.iloc[240:280]
rank_8 = df_num_public_lists.iloc[280:320]
rank_9 = df_num_public_lists.iloc[320:340]
rank_10 = df_num_public_lists.iloc[340:380]
rank_11 = df_num_public_lists.iloc[380:420]
rank_12 = df_num_public_lists.iloc[420:460]
rank_13 = df_num_public_lists.iloc[460:500]
rank_14 = df_num_public_lists.iloc[540:580]
rank_15 = df_num_public_lists.iloc[580:630]
rank_16 = df_num_public_lists.iloc[620:660]
rank_17 = df_num_public_lists.iloc[660:700]
rank_18 = df_num_public_lists.iloc[700:740]
rank_19 = df_num_public_lists.iloc[740:780]
rank_20 = df_num_public_lists.iloc[780:800]

ranks_public_list = {'Name': 'Public_list', 1: rank_1, 2: rank_2, 3: rank_3, 4: rank_4, 5:rank_5,
6: rank_6, 7: rank_7, 8:rank_8, 9: rank_9, 10: rank_10, 11: rank_11, 12: rank_12, 13: rank_13, 
14: rank_14, 15:rank_15, 16: rank_16, 17: rank_17, 18: rank_18, 19: rank_19, 20: rank_20}

###################################################################

##########################3 By Followers_friend ##################
df_racio = df.sort_values(by=['Followers_friend'], ascending=False)
#print(df_racio)

rank_1 = df_racio.iloc[:40]
rank_2 = df_racio.iloc[40:80]
rank_3 = df_racio.iloc[80:120]
rank_4 = df_racio.iloc[120:160]
rank_5 = df_racio.iloc[160:200]
rank_6 = df_racio.iloc[200:240]
rank_7 = df_racio.iloc[240:280]
rank_8 = df_racio.iloc[280:320]
rank_9 = df_racio.iloc[320:340]
rank_10 = df_racio.iloc[340:380]
rank_11 = df_racio.iloc[380:420]
rank_12 = df_racio.iloc[420:460]
rank_13 = df_racio.iloc[460:500]
rank_14 = df_racio.iloc[540:580]
rank_15 = df_racio.iloc[580:630]
rank_16 = df_racio.iloc[620:660]
rank_17 = df_racio.iloc[660:700]
rank_18 = df_racio.iloc[700:740]
rank_19 = df_racio.iloc[740:780]
rank_20 = df_racio.iloc[780:800]



ranks_racio = {'Name': 'Racio', 1: rank_1, 2: rank_2, 3: rank_3, 4: rank_4, 5:rank_5,
6: rank_6, 7: rank_7, 8:rank_8, 9: rank_9, 10: rank_10, 11: rank_11, 12: rank_12, 13: rank_13, 
14: rank_14, 15:rank_15, 16: rank_16, 17: rank_17, 18: rank_18, 19: rank_19, 20: rank_20}

###################################################################

##########################3 By Age_account #########################
df_age = df.sort_values(by=['Age_account'], ascending=False)

rank_1 = df_age.iloc[:40]
rank_2 = df_age.iloc[40:80]
rank_3 = df_age.iloc[80:120]
rank_4 = df_age.iloc[120:160]
rank_5 = df_age.iloc[160:200]
rank_6 = df_age.iloc[200:240]
rank_7 = df_age.iloc[240:280]
rank_8 = df_age.iloc[280:320]
rank_9 = df_age.iloc[320:340]
rank_10 = df_age.iloc[340:380]
rank_11 = df_age.iloc[380:420]
rank_12 = df_age.iloc[420:460]
rank_13 = df_age.iloc[460:500]
rank_14 = df_age.iloc[540:580]
rank_15 = df_age.iloc[580:630]
rank_16 = df_age.iloc[620:660]
rank_17 = df_age.iloc[660:700]
rank_18 = df_age.iloc[700:740]
rank_19 = df_age.iloc[740:780]
rank_20 = df_age.iloc[780:800]


ranks_age = {'Name': 'Age', 1: rank_1, 2: rank_2, 3: rank_3, 4: rank_4, 5:rank_5,
6: rank_6, 7: rank_7, 8:rank_8, 9: rank_9, 10: rank_10, 11: rank_11, 12: rank_12, 13: rank_13, 
14: rank_14, 15:rank_15, 16: rank_16, 17: rank_17, 18: rank_18, 19: rank_19, 20: rank_20}
###################################################################
########################## ACP ####################################


data = yf.download("AAPL", start='2022-01-11', end='2022-02-12')



############################ DATE ######################

data.loc["2022-01-12":"2022-02-12"]
data.to_excel("date.xlsm")
date_df = pd.read_excel('date.xlsm') # can also index sheet by name or fetch all sheets
mylist = date_df['Date'].tolist()

data_12_02 = pd.read_csv('srcrape_tweets_vader_neutro_clean_12_02_28_02.csv')
data_12_01 = pd.read_csv('srcrape_tweets_vader_neutro_clean_12_01_27_01.csv')
info_users = pd.read_csv('srcrape_tweets_user_information_2.csv')
user_info_list = info_users['User'].tolist()

user_tweet_user = []
for user in user_info_list:
    dt_user = data_12_02.loc[data_12_02['User'] == user]
    user_tweet_user.append([user, dt_user])

#########################################################


list_gain = []
list_values = data.values.tolist()


gain_value = 0
#print(list_values)
for i in range(len(list_values)):

        acp_yesterday = list_values[i-1][5]
        acp_today = list_values[i][5]
        list_gain.append([str(mylist[i]), acp_yesterday, acp_today, gain(acp_today, acp_yesterday)])

##################################################################################


################## LIST OF USERS ########################
# extract a column from cvs file and convert to string

data_12_02 = pd.read_csv('srcrape_tweets_vader_neutro_clean_12_02_28_02.csv')
data_12_01 = pd.read_csv('srcrape_tweets_vader_neutro_clean_12_01_27_01.csv')
info_users = pd.read_csv('srcrape_tweets_user_information_2.csv')
user_info_list = info_users['User'].tolist()
#print(user_info_list)
list_data_1 = data_12_01.to_numpy().tolist()
list_data_2 = data_12_01.to_numpy().tolist()
#converting column data to list
user_name_list_not_clean = data_12_02['User'].tolist()
#print(user_name_list_not_clean)
user_name_list_not_clean.extend(data_12_01['User'].tolist())


user_list_cleanm = []
user_name_list_clean  = list(dict.fromkeys(user_name_list_not_clean))

for name in user_name_list_clean:
    if name  not in user_info_list:
       user_list_cleanm.append(name)

users_list_info = []
print(f"Number of users: {len(user_name_list_clean)}")

################## USER DATA #############################
count = 0
user_list = []

for screen_name in user_info_list:

        tweets = []
        polarity = 0
        for tweet in list_data_1:
            if screen_name == tweet[1]:
                    tweets.append([tweet[2], tweet[3], tweet[7]])
                    polarity += tweet[7]
        for tweet in list_data_2:
                if screen_name == tweet[1]:
                    tweets.append([tweet[2], tweet[3], tweet[7]])
                    polarity += tweet[7]

        user = {'user': screen_name, 'tweets': tweets,'polarity': polarity}
        user_list.append(user)
#print(user_list)
df = pd.DataFrame(user_list) 
    
# saving the dataframe 
df.to_csv('user_list.csv') 

########################## Genetic Algroitm #########################
def best_gain_calculation(solutions):
    best_rank =  None
    best_gain = 0
       
    for ranks in solutions:
        rank_gain_total = 0
        for rank in ranks:
            rank_gain_total += rank['gain']
        
        if rank_gain_total > best_gain:
            best_gain = rank_gain_total
            best_rank = ranks
            print(best_gain)
    
    return best_rank, best_gain
print("******************** Genetic Algoritm ***********************")
def fitness(solutions):
    print("******************** Fitness ***********************")
    for ranks in solutions:
        for rank in ranks:
            for i in rank['rank'].to_numpy().tolist():
                    gain_value_rank = 0
                    for user in user_list[:801]:
                        
                        if user['user'] == i[1]:
                            for tweet in user['tweets']:
                                year = tweet[0].split()[0].split("-")[0]
                                month = tweet[0].split()[0].split("-")[1]
                                day = tweet[0].split()[0].split("-")[2]
                                index = 1
                                for values in list_gain:
                                    
                                    year_c = values[0].split()[0].split("-")[0]
                                    month_c = values[0].split()[0].split("-")[1]
                                    day_c = values[0].split()[0].split("-")[2]
                                    if year == year_c :
                                        if month == month_c:
                                            if day == day_c:   
                                                index = list_gain.index(values)

                                                for x in range(index, index + 11):

                                                    gain_value_rank += list_gain[x][3]
                                                    
                    
                    rank['gain'] = gain_value_rank
        

    print("*************************** Best gain *****************************")
    best_rank, best_gain = best_gain_calculation(solutions)
    return best_rank, best_gain

      
def gain_calculation(ranks, num):
    gain = 0
    for mini_rank in ranks[num]:
                gain += mini_rank['gain']
    return gain

def rank_winner_calculation(gain, best_gain, num, rank_winner):
    if gain > best_gain:

        rank_winner = num
        best_gain = gain
    #print(rank_winner, best_gain)
    return (rank_winner, best_gain)
   
 
def selection(ranks):
   # numbers_list = []
    winner_list = []
    
    for i in range(10):
        combat_list = []
        print(f"******************** Tournament Selection {i}***********************")
        for i in range (0, 3):
            num = random.randint(0, 19)
            while num in combat_list or num in winner_list:
                num = random.randint(0, 19)
            combat_list.append(num)
        print(combat_list)

        num_1 = combat_list[0]
        num_2 = combat_list[1]
        num_3 = combat_list[2]

        print(f"Numbers {num_1} {num_2} {num_3} will fight")
            
        num_1_gain = gain_calculation(ranks, num_1)
        best_gain = num_1_gain
        rank_winner = num_1
        print(f"Number {num_1} with gain {num_1_gain}")

        num_2_gain = gain_calculation(ranks, num_2)
        print(f"Number {num_2} with gain {num_2_gain}")
        results = rank_winner_calculation(num_2_gain, best_gain, num_2, rank_winner)
        rank_winner = results[0]
        best_gain = results[1]

        num_3_gain = gain_calculation(ranks, num_3)
        print(f"Number {num_3} with gain {num_3_gain}")
        results = rank_winner_calculation(num_3_gain, best_gain, num_3, rank_winner)
        rank_winner = results[0]
        best_gain = results[1]
        print(f"The winner is {rank_winner} with gain {best_gain}")
        winner_list.append(rank_winner)
    print(f"Winner list {winner_list}")
    return winner_list

def crossover(winner_list, ranks):
    mutation = 0
    solutions = []
    all_parents = []
    print("******************** Parents Selection ***********************") 
    while len(all_parents) != 10:
        mutation += 1
        parents = []
        for i in range(2):
            parent = random.choice(winner_list)
            while parent in all_parents or parent in parents:
                parent = random.choice(winner_list)
            all_parents.append(parent)
            parents.append(parent)
        print(f"*******Parents: {parents}***********")
        print(f"******************** Creating the child of {parents} ... ***********************") 
        crossover_first = random.randint(1, 3)
        crossover_second = random.randint(1, 3)
        while crossover_first == crossover_second:
            crossover_second = random.randint(1, 3)
        crossoverpoints = [crossover_first, crossover_second]
        crossoverpoints.sort()
        print(f"******************** Crossover points {crossoverpoints} ***********************") 
        child_1 = []
        child_2 = []
        new_child = []
        
        index_p_1 = parents[0]
        index_p_2 = parents[1]
        solutions.append(ranks[index_p_1])
        solutions.append(ranks[index_p_2])
        list_index = []
        for y in range(crossoverpoints[0], crossoverpoints[1]):
            list_index.append(y)
            child_1.append(ranks[index_p_1][y])
        list_index.sort()
        
        for z in range(0, 4 + 1):
            while z not in list_index:
                child_1.append(ranks[index_p_2][z]) 
                list_index.append(z)

        list_index = []
        for y1 in range(crossoverpoints[0], crossoverpoints[1]):
            list_index.append(y1)
            child_2.append(ranks[index_p_2][y1])
        list_index.sort()
        
        if mutation == 5:
            print(f"********************* Mutation ************************************")
            mutation = 0
            mutation_point = random.randint(0, 4)
            while mutation_point in list_index:
                mutation_point = random.randint(1, 4)
            list_index.append(mutation_point)
            child_2.append(ranks[index_p_2][mutation_point]) 

        
        for z1 in range(0, 4 + 1):
            while z1 not in list_index:
                child_2.append(ranks[index_p_1][z1]) 
                list_index.append(z1)
        #print(f"***************** Child {child} *************************** ")

        solutions.append(child_1)
        solutions.append(child_2)
    
    return solutions

def foo(ranks):
    best_rank = 0
    best_gain = 0
    solutions = ranks
    for i in range(200):
        best_rank, best_gain = fitness(solutions)
        print("******************** Seletion ***********************")   
        winner_list = selection(ranks)
        print("******************** End of Seletion ***********************")
        print("******************** CrossOver ***********************") 
        solutions = crossover(winner_list, ranks)    
        
        print("******************** End of CrossOver ***********************") 
        
       # print(f"***************** {i} Solution ********** {best_rank} ******** Gain ********* {best_gain}")
    print(f"***************** Best Solution ********** {best_rank}\n   ******** Gain ********* {best_gain}")
    

solutions = [  
[
    {'ID': 1 , 'rank': ranks_followers[1], 'gain': 0, 'Name': 'Followers'},
    {'ID': 1 , 'rank': ranks_public_list[1], 'gain': 0, 'Name': 'Public List'},
    {'ID': 1 , 'rank': ranks_racio[1],  'gain': 0, 'Name': 'Racio'},
    {'ID': 1 , 'rank': ranks_age[1],  'gain': 0, 'Name': 'Age'},
    {'ID': 1 , 'rank': ranks_tweets[1], 'gain': 0, 'Name': 'Tweets'}

],



[
    {'ID': 2 , 'rank': ranks_followers[2], 'gain': 0, 'Name': 'Followers'},
    {'ID': 2 , 'rank':ranks_public_list[2],'gain': 0, 'Name': 'Public List'},
    {'ID': 2 , 'rank':ranks_racio[2], 'gain': 0, 'Name': 'Racio'},
    {'ID': 2 , 'rank':ranks_age[2], 'gain': 0, 'Name': 'Age'},
    {'ID': 2 , 'rank':ranks_tweets[2], 'gain': 0, 'Name': 'Tweets'}

],

[
    {'ID': 3 , 'rank':ranks_followers[3],'gain': 0, 'Name': 'Followers'},
    {'ID': 3 , 'rank':ranks_public_list[3], 'gain': 0, 'Name': 'Public List'},
    {'ID': 3 , 'rank':ranks_racio[3], 'gain': 0, 'Name': 'Racio'},
    {'ID': 3 , 'rank':ranks_age[3], 'gain': 0, 'Name': 'Age'},
    {'ID': 3 , 'rank':ranks_tweets[3], 'gain': 0, 'Name': 'Tweets'}
              
],

[
    {'ID': 4 , 'rank':ranks_followers[4], 'gain': 0, 'Name': 'Followers'}, 
    {'ID': 4 , 'rank':ranks_public_list[4], 'gain': 0, 'Name': 'Public List'}, 
    {'ID': 4 , 'rank':ranks_racio[4], 'gain': 0,  'Name': 'Racio'}, 
    {'ID': 4 , 'rank':ranks_age[4], 'gain': 0, 'Name': 'Age'}, 
    {'ID': 4 , 'rank':ranks_tweets[4], 'gain': 0, 'Name': 'Tweets'}

],

[
    {'ID': 5 , 'rank':ranks_followers[5], 'gain': 0,  'Name': 'Followers'}, 
    {'ID': 5 , 'rank':ranks_public_list[5], 'gain': 0,  'Name': 'Public List'}, 
    {'ID': 5 , 'rank':ranks_racio[5], 'gain': 0, 'Name': 'Racio'}, 
    {'ID': 5 , 'rank':ranks_age[5], 'gain': 0, 'Name': 'Age'}, 
    {'ID': 5 , 'rank':ranks_tweets[5], 'gain': 0, 'Name': 'Tweets'}
    
    
],

[
    {'ID': 6 , 'rank':ranks_followers[6], 'gain': 0,  'Name': 'Followers'},
    {'ID': 6 , 'rank':ranks_public_list[6], 'gain': 0, 'Name': 'Public List'},
    {'ID': 6 , 'rank':ranks_racio[6], 'gain': 0, 'Name': 'Racio'},
    {'ID': 6 , 'rank':ranks_age[6], 'gain': 0, 'Name': 'Age'},
    {'ID': 6 , 'rank':ranks_tweets[6], 'gain': 0, 'Name': 'Tweets'}
    
],

[
    {'ID': 7 , 'rank':ranks_followers[7], 'gain': 0, 'Name': 'Followers'},
    {'ID': 7 , 'rank':ranks_public_list[7], 'gain': 0, 'Name': 'Public List'},
    {'ID': 7 , 'rank':ranks_racio[7], 'gain': 0,  'Name': 'Racio'},
    {'ID': 7 , 'rank':ranks_age[7], 'gain': 0,  'Name': 'Age'},
    {'ID': 7 , 'rank':ranks_tweets[7], 'gain': 0, 'Name': 'Tweets'}


],

[
    {'ID': 8 , 'rank':ranks_followers[8], 'gain': 0, 'Name': 'Followers'},
    {'ID': 8 , 'rank':ranks_public_list[8], 'gain': 0, 'Name': 'Public List'},
    {'ID': 8 , 'rank':ranks_racio[8], 'gain': 0,  'Name': 'Racio'},
    {'ID': 8 , 'rank':ranks_age[8], 'gain': 0,  'Name': 'Age'},
    {'ID': 8 , 'rank':ranks_tweets[8], 'gain': 0, 'Name': 'Tweets'}


],


[
    {'ID': 9 , 'rank':ranks_followers[9], 'gain': 0, 'Name': 'Followers'},
    {'ID': 9 , 'rank':ranks_public_list[9], 'gain': 0,  'Name': 'Public List'},
    {'ID': 9 , 'rank':ranks_racio[9], 'gain': 0, 'Name': 'Racio'},
    {'ID': 9 , 'rank':ranks_age[9], 'gain': 0, 'Name': 'Age'},
    {'ID': 9 , 'rank':ranks_tweets[9], 'gain': 0, 'Name': 'Tweets'}
    
    
    
],

[
    {'ID': 10 , 'rank':ranks_followers[10], 'gain': 0, 'Name': 'Followers'},
    {'ID': 10 , 'rank':ranks_public_list[10], 'gain': 0, 'Name': 'Public List'}, 
    {'ID': 10 , 'rank':ranks_racio[10], 'gain': 0, 'Name': 'Racio'},
    {'ID': 10 , 'rank':ranks_age[10], 'gain': 0, 'Name': 'Age'},
    {'ID': 10 , 'rank':ranks_tweets[10], 'gain': 0, 'Name': 'Tweets'}
    
],

[
    {'ID': 11 , 'rank':ranks_followers[11], 'gain': 0,  'Name': 'Followers'},
    {'ID': 11 , 'rank':ranks_public_list[11], 'gain': 0, 'Name': 'Public List' },
    {'ID': 11 , 'rank':ranks_racio[11], 'gain': 0, 'Name': 'Racio'},
    {'ID': 11 , 'rank':ranks_age[11], 'gain': 0, 'Name': 'Age'},
    {'ID': 11 , 'rank':ranks_tweets[11], 'gain': 0, 'Name': 'Tweets'}


],

[
    {'ID': 12 , 'rank':ranks_followers[12], 'gain': 0, 'Name': 'Followers'},
    {'ID': 12 , 'rank':ranks_public_list[12], 'gain': 0, 'Name': 'Public List'},
    {'ID': 12 , 'rank':ranks_racio[12], 'gain': 0, 'Name': 'Racio'},
    {'ID': 12 , 'rank':ranks_age[12], 'gain': 0, 'Name': 'Age' },
    {'ID': 12 , 'rank':ranks_tweets[12], 'gain': 0, 'Name': 'Tweets'}


],


[
    {'ID': 13 , 'rank':ranks_followers[13], 'gain': 0, 'Name': 'Followers'},
    {'ID': 13 , 'rank':ranks_public_list[13], 'gain': 0, 'Name': 'Public List' },
    {'ID': 13 , 'rank':ranks_racio[13], 'gain': 0, 'Name': 'Racio'},
    {'ID': 13 , 'rank':ranks_age[13], 'gain': 0, 'Name': 'Age'},
    {'ID': 13 , 'rank':ranks_tweets[13], 'gain': 0, 'Name': 'Tweets'}


],

[
    {'ID': 14 , 'rank':ranks_followers[14], 'gain': 0, 'Name': 'Followers'},
    {'ID': 14 , 'rank':ranks_public_list[14], 'gain': 0, 'Name': 'Public List'},
    {'ID': 14 , 'rank':ranks_racio[14], 'gain': 0, 'Name': 'Racio'},
    {'ID': 14 , 'rank':ranks_age[14], 'gain': 0, 'Name': 'Age'},
    {'ID': 14 , 'rank':ranks_tweets[14], 'gain': 0, 'Name': 'Tweets'}



],

[
    {'ID': 15 , 'rank':ranks_followers[15], 'gain': 0, 'Name': 'Followers'},
    {'ID': 15 , 'rank':ranks_public_list[15], 'gain': 0, 'Name': 'Public List'},
    {'ID': 15 , 'rank':ranks_racio[15], 'gain': 0, 'Name': 'Racio'},
    {'ID': 15 , 'rank':ranks_age[15], 'gain': 0, 'Name': 'Age'},
    {'ID': 15 , 'rank':ranks_tweets[15], 'gain': 0, 'Name': 'Tweets'}

],
            
[
    {'ID': 16 , 'rank':ranks_followers[16], 'gain': 0, 'Name': 'Followers'},
    {'ID': 16 , 'rank':ranks_public_list[16], 'gain': 0, 'Name': 'Public List'},
    {'ID': 16 , 'rank':ranks_racio[16], 'gain': 0, 'Name': 'Racio'},
    {'ID': 16 , 'rank':ranks_age[16], 'gain': 0, 'Name': 'Age'},
    {'ID': 16 , 'rank':ranks_tweets[16], 'gain': 0, 'Name': 'Tweets'}
    
],

[
    {'ID': 17 , 'rank':ranks_followers[17],  'gain': 0, 'Name': 'Followers'},
    {'ID': 17 , 'rank':ranks_public_list[17],  'gain': 0, 'Name': 'Public List'},
    {'ID': 17 , 'rank':ranks_racio[17],  'gain': 0, 'Name': 'Racio'},
    {'ID': 17 , 'rank':ranks_age[17],  'gain': 0, 'Name': 'Age'},
    {'ID': 17 , 'rank':ranks_tweets[17],  'gain': 0, 'Name': 'Tweets'}

],

[
    {'ID': 18 , 'rank':ranks_followers[18], 'gain': 0, 'Name': 'Tweets'},
    {'ID': 18 , 'rank':ranks_public_list[18], 'gain': 0, 'Name': 'Public List'},
    {'ID': 18 , 'rank':ranks_racio[18], 'gain': 0, 'Name': 'Racio'},
    {'ID': 18 , 'rank':ranks_age[18], 'gain': 0, 'Name': 'Age'},
    {'ID': 18 , 'rank':ranks_tweets[18], 'gain': 0, 'Name': 'Tweets'}

],

[
    {'ID': 19 , 'rank':ranks_followers[19], 'gain': 0, 'Name': 'Tweets'},
    {'ID': 19 , 'rank':ranks_public_list[19], 'gain': 0, 'Name': 'Public List'},
    {'ID': 19 , 'rank':ranks_racio[19], 'gain': 0, 'Name': 'Racio'},
    {'ID': 19 , 'rank':ranks_age[19], 'gain': 0, 'Name': 'Age'},
    {'ID': 19 , 'rank':ranks_tweets[19], 'gain': 0, 'Name': 'Tweets'}
    
],

[
    {'ID': 20 , 'rank':ranks_followers[20], 'gain': 0,  'Name': 'Tweets'},
    {'ID': 20 , 'rank':ranks_public_list[20], 'gain': 0, 'Name': 'Public List'},
    {'ID': 20 , 'rank':ranks_racio[20], 'gain': 0, 'Name': 'Racio'},
    {'ID': 20 , 'rank':ranks_age[20], 'gain': 0, 'Name': 'Age'},
    {'ID': 20 , 'rank':ranks_tweets[20], 'gain': 0, 'Name': 'Tweets'}
]
]

foo(solutions)