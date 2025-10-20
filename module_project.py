from unicodedata import category


class Product:
    def __init__(self):
        self.storage = {}
        self.id = 1

    def info_storage(self):
        if not self.storage:
            print(f'Каталог товаров пуст!')
        else:
            print('-' * 100)
            print(f'{'ID'} - {'Название' : <15} - {'Цена' : <8} - {'Вес' : <6} - {'Категория' : <12} - {'Описние' : <20}')
            print('-' * 100)
            for prod in self.storage.values():
                print(f'{prod['id'] : <3}. {prod['Название'] : <15} - {prod['Цена'] : <8} - {prod['Вес'] : <6} - {prod['Категория'] : <12} - {prod['Описание'] : <20}')
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
        pass

    def remove_product(self):
        try:
            remove_id = int(input(f'Введите id карточка товара, которую хотите удалить: '))
            if remove_id in self.storage:
                del self.storage[remove_id]
                print(f'Карточка товара c ID {remove_id} удалена')
            else:
                print(f'Карточка товара c ID {remove_id} не найдена')
        except ValueError:
            print(f'Ошибка ввода. Введите корректный числовой ID')


    # Для просмотре текущего состояния хранилиша карточек с товаром
    def seeing(self):
        print(self.storage)


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
        print(f'5. Покинуть магазин товаров')
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
            print(f'Мы будем скучать без тебя Наш верный покупатель!')
            break
        elif pick == '9':
            product.seeing()