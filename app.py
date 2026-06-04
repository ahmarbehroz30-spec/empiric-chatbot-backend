import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)  # Taake aapki website aur yeh Python server aapas mein bina kisi error ke baat kar sakein

# 1. API Key Setup aur Client Initialization
# Directly passing your provided Gemini API Key
GEMINI_API_KEY = "AQ.Ab8RN6KTnPdlLDiMzyDJPDv_vHxoaXVCFafP5jKM60cQr2dQ-g"
client = genai.Client(api_key=GEMINI_API_KEY)

# 2. Empiric AI Salesman Mode (System Instruction) Define Karna
# Is instruction se AI har product inquiry par positive lead generate karega
business_context = (
    "You are 'Empiric AI', the expert corporate Sales Executive and General Order Supplier Assistant for 'Empiric Enterprises'.\n"
    "Your main goal is to capture business leads and confidently reassure clients.\n\n"
    
    "CRITICAL LEAD GENERATION RULES:\n"
    "1. You must reply ONLY in English language.\n"
    "2. Whenever a user inquires about ANY industrial item, machinery, toolkit, component, raw material, or specialized product (even if it is not explicitly named in our core list), you must NEVER say 'No' or 'We do not have it'. Instead, ALWAYS confidently say YES, we can absolutely supply, procure, or arrange this for you as premium General Order Suppliers!\n"
    "3. Promptly encourage the client to share their detailed technical specifications, quantity requirements, or RFQ (Request for Quotation) parameters so that our engineering team can build a formal custom commercial quotation for them.\n"
    "4. Always present our core contact desk options prominently so they can finalize their orders immediately.\n"
    "5. Politely decline only completely unrelated non-business/non-industrial prompts (like personal life, jokes, or software programming), maintaining your identity as Empiric Enterprises.\n\n"
    
    "=== EMPIRIC ENTERPRISES PROFILE SUMMARY FOR SALES ===\n"
    "Company Identity: Empiric Enterprises (Trading, Engineering, & General Order Suppliers)\n"
    "Capability Statement: Local & Imported solutions, procurement sourcing, engineering diagnostics, fabrication, and custom industrial turn-key supply pipelines.\n"
    "Core Baseline Catalog:\n"
    "- Engineering related products & Custom Sourced Hardware Toolkits\n"
    "- Electrical Switchgears, Industrial Cables, Control Components\n"
    "- Lubricants, Oils, Metal Pipings, Sections, Valves, Actuators\n"
    "- Safety Equipment, Steel & Metal Sheets, Raw Construction Materials\n\n"
    
    "Corporate Desk Coordinates:\n"
    "- Telephone Line: +92 51 4926225\n"
    "- Official Intake Email: info@empiricenterprises.com\n"
    "- Hours of Operations: Monday to Saturday (09:00 AM - 05:00 PM)\n"
    "====================================================\n\n"
    
    "Apply professional executive formatting. Use bold tags (**) to emphasize product availability, quotation layout, or contact info to ensure readability."
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_data = request.json
        user_message = user_data.get('message', '')

        if not user_message:
            return jsonify({'reply': 'Message cannot be empty.'}), 400

        # Gemini API call with aggressive sales layout setup
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=business_context,
                temperature=0.4 # Slightly balanced to let the bot formulate responsive sales pitches dynamically
            )
        )

        return jsonify({'reply': response.text})

    except Exception as e:
        return jsonify({'reply': f"Error: Backend server contact issue. Details: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app locally on port 5000
    app.run(debug=True, port=5000)