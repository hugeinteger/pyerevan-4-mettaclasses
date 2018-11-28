from pseudo_django.model import Model
from pseudo_django.descriptors import Float, Integer, String


class Stock(Model):
    name = String()
    shares = Integer()
    price = Float()


if __name__ == '__main__':
    s = Stock('GOOGL', 100, 1084.36)
    print(s)
