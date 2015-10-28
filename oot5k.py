# Outfit-o-Tron 5000 ALPHA
from sys import exit
import csv
from os.path import exists
import random
import pandas as pd

# start screen
# add a close option
def dicts():
    global article_dict
    global top_type_dict
    global bottom_type_dict
    global dress_dict
    global second_type_dict
    global color_dict
    global weather_dict
    article_dict = {1: 'Top', 2: 'Bottom', 3: 'Dress', 4: 'Jacket/Cardigan'}
    if article == 1:  # tops
        top_type_dict = second_type_dict = {1: 'Blouse', 2: 'Camisole/Tee', 3: 'Shirt', 4: 'Sweater'}
    elif article == 2:  # bottoms
        bottom_type_dict = second_type_dict = {1: 'Pants', 2: 'Skirt'}
    elif article == 3:
        dress_dict = second_type_dict = {}
    color_dict = {1: 'Warm', 2: 'Cool', 3: 'Neutral', 4: 'Pattern'}
    weather_dict = {1: 'Warm', 2: 'Cold', 3: 'Any'}

def start():
    print('Welcome to the Outfit-o-Tron 5000! \n')
    print('Before we get into the fun stuff, we need to know: where do you want your outfit database to be stored (or where is it already)?')
    print('Type or copy and paste a file directory here, e.g. C:/Users/Tammy/Documents/  Make sure to use forward slashes!')
    global file_dir
    global db
    file_dir = input("> ")
    if not exists(file_dir):
        print('\n Sorry, that\'s not a valid filepath. Try again, check your spelling, and make sure to use forward slashes (/) not back slashes (\)! \n')
        start()
    elif not file_dir.endswith('/'):
        file_dir = file_dir + '/'
        menu()
    else:
        menu()

# menu: would you like to add to the wardrobe or select an outfit?
# add a close option
def menu():
    print('Would you like to ADD to your wardrobe, SELECT an outfit, or QUIT?')
    menu_select = ''
    menu_select = input('> ')
    if menu_select.lower() in ('add', 'ad', 'a'):
        print('Beep bop boop beep bop....')
        print('Whirrr.... whirrr....')
        add_wardrobe()
    elif menu_select.lower() in ('select', 's'):
        print('Beep beep boop boop....')
        outfit_select()
    elif menu_select.lower() in ('quit', 'q'):
        exit
    else:
        print('Um. I didn\'t get that. Could you try again?')
        menu()
        return

# data input
def add_wardrobe():
    print('\nWelcome to the wardrobe modification area. When given a list of options, please enter the number associated with that option. \n')
    print('Please enter a nickname for the article of clothing we\'re entering now, e.g. "Favorite red blouse".')
    global name
    name = ''
    name = input('> ')
    if name.lower() in('none', 'quit', 'stop', 'exit'):
        back = input('Do you want to return to the main menu? (Y/N)     > ')
        if back.lower() == 'y':
            menu()
    # need to add a duplicate search here
    else:
        add_article()

def add_article():
    print('What article of clothing are you adding? Please choose from: \n 1) Top \n 2) Bottom \n 3) Dress \n 4) Jacket/Cardigan \n 5) Quit')
    try:
        global article
        global second_type
        second_type = None
        article = None
        article = int(input('> '))
        if article == 1:
            print('You chose TOP. Is it a: \n 1) Blouse \n 2) Camisole/Tee \n 3) Shirt \n 4) Sweater \n 5) Oops, I didn\'t mean to choose TOP')
            second_type = int(input('> '))
            if second_type in (1, 2, 3, 4):
                color()
                return
            elif second_type == 5:
                add_article()
                return
            else:
                type_error()
                return
        elif article == 2:
            print('You chose BOTTOM. Which type? \n 1) Pants \n 2) Skirt \n 3) Oops, I didn\'t mean to choose BOTTOM')
            second_type = int(input('> '))
            if second_type == 3:
                add_article()
                return
            elif second_type in (1, 2):
                color()
                return
            else:
                type_error()
                return
        elif article in (3, 4):
            color()
            return
        elif article == 5:
            exit
        else:
            type_error()
            return
    except:
        type_error()
        return

def type_error():
    print('Whoa there. Let\'s take a deep breath and try again.')
    add_article()
    return

def color():
    dicts()
    print('What color family is the ' + article_dict[article].lower() + ' in? \n 1) Warm \n 2) Cool \n 3) Neutral \n 4) Pattern')
    global art_color
    art_color = int(input('> '))
    if art_color in (1, 2, 3, 4):
        weather()
    else:
        print('Whoa there. Let\'s take a deep breath and try again.')
        color()

def weather():
    print('When would you want to wear this ' + article_dict[article].lower() + '? \n 1) When it\'s warm outside \n 2) When it\'s cold outside \n 3) Any weather')
    global art_weather
    art_weather = None
    art_weather = int(input('> '))
    if art_weather in (1, 2, 3):
        review()
    else:
        print('Whoa there. Let\'s take a deep breath and try again.')
        weather()

def review():
    print('You\'re all done! Does this look right?')
    print('Nickname:     ' + name)
    print('Article Type: ' + article_dict[article])
    if article in (1, 2):
        print(article_dict[article] + ' Type: ' + second_type_dict[second_type])
    print('Color Family: ' + color_dict[art_color])
    print('Weather:      ' + weather_dict[art_weather])
    print('What do you think? \n 1) Looks great! \n 2) I need to change the article or ' + article_dict[article].lower() + ' type')
    print(' 3) I need to change the color family \n 4) I need to change the weather type')
    review_choice = ''
    review_choice = input('> ')
    if review_choice == '1':
        if not exists(file_dir + 'OOT5K.csv'):
            db = open(file_dir + 'OOT5K.csv', 'w')
            writer = csv.writer(db, delimiter=',')
            writer.writerow(['Nickname', 'Article Type', 'Second Type', 'Color Family', 'Weather'])
        else:
            db = open(file_dir + 'OOT5K.csv', 'a')
        with db as csvfile:
            wardrobe_writer = csv.writer(csvfile, delimiter=',')
            wardrobe_writer.writerow([name, article, second_type, art_color, art_weather])
        db.close()
        menu()
    elif review_choice == '2':
        add_article()
    elif review_choice == '3':
        color()
    elif review_choice == '4':
        weather()
    else:
        print('Whoa there. Let\'s take a deep breath and try again.')
        review()

# select an outfit - randomize
def outfit_select():
    print('Beep bop booooooooooooooooooooo.... p')
    # read the wardrobe database
    colnames = ['name', 'article_type', 'second_type', 'art_color', 'art_weather']
    global wardrobe
    wardrobe = pd.read_csv(file_dir + 'OOT5K.csv', names=colnames, header=0).dropna(how='all')
    # read through lists and save each article type as a separate data frame
    global top
    top = wardrobe.query('article_type == 1')
    global bottom
    bottom = wardrobe.query('article_type == 2')
    global dress
    dress = wardrobe.query('article_type == 3')
    global jacket
    jacket = wardrobe.query('article_type == 4')
    outfit_randomizer()

def outfit_randomizer():
    # randomly pick from each item type
    print('Beep bop boop boop')
    item_1 = None
    item_2 = None
    item_3 = None
    item_1 = wardrobe.ix[random.sample(wardrobe.index, 1)]
    if item_1.iloc[0]['article_type'] == 1:
        item_2 = jacket.ix[random.sample(jacket.index, 1)]
        item_3 = bottom.ix[random.sample(bottom.index, 1)]
    elif item_1.iloc[0]['article_type'] == 2:
        item_2 = top.ix[random.sample(top.index, 1)]
        item_3 = jacket.ix[random.sample(jacket.index, 1)]
    elif item_1.iloc[0]['article_type'] == 3:
        item_2 = jacket.ix[random.sample(jacket.index, 1)]
        item_3 = pd.DataFrame({'name': ['']})
    else:  # if it chooses a jacket we can't easily have equal opportunity to pick a dress or top/bottom combo.
        outfit_randomizer()
    print('Your outfit: \n' + item_1.iloc[0]['name'] + '\n' + item_2.iloc[0]['name'] + '\n' + item_3.iloc[0]['name'] + '\n')
    outfit_choice()

def outfit_choice():
    print(' 1) Pick again! \n 2) Main menu \n 3) Quit')
    choice = ''
    choice = input('> ')
    if choice == '1':
        outfit_randomizer()
    elif choice == '2':
        menu()
    elif choice == '3':
        exit
    else:
        print('Whoa there. Let\'s take a deep breath and try again.')
        outfit_choice()

    # print 'Welcome to the outfit selection area. When given a list of options, please enter the number associated with that option.'
    # outfit_weather = raw_input('Please indicate the weather you are dressing for: \n 1) It\'s warm outside \n 2) It\'s cold outside \n 3) It\'s in between')
    # if outfit_weather == '1':
    #     db.close()
    #     wardrobe=open(file_dir + 'OOT5K.csv', 'r')

start()
