# coding: utf-8
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

botChat = ChatBot('Teste')

conversas = ['oi','olá','olá,bom dia','bom dia,como vai?','estou bem!']

convF = ['Quais filmes vc gosta?','Vc tem algum genero de filme favorito?','Vc gosta de ir ao cinema?',
         'Eu gosto de Harry Potter!','Vc assistiu o último filme da Marvel?']

convR = ['Vc acredita em Deus?','Vc tem alguma relgiao?','Vc é ateu?','Eu sou um bot por isso nao tenho relgiao',
         'Vc acredita quem existe uma força maior que nos move?']



traine = ListTrainer(botChat)
traine.train(conversas)
traine.train(convF)
traine.train(convR)

while True:
    quest = input('Voce: ')

    response = botChat.get_response(quest)

    print('Bot: ',response)







