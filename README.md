# tdd-python

```
python -m venv venv
```
```
source ./venv/bin/activate
```
```
pip install -e .[dev,unit,integration]
```
```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```
```
bandit -r . -x ./test,./venv
```
```
python setup.py bdist_wheel
```
```
python manage.py runserver
```
```
pytest --cov --cov-report xml  test/
```
```
sudo docker build .
```