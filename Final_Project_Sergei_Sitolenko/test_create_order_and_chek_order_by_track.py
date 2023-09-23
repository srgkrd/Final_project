# Сергей Ситоленко, 8а когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import Data
def test_create_order_and_get_by_track():
    # Создание заказа и получение его трекингового номера в ответе
    response = sender_stand_request.post_new_order(Data.order_body)
    assert response.status_code == 201 # Ожидаемый код ответа 201

    order_track = response.json()["track"]

    # Получение заказа по трекинговому номеру
    response = sender_stand_request.get_order_by_track(order_track)
    assert response.status_code == 200 # Ожидаемый код ответа 200
    # Используем 2 ассерта так как в данном случае  тест содержит в себе два запроса
    # в случае неуспешности выполнения одного из шагов локализация проблемы упрощается.