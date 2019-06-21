# iserver-info

**Run flask app:**
```
python3 -m pip install --trusted-host pypi.python.org -r requirements.txt
sudo python3 app.py
```


**Run docker image:**
```
docker pull zihowe/iserver-info
docker run -p 4000:80 zihowe/iserver-info:zihao_xml_api
```

visit `http://localhost:4000/`


**Enable debugger:**
add `debug=Ture` to `app.run` in app.py:
```
app.run(host='0.0.0.0', port=4000, debug=True)
```
Go to the web page, it will show you the error message when hit an error. You can use **PIN**(which will show when start flask server)to remote debug.

**build docker image**
set port to 80 and `debug=False` in `app.py`
`change app.run(host='0.0.0.0', port=80, debug=False)`

run `docker build --tag=iserver-info .` in current project folder.

run `docker run -p 4000:80 iserver-info` and visit `localhost:4000`

stop container

tag the image
```python
docker tag image username/repository:tag
# example
docker tag iserver-info:DSSErrors zihowe/iserver-info:DSSErrors
```

publish the image

```
docker push username/repository:tag
# example
docker push zihowe/iserver-info:DSSErrors
```
