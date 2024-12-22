from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

application = Flask(__name__)  # This is for AWS EB
app = application  # This is for local development
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'Welcome to the Homework Helper API',
        'endpoints': {
            '/webhook': 'POST - Submit homework questions',
            '/health': 'GET - Check API health'
        }
    }), 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Here we'll handle incoming webhook data from Make.com
    try:
        # Extract the relevant information from the webhook
        question = data.get('question', '')
        subject = data.get('subject', '')
        grade_level = data.get('grade_level', '')
        
        # Process the homework help request
        # This is where you can add your tutoring logic
        response = {
            'status': 'success',
            'message': f'Received homework help request for {subject}',
            'question': question,
            'grade_level': grade_level
        }
        
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    print("Starting server on port 8080...")
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
