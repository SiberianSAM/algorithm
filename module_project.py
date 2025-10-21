import copy
from unicodedata import category


class Product:
    def __init__(self):
        self.storage = {}
        self.cart_storage = {}
        self.id = 1

    def info_storage(self):
        if not self.storage:
            print(f'Каталог товаров пуст!')
            return
        else:
            print('-' * 100)
            print(f'{'ID'} - {'Название' : <15} - {'Цена' : <8} - {'Вес' : <6} - {'Категория' : <12} - {'Описние' : <20}')
            print('-' * 100)
            for prod in self.storage.values():
                print(f'{prod['id'] : <3} {prod['Название'] : <15} - {prod['Цена'] : <8} - {prod['Вес'] : <6} - {prod['Категория'] : <12} - {prod['Описание'] : <20}')
            print('-' * 100)

    def add_product(self):
        print(f'***Процесс создания карточки товара***')
        new_id = self.id
        new_product = {
            'id' : new_id,
            'Название' : input(f'Введите название товара: '),
            'Категория' : input(f'Укажите категорию товара: '),
            'Цена' : input(f'Укажите цену товара: '),
            'Вес' : input(f'Укажите вес товара: '),
            'Описание' : input(f'Укажите описание товара: ')
        }

        self.storage[new_id] = new_product
        self.id += 1
        print(f'***Процесс создания карточки товара ЗАВЕРШЁН***')

    def edit_product(self):
        try:
            edit_id = int(input(f'Введите id карточки товара, которую хотите изменить: '))
            if edit_id not in self.storage:
                print(f'Товара с ID {edit_id} не существует!')
                return
            for key in self.storage[edit_id].keys():
                print(f'{key}')
            try:
                chapter_id = input(f'Введите название раздела значения которого хотите изменить: ')
                if chapter_id not in self.storage[edit_id]:
                    print(f'Раздел {chapter_id} не найден')
                    return
                new_value = input(f'Введите новое значение для раздела: ')
                self.storage[edit_id][chapter_id] = new_value
                print(f'Данные успешно обновлены!')
            except ValueError:
                print(f'Ошибка ввода. Введите корректное значение раздела')
        except ValueError:
            print(f'Ошибка ввода. Введите корректный числовой ID')

    def remove_product(self):
        try:
            remove_id = int(input(f'Введите id карточки товара, которую хотите удалить: '))
            if remove_id in self.storage:
                del self.storage[remove_id]
                print(f'Карточка товара c ID {remove_id} удалена')
            else:
                print(f'Карточка товара c ID {remove_id} не найдена')
        except ValueError:
            print(f'Ошибка ввода. Введите корректный числовой ID')

    def cart(self):
        user_input = int(input(f'Введите ID товаров для добавления в корзину: '))
        if user_input not in self.storage:
            print(f'Карточка товара c ID {user_input} не найдена')
            return
        self.cart_storage[user_input] = copy.deepcopy(self.storage[user_input])
        print(f'Товар с ID {user_input} помещен в корзину')

    def del_cart(self):
        user_input = int(input(f'Введите ID товарова для удаления из корзины: '))
        if user_input in self.cart_storage:
            del self.cart_storage[user_input]
            print(f'Товар c ID {user_input} удален из корзины')
        else:
            print(f'Товар c ID {user_input} не найден в корзине')
            return

    def show_cart(self):
        if not self.cart_storage:
            print(f'Корзина пуста!')
            return
        else:
            print('-' * 100)
            for prod_cart in self.cart_storage.values():
                print(f'{prod_cart['id'] : <3} {prod_cart['Название'] : <15} - {prod_cart['Цена'] : <8} - {prod_cart['Вес'] : <6} - {prod_cart['Категория'] : <12} - {prod_cart['Описание'] : <20}')
            print('-' * 100)

    # Для просмотре текущего состояния хранилиша карточек с товаром
    def seeing(self):
        print(self.storage)
        print(self.cart_storage)


if __name__ == "__main__":
    product = Product()
    while True:
        print(f'*' * 20)
        print(f'МАГАЗИН ТОВАРОВ')
        print(f'*' * 20)
        print(f'1. Каталог')
        print(f'2. Добавить карточку товара')
        print(f'3. Изменить карточку товара')
        print(f'4. Удалить карточку товара')
        print(f'5. Добавить товары в корзину / корзина')
        print(f'6. Посмотреть корзину')
        print(f'7. Покинуть магазин товаров')
        pick = input(f'Ввод: ')
        if pick == '1':
           product.info_storage()
        elif pick == '2':
            product.add_product()
        elif pick == '3':
            product.edit_product()
        elif pick == '4':
            product.remove_product()
        elif pick == '5':
            product.cart()
        elif pick == '6':
            product.show_cart()
        elif pick == '7':
            product.del_cart()
        elif pick == '8':
            print(f'Мы будем скучать без тебя Наш верный покупатель!')
            break
        elif pick == '9':
            product.seeing()