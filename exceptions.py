class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnoughSpase(LogisticError):
    message = "недостаточно места"


class NotEnoughProduct(LogisticError):
    message = "недостаточно товара"


class UnknownProduct(LogisticError):
    message = "неизвестный товар"


class TooManyDifferentProducts(LogisticError):
    message = "Слишком моного различных товаров"


class InvalidRequest(RequestError):
    message = "неверный запрос"


class InvalidStorage(RequestError):
    message = "такого склада нет"
