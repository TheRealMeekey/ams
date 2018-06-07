### curl --request POST --url https://ams-kgeu.herokuapp.com/account/auth/ --header 'content-type: application/json' --data '{"username":"username", "password":"password"}' - Авторизация
### curl -X GET https://ams-kgeu.herokuapp.com/helpdesk/application/ -H 'Authorization: Token <token>' - Получение списка заявок
### curl -X GET https://ams-kgeu.herokuapp.com/application/<id>/ -H 'Authorization: Token <token>' - Получение определенной заявки
### curl -X GET https://ams-kgeu.herokuapp.com/executor/<id> -H 'Authorization: Token <token>' - Получение определенного исполнителя
