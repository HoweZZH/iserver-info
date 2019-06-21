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


