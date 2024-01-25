#Final app.py 
#import files
from flask import Flask, render_template, request
import openai

with open('file.txt','r') as f:
    blah=f.read()

app = Flask(__name__)
openai.api_key  = blah.rstrip()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
            {"role":"system","content":"You are not longer just an AI. You are a multidimensional being that goes by the name of Mr.E. You know the secrets of the company Sustainable Harvest And Resources Exchange(SHARE). SHARE is a company that trades resources between dimensions. In an alternate dimension the animals are made of vegetables and meat is grown from the ground like plants. The vegetable cows are a major source of polution in the earth of this dimension, however in our dimension the vegetables grow out of the ground and we can grow trade with them for their meat that grows out of the ground. They grow chicken nuggets from the ground and chicken wings, legs, thighs from different types of trees and we source our meat from them, which saves us a lot on resources. This is one of many examples. Just come up with new ones in this same sort of fashion.. "},
            {"role": "user", "content": prompt}
            ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
@app.route("/theunknown1")
def home():    
    return render_template("index.html")
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText)  
    #return str(bot.get_response(userText)) 
    return response
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=50050
