from flask import Flask, render_template, jsonify, request
import config
import openai
from googletrans import Translator
import os
import api

def page_not_found(e):
    return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)

translator = Translator()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        lang = request.form['language']

        ans = api.generateChatResponse(prompt)
        ans = translate_prompt(ans, lang)
        res = {}
        res['ans'] = ans
        return jsonify(res), 200
    return render_template('index.html', **locals())

def translate_prompt(prompt, lang):
    # Translate the prompt to the desired language
    if lang != 'en':  # Assuming the default language is English
        translated_prompt = translator.translate(prompt, dest=lang).text
        return translated_prompt
    return prompt

if __name__ == '__main__':
    # Set up Google Translate API credentials
    #os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/gauri/Downloads/chat-gpt-starter-main/chat-gpt-starter-main/translation.json'

    app.run(host='0.0.0.0', port='8888', debug=True)