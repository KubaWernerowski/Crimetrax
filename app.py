from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/location', methods=['POST'])
def location():
    if request.method == 'POST':
        data = request.json
    #using day and hour when fetching info from network
        day = data['day']
        hour = data['hour']
    return jsonify({'latitude': day,
                    'longitude': hour})

if __name__ == '__main__':
    app.run()