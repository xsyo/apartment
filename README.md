Для использования вертуального окружения используется библиотека pipenv. Её можно устоновить по команде 
```
pip install pipenv
```

Далее для входа в вертуальную среду нужно ввести команду 
```
pipenv shell
``` 

После нужно устоновить зависимости через команду 
```
pipenv install
``` 

Если у вас версия python не 3.7 то измените файл `Pipfile`.
После запустите приложение
```
py manage.py runserver
``` 

Приложение еще не протестировано!!!
