from app import app,socketio

app.run(port=5000)
socketio.run(port=5001)
