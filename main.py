from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, request
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

app = Flask(__name__)
api = Api(app)
bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
            'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

def Model(pergunta):
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        return {"GeorgeBot":str(resposta)}

    else:
        return {"GeorgeBot":'Ainda não sei responder esta pergunta'}


class API_NLP_BOT(Resource):
    def get(self, pergunta_id):
        pergunta = request.form['pergunta']
        bot_resposta = Model(pergunta)
        print(bot_resposta)
        return bot_resposta


class about(Resource):
    def get(self):
        return {"status":"alive"}

api.add_resource(about, '/')     
api.add_resource(API_NLP_BOT, '/<string:pergunta_id>')        

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)

