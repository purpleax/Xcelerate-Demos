from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get raw data from the request
    data = request.get_data(as_text=True)  # Retrieves data as text

    # Write the data to a log file
    with open('received_data.log', 'a') as file:
        file.write(data + '\n')

    return "Data received and logged.\n", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
