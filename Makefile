setup:
	if [ ! -d .env ]; then virtualenv .env; fi
	. .env/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	nose2