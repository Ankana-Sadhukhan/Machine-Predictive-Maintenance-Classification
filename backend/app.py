# import io
# from flask import Flask, request, send_file, jsonify
# from flask_cors import CORS
# import pdfkit

import io
import os
from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_cors import CORS
from fpdf import FPDF  # <--- Make sure this is here instead of pdfkit

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    # Simple mock logic for the prediction
    data = request.json['features']
    # Example logic: if Torque > 80 or RPM > 2800, predict failure
    if data[3] > 80 or data[2] > 2800:
        return jsonify({"prediction": "Machine Failure"})
    return jsonify({"prediction": "No Machine Failure"})

@app.route('/download-report', methods=['POST'])
def download_report():
    try:
        req_data = request.get_json()
        features = req_data['features']
        prediction = req_data['prediction']
        
        html_content = f"""
        <html>
        <body style="font-family: Arial; background: #0f172a; color: white; padding: 40px;">
            <h1 style="color: #3b82f6; border-bottom: 2px solid #3b82f6;">Machine Diagnostic Report</h1>
            <p style="font-size: 20px;"><strong>Status:</strong> {prediction}</p>
            <div style="background: #1e293b; padding: 20px; border-radius: 10px; border: 1px solid #334155;">
                <h3>Telemetry Data:</h3>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin: 5px 0;"><strong>Air Temp:</strong> {features[0]} K</li>
                    <li style="margin: 5px 0;"><strong>Process Temp:</strong> {features[1]} K</li>
                    <li style="margin: 5px 0;"><strong>Rotational Speed:</strong> {features[2]} RPM</li>
                    <li style="margin: 5px 0;"><strong>Torque:</strong> {features[3]} Nm</li>
                    <li style="margin: 5px 0;"><strong>Tool Wear:</strong> {features[4]} min</li>
                </ul>
            </div>
            <p style="margin-top: 50px; font-size: 11px; color: #94a3b8;">Report Generated Automatically by AI Diagnostics</p>
        </body>
        </html>
        """
        
        # WINDOWS USERS: Uncomment the line below and point to your wkhtmltopdf.exe
        # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        # pdf = pdfkit.from_string(html_content, False, configuration=config)
        
        # MAC/LINUX USERS: Use this line
        pdf = pdfkit.from_string(html_content, False)
        
        return send_file(
            io.BytesIO(pdf),
            download_name='Machine_Report.pdf',
            as_attachment=True,
            mimetype='application/pdf'
        )
    except Exception as e:
        print(f"Server Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)