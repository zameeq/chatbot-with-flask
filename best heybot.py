#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
from flask import request,render_template,Flask
import os
bot=ChatBot('Friend')
trainer=ListTrainer(bot)

for files in os.listdir('C:/Users/user/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/user/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    trainer.train(data)
    
app=Flask(__name__)

@app.route('/home')

def index():
    return render_template("index.html")
@app.route('/process',methods=['POST'])
def process():
    user_input=request.form['user_input']
    
    bot_response=bot.get_response(user_input)
    bot_response=str(bot_response)
    print("Friend: "+bot_response)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)

if __name__=='__main__':
    app.run(port='5002')
    


# In[ ]:





# In[ ]:




