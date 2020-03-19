# MRoom
just a web demo



-------

**如何启动服务**

```bash
git clone https://github.com/99kies/MRoom
cd MRoom
pip install -r requirements.txt
cd app
python app.py
```

**利用Docker**

```bash
git clone https://github.com/99kies/MRoom
cd MRoom
docker build -t mroom .
docker run -id -p 5000:5000 --name mroom mroom
```

