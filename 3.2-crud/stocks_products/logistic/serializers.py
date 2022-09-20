from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'stocks']
    # настройте сериализатор для продукта
    # pass


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']
    # настройте сериализатор для позиции продукта на складе


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        print(validated_data)
        positions = validated_data.pop('positions')
        print(positions)
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        print('stock:', stock)

        for position in positions:
            position['stock'] = stock
            print('position:', position)

            StockProduct.objects.create(**position)
            StockProduct.objects.create(product=position['product'], quantity=position['quantity'],
                                        price=position['price'], stock=position['stock'])
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        print(validated_data)
        print(instance)
        positions = validated_data.pop('positions')
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        StockProduct.objects.filter(stock_id=instance.id).delete()

        for position in positions:
            position['stock'] = stock
            print('position:', position)

            StockProduct.objects.create(**position)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
