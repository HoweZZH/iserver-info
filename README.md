# simple simcloud flask server
Run flask app:
```
python3 -m pip install --trusted-host pypi.python.org -r requirements.txt
sudo python3 app.py
```


Run docker image:
```
docker pull zihowe/iserver-info
docker run -p 4000:1234 zihowe/inserver-info
```

visit `http://localhost:4000/`


Enable debugger:
add `debug=Ture` to `app.run` in app.py:
```
app.run(host='0.0.0.0', port=3234, debug=True)
```
Go to the web page, it will show you the error message when hit an error. You can use **PIN**(which will show when start flask server)to remote debug.