from flask import Flask,Response,json
app = Flask(__name__)


def success_handler(output , status=200 , mimetype='application/json'):
  return Response(output,status=status,mimetype=mimetype)

def error_handle(error_msg , status=500 ,mimeType='application/json'):
  return Response(json.dumps({ "error": { "message":error_msg}}), status=status , mimetype=mimetype)

@app.route('/', methods=['GET'])
def home():
  output = json.dumps({"api": '1.0.2'})
  return success_handler(output=output)
 
 
@app.route('/api/train', methods=['POST']) 
def train():
  output= json.dumps({"success":True})
  
  return success_handler(output=output)

# app.run()
if __name__ == "__main__":

   app.run()
  