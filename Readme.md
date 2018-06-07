url | Descriptions
----|--------------
 curl --request POST --url https://ams-kgeu.herokuapp.com/account/auth/ --header 'content-type: application/json' --data '{"username":"username", "password":"password"}' | Авторизация
 curl -X GET https://ams-kgeu.herokuapp.com/helpdesk/application/ -H 'Authorization: Token 123213213>' | Получение списка заявок
curl -X GET https://ams-kgeu.herokuapp.com/application/id/ -H 'Authorization: Token 123213213' | Получение определенной заявки
curl -X GET https://ams-kgeu.herokuapp.com/executor/id/ -H 'Authorization: Token 123213213' | Получение определенного исполнителя
curl --request POST --url http://127.0.0.1:8000/helpdesk/executor/ --header 'content-type: application/json' -H 'Authorization: Token 123213213' --data '{"application":id, "owner":id}' | Добавление исполнителя к заявке 
