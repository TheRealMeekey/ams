Application Management System
=====================
curl api | Descriptions
----|--------------
curl -X POST --url https://ams-kgeu.herokuapp.com/api/account/auth/ -H 'content-type: application/json' -d '{"username":"username", "password":"password"}' | Авторизация
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/ticket_list/ -H 'Authorization: Token 123213213' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/my_ticket/ -H 'Authorization: Token 123213213' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/ticket_history/ -H 'Authorization: Token 123213213' | Все заявки
curl -X GET https://ams-kgeu.herokuapp.com/api/helpdesk/ticket/id/ -H 'Authorization: Token 123213213' | Получение определенной заявки
curl -X POST --url https://ams-kgeu.herokuapp.com/api/helpdesk/executor/ -H 'content-type: application/json' -H 'Authorization: Token 123213213' --data '{"ticket":id, "owner":id}' | Добавление исполнителя к заявке 
curl -X POST --url https://ams-kgeu.herokuapp.com/api/helpdesk/ticket_new/ -H 'content-type: application/json' -H 'Authorization: Token 232123' -d '{"phone": "phone", "title":"title", "text":"text", "cabinet":"cabinet", "ticket_executor":[]}' | Создание заявки
