import requests as requests
import random
import emoji

url = "https://api.telegram.org/bot1548391198:AAHni6H64lN8HbONOyR8lX4zZZS7ZBV-FJw/"


# create func that get chat id
def get_chat_id(update):
    chat_id = update['message']["chat"]["id"]
    return chat_id


# create func that gets message text
def get_message_text(update):
    message_text = update["message"]["text"]
    return message_text


# creat function that get last_update
def last_update(req):
    response = requests.get(req + "getUpdates")
    response = response.json()
    result = response["result"]
    total_updates = len(result) - 1
    return result[total_updates]  # get last record message update


# create function that let bot send message to user
def send_message(chat_id, message_text):
    params = {"chat_id": chat_id, "text": message_text}
    response = requests.post(url + "sendMessage", data=params)
    return response


# create main function for navigate or reply message back
def main():
    update_id = last_update(url)["update_id"]
    while True:
        update = last_update(url)
        if update_id == update["update_id"]:
            if get_message_text(update) == "/start":
                send_message(get_chat_id(update), 'Ran out of convo topics? ' + emoji.emojize(':broken_heart:') +
                             ' We gotchu!! \nWe will help you make a' + emoji.emojize(':sparkles:') + ' New Friend ' +
                             emoji.emojize(':sparkles:') + 'without an end! '
                                                           '\nWhat topic do you want to talk to your friend about? '
                                                           '\nEnter:\n1 for food \n2 for personality \n3 for entertainment '
                                                           '\n4 for places to go \n5 for volunteer')
            # FOOD
            elif get_message_text(update) == "1":
                food_list = ['Do you get xiaola zhongla or dala?',
                             'Do you prefer cafes restaurants or hawkers?',
                             'Do you pour the milk or cereal in first',
                             'Do you eat food to survive or eat food to enjoy?',
                             'What is your go to comfort food?']
                food_item = random.choice(food_list)
                send_message(get_chat_id(update),
                             'Ask your friend: ' + food_item + '\n' + emoji.emojize(':eyes:') + 'Open the link below to explore more possibilities! '
                                                                                                '\nhttps://ramav111.github.io/food.html')

            # PERSONALITY
            elif get_message_text(update) == "2":
                personality_list = ['Do you prefer zoom uni or ftf uni?',
                                    'Are you comfortable with making new friends online?',
                                    'Would you rather forgive or forget?',
                                    'What is a deal-breaker for a friendship?',
                                    'What would be your perfect day?']
                personality_item = random.choice(personality_list)
                send_message(get_chat_id(update),
                             'Ask your friend: ' + personality_item )


            # ENTERTAINMENT
            elif get_message_text(update) == "3":
                entertainment_list = ['Do you prefer to binge watch shows or watch as they are released?',
                                      'Do you have a spotify playlist to share with me?',
                                      'What movie/show genre do you like to watch?',
                                      'What are some things in shows you cannot stand? (Cliffhangers, sad endings etc)',
                                      'What was a movie/show that left the greatest impact on you?']
                entertainment_item = random.choice(entertainment_list)
                send_message(get_chat_id(update),
                             'Ask your friend: ' + entertainment_item + '\n' + emoji.emojize(':eyes:') + 'Open the link below to explore more possibilities!'
                                                                        '\nhttps://ramav111.github.io/moviesnmusic.html')

            # PLACES
            elif get_message_text(update) == "4":
                places_list = ['Do you prefer hanging out at places with or without aircon?',
                               'Do you prefer going out when the sun is up or down?',
                               'What is your budget for a day out?',
                               'Do you prefer to be active or chill on a day out?',
                               'What do you spend the most money on when you are out?']
                places_item = random.choice(places_list)
                send_message(get_chat_id(update),
                             'Ask your friend: ' + places_item + '\n' + emoji.emojize(':eyes:') + 'Open the link below to explore more possibilities!'
                                                                 '\nhttps://ramav111.github.io/tourism.html')

            # VOLUNTEER
            elif get_message_text(update) == "5":
                volunteer_list = ['Do you have a preference for the beneficiaries you wish to interact with?',
                                  'Do you have talents to showcase to the beneficiaries?',
                                  'Do you prefer long term volunteering with the same group of people or do you wish to have multiple different experiences?',
                                  'Was there a volunteer experiences that left a long lasting impact on you?',
                                  'How can we continue to volunteer during this pandemic?']
                volunteer_item = random.choice(volunteer_list)
                send_message(get_chat_id(update),
                             'Ask your friend: ' + volunteer_item)
            else:
                send_message(get_chat_id(update), "Sorry we do not recognise your input")
            update_id += 1


# call the function to make it reply
main()
