from app import app, socketio

app.run(host='127.0.0.1', port=5000)
socketio.run(port=5001)
