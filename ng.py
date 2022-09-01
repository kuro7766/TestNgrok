from pyngrok import ngrok
import time
ngrok.set_auth_token('27xqdUZec8gJCpJ2g8maHKgQAuA_6uT52UntAv25GP48JzA4G')
active_tunnels = ngrok.get_tunnels()
for tunnel in active_tunnels:
    public_url = tunnel.public_url
    ngrok.disconnect(public_url)
url = ngrok.connect(addr=10086, bind_tls=True)
print(url.public_url + '/?token=123456')

while True:
    time.sleep(5)
    print('heat beat')
