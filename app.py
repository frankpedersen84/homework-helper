from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import base64
import requests

application = Flask(__name__)
app = application
CORS(app)

# Configure upload settings
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        subject = request.form.get('subject')
        grade_level = request.form.get('grade_level')
        question = request.form.get('question')
        
        # Initialize payload for Make.com webhook
        payload = {
            'subject': subject,
            'grade_level': grade_level,
            'question': question,
            'image_data': None
        }

        # Handle image upload if present
        if 'image' in request.files:
            file = request.files['image']
            if file and allowed_file(file.filename):
                # Convert image to base64
                file_content = file.read()
                encoded_image = base64.b64encode(file_content).decode('utf-8')
                payload['image_data'] = encoded_image

        # Send to Make.com webhook
        response = requests.post(os.getenv('MAKE_WEBHOOK_URL'), json=payload)
        
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': 'Question submitted successfully'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Error sending to webhook'}), 500

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        response = {
            'status': 'success',
            'message': f'Received homework help request for {data.get("subject", "")}',
            'question': data.get('question', ''),
            'grade_level': data.get('grade_level', '')
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200
