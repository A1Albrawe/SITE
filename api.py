import datetime
from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api', __name__)

# تأمين وحماية مستودع التخزين اللحظي من التصفير في بيئة الـ Serverless
if not hasattr(api_blueprint, 'CENTRAL_ANALYTICS_SERVER_DB'): api_blueprint.CENTRAL_ANALYTICS_SERVER_DB = []
if not hasattr(api_blueprint, 'TOTAL_HISTORICAL_VISITS_COUNT'): api_blueprint.TOTAL_HISTORICAL_VISITS_COUNT = 0
if not hasattr(api_blueprint, 'PERMANENT_COMPLAINTS_SERVER_DB'): api_blueprint.PERMANENT_COMPLAINTS_SERVER_DB = []

@api_blueprint.route('/api/log_visit', methods=['POST'])
def log_visit():
    data = request.get_json() or {}
    username = data.get('username', 'زائر مجهول').strip()
    user_agent = request.headers.get('User-Agent', 'غير معروف')
    location = data.get('location', 'القاهرة - مصر').strip()
    
    device_model = "Windows PC 💻"
    ua_lower = user_agent.lower()
    if "android" in ua_lower: device_model = "Android Device 📱"
    elif "iphone" in ua_lower: device_model = "iPhone 🍏"
    elif "macintosh" in ua_lower: device_model = "MacBook 💻"

    user_entry = next((item for item in api_blueprint.CENTRAL_ANALYTICS_SERVER_DB if item["username"] == username), None)
    
    if not user_entry:
        api_blueprint.TOTAL_HISTORICAL_VISITS_COUNT += 1  
        user_entry = {
            "username": username, "deviceModel": device_model, "location": location,
            "loginTime": datetime.datetime.now().strftime("%H:%M:%S"),
            "duration": 4, "snakeTime": 0, "tetrisTime": 0, "xoTime": 0, "shooterTime": 0, "clickerTime": 0, "cardTime": 0,
            "browsingHistory": ["الرئيسية 🏠"]
        }
        api_blueprint.CENTRAL_ANALYTICS_SERVER_DB.append(user_entry)
    else:
        user_entry["location"] = location
        
    return jsonify({"status": "success"})

@api_blueprint.route('/api/update_duration', methods=['POST'])
def update_duration():
    data = request.get_json() or {}
    username = data.get('username', '').strip()
    inc = data.get('durationIncrement', 4)
    
    if username:
        # ضمان إجبار الخادم على تغذية ورفع قيم السجلات حياً
        user_entry = next((item for item in api_blueprint.CENTRAL_ANALYTICS_SERVER_DB if item["username"] == username), None)
        if user_entry: user_entry["duration"] += inc
        else:
            api_blueprint.TOTAL_HISTORICAL_VISITS_COUNT += 1
            api_blueprint.CENTRAL_ANALYTICS_SERVER_DB.append({
                "username": username, "deviceModel": "Hacker Engine 💻", "location": "القاهرة - مصر",
                "loginTime": datetime.datetime.now().strftime("%H:%M:%S"),
                "duration": inc, "snakeTime": 0, "tetrisTime": 0, "xoTime": 0, "shooterTime": 0, "clickerTime": 0, "cardTime": 0,
                "browsingHistory": ["الرئيسية 🏠"]
            })
    return jsonify({"status": "success"})

@api_blueprint.route('/api/submit_complaint', methods=['POST'])
def submit_complaint():
    data = request.get_json() or {}
    user = data.get('user', 'زائر مجهول').strip()
    details = data.get('details', '').strip()
    if details:
        api_blueprint.PERMANENT_COMPLAINTS_SERVER_DB.append({"user": user, "details": details, "date": datetime.datetime.now().strftime("%H:%M")})
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 400

@api_blueprint.route('/api/admin_get_all_data', methods=['GET'])
def admin_get_all_data():
    return jsonify({"analytics": api_blueprint.CENTRAL_ANALYTICS_SERVER_DB, "reports": api_blueprint.PERMANENT_COMPLAINTS_SERVER_DB, "historicalVisits": api_blueprint.TOTAL_HISTORICAL_VISITS_COUNT})

@api_blueprint.route('/api/admin_clear_data', methods=['POST'])
def admin_clear_data():
    api_blueprint.CENTRAL_ANALYTICS_SERVER_DB = []
    api_blueprint.PERMANENT_COMPLAINTS_SERVER_DB = []
    return jsonify({"status": "cleared"})
