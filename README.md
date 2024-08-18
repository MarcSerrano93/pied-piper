# encode-labs-uploader

A program that upload files into Telegram.

<!-- GETTING STARTED -->
## Getting Started

Firstly, you need to configure the virtual environment.

```
python -m venv venv

source venv/bin/activate
```

Secondly, you need to install dependencies running the next command:

```
pip install -r requirements.txt
```

After that you need to create a .env file with this content (and fill it with yours):
```
#Telegram
API_ID=
API_HASH=
PHONE_NUMBER=

#TMDB
API_KEY=
```

And finally, you need to fill the config.json file with your own parameters
