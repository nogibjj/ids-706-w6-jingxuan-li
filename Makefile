install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

test:
	python3 -m pytest -vv --cov=mylib --cov=main test_*.py

format:	
	python3 -m black *.py 

lint:
	python3 -m ruff check *.py mylib/*.py test_*.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here


generate:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git add .
	git commit -m "finish"
	git push origin main
all: install test format lint deploy
