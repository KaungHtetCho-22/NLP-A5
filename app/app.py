# import libraries
import os 
import pickle
import torch

from utils import *
from flask import Flask, render_template, request, jsonify, send_file

# load the data
Data         = pickle.load(open('./data/Data.pkl', 'rb'))
max_len      = Data['max_len']
max_mask     = Data['max_mask']
word2id      = Data['word2id']


tokenizer = customTokenizer(word2id)


save_path = f'./model/sentenceBERT.pth'
device    = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# device = 'cpu'
model     = BERT()
model.load_state_dict(torch.load(save_path))
model.to(device)
# model.eval()

# flask app
app = Flask(__name__, static_url_path = '/static')

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'GET':
        result = None
        return render_template('index.html', result=result)
    
    if request.method == 'POST':        
        sentence_a = request.form.get('sen1')
        sentence_b = request.form.get('sen2')
        print(sentence_a, sentence_b)
        result = calculate_similarity(model, tokenizer, sentence_a, sentence_b, device)
        return render_template('index.html', result=result, sen1 = sentence_a, sen2 = sentence_b)



port_number = 8000

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=port_number)


