### curl --request POST --url https://ams-kgeu.herokuapp.com/account/auth/ --header 'content-type: application/json' --data '{"username":"username", "password":"password"}' - Авторизация
### curl -X GET http://127.0.0.1:8000/helpdesk/application/ -H 'Authorization: Token <token>' - Получение списка заявок
### curl -X GET http://127.0.0.1:8000/helpdesk/application/<id>/ -H 'Authorization: Token <token>' - Получение определенной заявки
### curl -X GET http://127.0.0.1:8000/helpdesk/executor/<id> -H 'Authorization: Token <token>' - Получение определенного исполнителя
