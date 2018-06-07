curl api | Descriptions
----|--------------
 curl -X POST --url https://ams-kgeu.herokuapp.com/account/auth/ -H 'content-type: application/json' -d '{"username":"username", "password":"password"}' | Авторизация
 curl -X GET https://ams-kgeu.herokuapp.com/helpdesk/application/ -H 'Authorization: Token 123213213>' | Получение списка заявок
curl -X GET https://ams-kgeu.herokuapp.com/application/id/ -H 'Authorization: Token 123213213' | Получение определенной заявки
curl -X POST --url https://ams-kgeu.herokuapp.com/executor/ -H 'content-type: application/json' -H 'Authorization: Token 123213213' --data '{"application":id, "owner":id}' | Добавление исполнителя к заявке 
curl -X POST --url https://ams-kgeu.herokuapp.com/helpdesk/application/ -H 'content-type: application/json' -H 'Authorization: Token 232123' -d '{"author": id, "phone": "phone", "title":"title", "text":"text", "cabinet":"cabinet", "published_date":"year-month-day", "status":"status", "application_executor":[]}' | Создание заявки
