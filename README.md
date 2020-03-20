# einfache Backends mit python
- Basics (Templates, auf GET-Parameter zugreifen)
- lustige GIFs von giphypop
- Zulip API


# Installation
virtualenv -p python3 venv  
source venv/bin/activate   
pip install -r requirements.txt  
python list-dir.py  oder  
python zulip-web.py  

# Konfiguration (wird vom zulip python Modul benötigt)
(venv) kmille@linbox webprogrammierung-flask master % /bin/cat ~/.zuliprc  
[api]  
email=Email-Adresse, die ich bei zulip hinterlegt habe    
key=[api key](https://zulipchat.com/api/api-keys)  
site=https://community.jugendhackt.org   


# Links
- [Lightning Talk von Jugend hackt Berlin (Beispiel mit Katzen-GIFs](https://media.ccc.de/v/jh-berlin-2018-4-lightning_talk_webprogrammierung_mit_python_flask)  
- [Zulip API](https://community.jugendhackt.org/api/get-all-users)
- [flask quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Dokumentation der Giphy API](https://github.com/shaunduncan/giphypop)
