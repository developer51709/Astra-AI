from flask import Flask, request, jsonify, render_template
import os
import json
from src.core.router import Router

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

router = Router()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    history = data.get('history', [])
    
    # The Router expects a conversation state dictionary
    conversation_state = {"history": history}
    
    response_data = router.handle_request(message, conversation_state)
    return jsonify(response_data)

def run_web_server(host='0.0.0.0', port=5000):
    app.run(host=host, port=port)

if __name__ == '__main__':
    run_web_server()
