from flask import Flask
app = Flask(__name__)

@app.route('/admin/do_login.shtml', methods=['POST'])
def hello_world():
    return "1"


app.run()

"""http://www.bgcryptogroup.com/admin/login.shtml"""