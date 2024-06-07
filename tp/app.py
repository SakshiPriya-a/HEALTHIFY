from flask import Flask,render_template,request, jsonify
from chat_bot import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get",method=["GET","POST"])
def chat():
 msg= request.form("msg")
 input = msg
 return get_Chat_response(input) # type: ignore




@app.route('/chat', methods=['POST'])
def chat_bot():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 

    response = get_response(user_input)
    return jsonify({"response": response})


if __name__ == '__main__':
    app.run(debug=True)