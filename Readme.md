url | Descriptions
----|--------------
 curl --X POST --url https://ams-kgeu.herokuapp.com/account/auth/ -H 'content-type: application/json' -d '{"username":"username", "password":"password"}' | Авторизация
 curl -X GET https://ams-kgeu.herokuapp.com/helpdesk/application/ -H 'Authorization: Token 123213213>' | Получение списка заявок
curl -X GET https://ams-kgeu.herokuapp.com/application/id/ -H 'Authorization: Token 123213213' | Получение определенной заявки
curl -X GET https://ams-kgeu.herokuapp.com/executor/id/ -H 'Authorization: Token 123213213' | Получение определенного исполнителя
curl -X POST --url https://ams-kgeu.herokuapp.com/executor/ -H 'content-type: application/json' -H 'Authorization: Token 123213213' -d '{"application":id, "owner":id}' | Добавление исполнителя к заявке 

