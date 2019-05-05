# SendToFutureBackground
给未来写封信
uwsgi --http :8001 --chdir /usr/desktop/SendToFutureBackground --wsgi-file SendToFutureBackground/wsgi.py --master --processes 4 --threads 2 --stats 127.0.0.1:8081 
