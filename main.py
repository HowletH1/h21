from exceptions import RequestError, LogisticError
from shop import Shop
from store import Store
from request import Request


storage = Store(
    items={
        "печеньки": 25,
        "манго": 10,
        "коробки": 20,
        "пироги": 4,
        "бананы": 25,
        "конь": 1,
    },
)

shop = Shop(
    items={
        "печеньки": 2,
        "манго": 2,
        "коробки": 8,
        "пироги": 2,
        "бананы": 2,
    },
)

sources = {
    "магазин": shop,
    "склад": storage
}


def main():
    while True:
        for source_name in sources:
            print(f"{source_name}:\n {sources[source_name].get_items()}")

        user_input = input("Формат запроса:'Доставить 1 конь из склад в магазин'\n"
                           "завершение stop или стоп\n")
        if user_input in ('stop', 'стоп'):
            break
        try:
            request = Request(request=user_input, sources=sources)
        except RequestError as error:
            print(error.message)
            continue

        try:
            sources[request.departure].remove(request.product, request.count)
            print(f'отправлено: {request.count}{request.product} из {request.departure}')
        except LogisticError as error:
            print(error.message)
            continue
        try:
            sources[request.destination].add(request.product, request.count)
            print(f'получено: {request.count}{request.product} в {request.destination}')
        except LogisticError as error:
            print(error.message)
            sources[request.departure].add(request.product, request.count)
            print(f'возврат: {request.count}{request.product} из {request.departure}')
            continue


if __name__ == '__main__':
    main()
