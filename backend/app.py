import io
import os
from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_cors import CORS
from fpdf import FPDF

# Initialize Flask
app = Flask(__name__)
CORS(app)

# Define the path to the frontend folder
# This goes up one level from 'backend' and into 'frontend'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

class MachineReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_text_color(37, 99, 235)
        self.cell(0, 10, 'Machine Diagnostic Report', 0, 1, 'C')
        self.ln(5)

@app.route('/')
def index():
    # Serve index.html from the frontend folder
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def send_static(path):
    # Serve CSS or other files from the frontend folder
    return send_from_directory(FRONTEND_DIR, path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get('features', [])
        if len(data) >= 4 and (data[3] > 80 or data[2] > 2800):
            res = "Machine Failure"
        else:
            res = "No Machine Failure"
        return jsonify({"prediction": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/download-report', methods=['POST'])
def download_report():
    try:
        req_data = request.get_json()
        features = req_data.get('features', [])
        prediction = req_data.get('prediction', 'Unknown')

        pdf = MachineReport()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, f"Diagnostic Status: {prediction}", ln=True)
        pdf.ln(5)

        labels = ["Air Temp", "Process Temp", "Speed", "Torque", "Tool Wear", "Type"]
        for i in range(min(len(features), len(labels))):
            pdf.set_font("Arial", size=10)
            pdf.cell(95, 10, labels[i], 1)
            pdf.cell(95, 10, str(features[i]), 1)
            pdf.ln()

        pdf_bytes = pdf.output()
        return send_file(io.BytesIO(pdf_bytes), download_name='Report.pdf', mimetype='application/pdf')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)