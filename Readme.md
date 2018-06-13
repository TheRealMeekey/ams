curl api | Descriptions
----|--------------
curl -X POST --url https://ams-kgeu.herokuapp.com/api/account/auth/ -H 'content-type: application/json' -d '{"username":"username", "password":"password"}' | Авторизация
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/application_list/ -H 'Authorization: Token 123213213>' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/my_application/ -H 'Authorization: Token 123213213>' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/history/ -H 'Authorization: Token 123213213>' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/application/id/ -H 'Authorization: Token 123213213' | Получение определенной заявки
curl -X POST --url https://ams-kgeu.herokuapp.com/api/helpdesk/executor/ -H 'content-type: application/json' -H 'Authorization: Token 123213213' --data '{"application":id, "owner":id}' | Добавление исполнителя к заявке 
curl -X POST --url https://ams-kgeu.herokuapp.com/api/helpdesk/application_new/ -H 'content-type: application/json' -H 'Authorization: Token 232123' -d '{"phone": "phone", "title":"title", "text":"text", "cabinet":"cabinet", "application_executor":[]}' | Создание заявки