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
        self.show_cart()
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
            total_price = 0
            for product_dict in self.cart_storage.values():
                price = product_dict.get('Цена')
                total_price += int(price)
            print(f'Итоговая цена корзины составляет: {total_price}')


    # Методы сортииовки
    def bubble_sort_cart(self, key='Цена', reverse=False):
        if not self.cart_storage:
            print(f'Корзина пуста!')
            return
        items = list(self.cart_storage.values())
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                val1 = self._convert_value(items[j].get(key, ''))
                val2 = self._convert_value(items[j + 1].get(key, ''))
                if (not reverse and val1 > val2) or (reverse and val1 < val2):
                    items[j], items[j + 1] = items[j + 1], items[j]
        self._update_cart_from_sorted_list(items)
        print(f'Корзина отсортирована методом Bubble Sort по полю: {key}')

    def _convert_value(self, value):
        if isinstance(value, (int, float)):
            return value
        try:
            return float(value) if '.' in str(value) else int(value)
        except (ValueError, TypeError):
            return str(value)

    def _update_cart_from_sorted_list(self, sorted_items):
        self.cart_storage.clear()
        for item in sorted_items:
            self.cart_storage[item['id']] = item

    def sort_cart_menu(self):
        if not self.cart_storage:
            print(f'Корзина пуста! Нечего сортировать')
            return

        print(f'=== МЕНЮ СОРТИРОВКИ КОРЗИНЫ ===')
        print(f'Выберите поле для сортировки: ')
        print(f'1. Цена')
        print(f'2. Вес')
        print(f'3. Категория')
        print(f'4. Название')

        field_choice = input('Введите номер поля: ').strip()
        field_map = {'1': 'Цена', '2': 'Вес', '3': 'Категория', '4': 'Название'}
        field = field_map.get(field_choice, 'Цена')

        print(f'Выберите порядок сортировки: ')
        print(f'1. По возрастанию')
        print(f'2. По убыванию')

        order_choice = input('Введите номер порядка: ').strip()
        reverse = order_choice == '2'

        print(f'Выберите алгоритм сортировки: ')
        print(f'1. Bubble Sort (пузырьком)')
        print(f'2. Insertion Sort (вставками)')
        print(f'3. Quick Sort (быстрая)')
        print(f'4. Merge Sort (слиянием)')

        algo_choice = input('Введите номер алгоритма: ').strip()

        if algo_choice == '1':
            self.bubble_sort_cart(field, reverse)
        # elif algo_choice == '2':
        #     self.insertion_sort_cart(field, reverse)
        # elif algo_choice == '3':
        #     self.quick_sort_cart(field, reverse)
        # elif algo_choice == '4':
        #     self.merge_sort_cart(field, reverse)
        else:
            print(f'Неверный выбор алгоритма!')

        self.show_cart()


    # Для просмотре текущего состояния хранилиша карточек с товаром
    def seeing(self):
        print(self.storage)
        print(self.cart_storage)


if __name__ == "__main__":
    product = Product()
    while True:
        print(f'\n=== МАГАЗИН ТОВАРОВ ===')
        print(f'1. Каталог')
        print(f'2. Добавить карточку товара')
        print(f'3. Изменить карточку товара')
        print(f'4. Удалить карточку товара')
        print(f'5. Добавить товары в корзину')
        print(f'6. Посмотреть корзину')
        print(f'7. Удалить товары из корзины')
        print(f'8. Меню сортировки корзины')
        print(f'9. Покинуть магазин товаров')
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
            product.sort_cart_menu()
        elif pick == '9':
            print(f'Мы будем скучать без тебя Наш верный покупатель!')
            break
        elif pick == '10':
            product.seeing()