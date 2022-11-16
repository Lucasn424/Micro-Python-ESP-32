# main.py Main file to run
'''
execfile ('Martian.py')
'''

from machine import Pin, PWM
servo = PWM(Pin(23), freq=50)

def web_page():
  if servo.duty() == 39:
    HexChar="0"
  elif servo.duty() == 45:
    HexChar="1"

  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"></head><body> <h1>ESP Web Server</h1>
  <p>Current Hexidecimal Character: <strong>""" + HexChar + """</strong></p>
  <p><a href="/?hex0"><button class="button">0</button></a></p>
  <p><a href="/?hex1"><button class="button button2">1</button></a></p>
  <p><a href="/?hex2"><button class="button button2">2</button></a></p>
  <p><a href="/?hex3"><button class="button button2">3</button></a></p>
  <p><a href="/?hex4"><button class="button button2">4</button></a></p>
  <p><a href="/?hex5"><button class="button button2">5</button></a></p>
  <p><a href="/?hex6"><button class="button button2">6</button></a></p>
  <p><a href="/?hex7"><button class="button button2">7</button></a></p>
  <p><a href="/?hex8"><button class="button button2">8</button></a></p>
  <p><a href="/?hex9"><button class="button button2">9</button></a></p>
  <p><a href="/?hexA"><button class="button button2">A</button></a></p>
  <p><a href="/?hexB"><button class="button button2">B</button></a></p>
  <p><a href="/?hexC"><button class="button button2">C</button></a></p>
  <p><a href="/?hexD"><button class="button button2">D</button></a></p>
  <p><a href="/?hexE"><button class="button button2">E</button></a></p>
  <p><a href="/?hexF"><button class="button button2">F</button></a></p>
  </body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  hex0 = request.find('/?hex0')
  hex1 = request.find('/?hex1')
  hex2 = request.find('/?hex2')
  hex3 = request.find('/?hex3')
  hex4 = request.find('/?hex4')
  hex5 = request.find('/?hex5')
  hex6 = request.find('/?hex6')
  hex7 = request.find('/?hex7')
  hex8 = request.find('/?hex8')
  hex9 = request.find('/?hex9')
  hexA = request.find('/?hexA')
  hexB = request.find('/?hexB')
  hexC = request.find('/?hexC')
  hexD = request.find('/?hexD')
  hexE = request.find('/?hexE')
  hexF = request.find('/?hexF')
  if hex0 == 6:
    servo.duty(39)
  if hex1 == 6:
    servo.duty(45)
  if hex2 == 6:
    servo.duty(51)
  if hex3 == 6:
    servo.duty(57)
  if hex4 == 6:
    servo.duty(63)
  if hex5 == 6:
    servo.duty(69)
  if hex6 == 6:
    servo.duty(75)
  if hex7 == 6:
    servo.duty(81)
  if hex8 == 6:
    servo.duty(87)
  if hex9 == 6:
    servo.duty(93)
  if hexA == 6:
    servo.duty(99)
  if hexB == 6:
    servo.duty(105)
  if hexC == 6:
    servo.duty(111)
  if hexD == 6:
    servo.duty(117)
  if hexE == 6:
    servo.duty(123)
  if hexF == 6:
    servo.duty(129)
  response = web_page()
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
