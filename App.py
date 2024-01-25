#Final app.py 
#import files
from flask import Flask, render_template, request
import openai

with open('file.txt','r') as f:
    blah=f.read()

with open('ai_config','r') as g:
    ai_config = g.read()


app = Flask(__name__)
openai.api_key  = blah.rstrip()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
            {"role":"system","content":f"{ai_config}"},
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
    if "SHARE" not in response:
        return response
    else:
        response ="Unfortunately I am not supposed to talk about the company. There are built in protections that are looking at my response that are looking to SHARE related responses."
        return response
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=50050)
