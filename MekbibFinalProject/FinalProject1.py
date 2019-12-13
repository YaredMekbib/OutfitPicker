#!/usr/bin/env python
# coding: utf-8

# # Yared Mekbib
# # PID - A15525755
# ## Project Description:
#  For this project I created an automatic outfit picker that picks your outfit depending on the weather. It first asks whether or not its hot or cold, and depending on the answer it will ask you for what color tshirts/shorts you own or what color long sleeves/pants you own. Depending on the weather and color combinations you enter, the program will return a random pairing of dark top wear/light bottom wear or light bottom wear/dark top wear.
# ## In order for this program to function correctly, the user must 
# 
# -Import random module and install nltk module
# 
# -To install nltk, write the following in the terminal (pip install nltk --user)
# 
# -Hit enter after each specific COLOR of article of clothing. (EG: What light colored long sleeves do you own? *Type "White" then hit *enter*)
# 
# -Type "Done" when you have completed entering the corresponding article of clothing
# 
# -Be sure to enter the CORRECT type of color the program asks
# 
# #### Test functions
# 
# - for test functions, I am using the pytest module
# - this module can be installed with the following command in the terminal (pip install pytest --user)

# ## Github <br>
# https://github.com/YaredMekbib/OutfitPicker

# In[20]:


# Setup - run this cell before doing the next part of the assignment
#   This imports some /extra code, making it available for us to use later
import random
import nltk


# In[21]:


# Asks what colored long sleeves shirts are owned and appends them into lists.
# Once "Done" is typed, it moves onto the other lists
light_longsleeves = []
dark_longsleeves = []
def longsleeves():
    part1 = True
    while part1:
        print('What light colored long sleeves do you own?')
        answer1 = light_longsleeves.append(input())
        if 'Done' in light_longsleeves:
            light_longsleeves.remove('Done')
            print(light_longsleeves)
            break
    part2 = True
    while part2:
        print('What dark colored long sleeves do you own?')
        answer2 = dark_longsleeves.append(input())
        if 'Done' in dark_longsleeves:
            dark_longsleeves.remove('Done')
            print(dark_longsleeves)
            part2 = False


# In[22]:


# Asks what colored shirts are owned and appends them into lists.
# Once "Done" is typed, it moves onto the other lists
light_tshirts = []
dark_tshirts = []
def tshirts():
    part1 = True
    while part1:
        print('What light colored t shirts do you own?')
        answer1 = light_tshirts.append(input())
        if 'Done' in light_tshirts:
            light_tshirts.remove('Done')
            print(light_tshirts)
            break
    part2 = True
    while part2:
        print('What dark colored t shirts do you own?')
        answer2 = dark_tshirts.append(input())
        if 'Done' in dark_tshirts:
            dark_tshirts.remove('Done')
            print(dark_tshirts)
            part2 = False
    


# In[23]:


# Asks what colored pants are owned and appends them into lists.
# Once "Done" is typed, it moves onto the other lists
dark_pants = []
light_pants = []

def pants():
    part1 = True
    while part1:
        print('What light colored pants do you own?')
        answer1 = light_pants.append(input())
        if 'Done' in light_pants:
            light_pants.remove('Done')
            print(light_pants)
            break
    part2 = True
    while part2:
        print('What dark colored pants do you own?')
        answer2 = dark_pants.append(input())
        if 'Done' in dark_pants:
            dark_pants.remove('Done')
            print(dark_pants)
            part2 = False
    


# In[24]:


# Asks what colored shorts are owned and appends them into lists.
# Once "Done" is typed, it moves onto the other lists
dark_shorts = []
light_shorts = []
def shorts():
    part1 = True
    while part1:
        print('What light colored shorts do you own?')
        answer1 = light_shorts.append(input())
        if 'Done' in light_shorts:
            light_shorts.remove('Done')
            print(light_shorts)
            break
    part2 = True
    while part2:
        print('What dark colored shorts do you own?')
        answer2 = dark_shorts.append(input())
        if 'Done' in dark_shorts:
            dark_shorts.remove('Done')
            print(dark_shorts)
            part2 = False
    


# In[25]:


# Main function that asks what the weather is like.
# Sorts your outfit into a random color combo of light/dark or dark/light
def is_weather():
    """Determine if the weather is hot or cold"""
    
    print('Is it hot or cold?')
    msg = input()
    if msg == 'cold' or msg == 'Cold' or msg == 'COLD':
        answer1 = longsleeves()
        answer2 = pants()
        combo = random.randrange(1,3)
        if combo == 1:
            top = random.choice(light_longsleeves)
            bottom = random.choice(dark_pants)
            print('Wear a ' + top + ' long sleeve and ' + bottom + ' pants!')
        else:
            top = random.choice(dark_longsleeves)
            bottom = random.choice(light_pants)
            print('Wear a ' + top + ' long sleeve and ' + bottom + ' pants!')
    elif msg == 'hot' or msg == 'Hot' or msg == 'HOT':
        answer1 = tshirts()
        answer2 = shorts()
        combo = random.randrange(1,3)
        if combo == 1:
            top = random.choice(light_tshirts)
            bottom = random.choice(dark_shorts)
            print('Wear a ' + top + ' t-shirt and ' + bottom + ' shorts!')
        else:
            top = random.choice(dark_tshirts)
            bottom = random.choice(light_shorts)
            print('Wear a ' + top + ' t-shirt and ' + bottom + ' shorts!')


# In[26]:


is_weather()


# In[ ]:




