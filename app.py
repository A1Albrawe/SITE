import os
import random
import string
from flask import Flask, session

# تهيئة وإقلاع النواة السحابية المركزية الموحدة والمحصنة لعام 2026
app = Flask(__name__)
app.secret_key = "albrawe_hacker_grid_os_secret_key_final_2026"

# استدعاء وبناء الواجهات المعتمدة كلياً بعد إبادة واستئصال ملف menu القديم
from api import api_blueprint
from home import home_blueprint
from projects import projects_blueprint
from scripts import scripts_blueprint
from report import report_blueprint
from about import about_blueprint
from admin import admin_blueprint

# تعميد وتسجيل الحزم والمسارات البرمجية في قلب السيرفر
app.register_blueprint(api_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(projects_blueprint)
app.register_blueprint(scripts_blueprint)
app.register_blueprint(report_blueprint)
app.register_blueprint(about_blueprint)
# حقن بوابات لوحة التحكم والرقابة السيبرانية V3 في مسار تفتيش مستقل ومعزول
app.register_blueprint(admin_blueprint, url_prefix='/albrawe-admin-panel-2026')

@app.before_request
def generate_stable_user_session():
    # خوارزمية صياغة وتوليد الهوية الرقمية الفريدة للاعبين والزوار حياً
    if 'cyber_user_id' not in session:
        random_suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
        session['cyber_user_id'] = f"user_{random_suffix}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
