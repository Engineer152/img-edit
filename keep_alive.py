from flask import Flask,render_template,send_file,request
from threading import Thread
from welcome import welcome

app = Flask('')

@app.route('/')
def main():
  return '<html><head><title>Image Editor</title></head><body bgcolor="white"  link ="cyan" vlink="red"><font color="black" size ="4"><h2>Image Editor</h2></font>Testing</body></html>'

@app.route('/welcome',methods=['GET'])
def welcome_link():
  sbg=''
  pfp=''
  server=''
  user=''
  color=(237, 230, 211)
  if 'pfp' in request.args:
    pfp=request.args.get('pfp')+'?size=256'
  if 'bg' in request.args:
    sbg=request.args.get('bg')
  if 'server' in request.args:
    server=request.args.get('server')
  if 'user' in request.args:
    user=request.args.get('user')
  if 'color' in request.args:
    color=request.args.get('color')
  welcome(server,user,pfp,sbg,color)
  return send_file(f"./out/{server}.png",mimetype='image/png')

def run():
  app.run(host="0.0.0.0", port=80)

def keep_alive():
  server = Thread(target=run)
  server.start()