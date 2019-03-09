from flask import Flask, request, jsonify, render_template
from PopulateMap import PopulateMap

app = Flask(__name__)

MapNodes = PopulateMap()


@app.route('/map')
def main():
    return render_template('map.html')


@app.route('/location', methods=['POST'])
def location():
    if request.method == 'POST':
        data = request.json
        hour = data["hour"] - 1     # Add +1 before sending back
        day = data["day"]

        MapNodes.applyFilter(day, hour)

        jsonNodes = []

        for node in MapNodes.nodes:
            jsonNode = jsonify({"lat": node.lat, "lng": node.long})
            jsonNodes.append(jsonNode)

        return jsonify({"nodes": MapNodes.nodes})


if __name__ == '__main__':
    app.run()
