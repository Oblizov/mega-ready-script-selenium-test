# Selenium tests mega.readyscript.ru

### The following cases are automated:
* `Checking user authorization`

### Used libraries:
* **selenium 4.25.0** 
* **pytest 8.3.3**

### Setting Selenoid
#### Tests are run locally on Selenoid
1) Download the latest Selenoid binary from https://github.com/aerokube/cm/releases/tag/1.8.8
2) Run docker containers Selenoid:
```
./cm selenoid start --vnc
```

#### Stop Selenoid docker containers after running tests
```
./cm selenoid stop
```

### Run аutotest
Run command:
```bash
pytest src/tests/test_login.py
```