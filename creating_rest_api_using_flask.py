from flask import Flask, jsonify  
app = Flask(__name__)

my_info = {
    "name": "Sheena Mae Delima",
    "course_and_section": "BSCPE 1-2",
    "favorite_programming language": "Python",
    "aws_service": "Amazon S3 (Simple Storage Service)"
}

@app.route('/', methods=['GET'])
def get_info():
    pass

if __name__ == '__main__':
    app.run(debug=True)