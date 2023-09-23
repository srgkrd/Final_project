# Сергей Ситоленко, 8а когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration

def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)


def get_order_by_track(track):
     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACKNUMBER_PATH, params={"t": track})

