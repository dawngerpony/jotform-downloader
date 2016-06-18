setup:
	if [ ! -d .env ]; then virtualenv .env; fi
	. .env/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	@echo "CIRCLE_TEST_RESULTS = ${CIRCLE_TEST_RESULTS}"
	nose2  --plugin nose2.plugins.junitxml --junit-xml
	@if [ -n "${CIRCLE_TEST_RESULTS}" ]; then \
		mv nose2-junit.xml ${CIRCLE_TEST_RESULTS}/; \
	fi

all:
	test
