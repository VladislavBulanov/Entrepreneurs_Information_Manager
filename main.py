def show_general_information(name, age, phone_number, email, zipcode,
                             address, more_information):
    print(divider)
    if not name:
        print('В базе данных нет личной информации.', end=' ')
        print('Пожалуйста, сначала введите информацию в систему.')
        return False
    else:
        print('Имя:    ', name)
        print('Возраст:', age, end=" ")
        if age % 10 == 1:
            print('год')
        elif 2 <= age % 10 <= 4:
            print('года')
        else:
            print('лет')
        print('Телефон: +7' + phone_number)
        print('E-mail: ', email)
        print('Индекс: ', zipcode)
        print('Адрес:  ', address)
        if more_information:
            print('Дополнительная информация:', more_information)
        return True


def show_business_information(registration_number, individual_taxpayer_number,
                              payment_account, bank, bank_identification_code,
                              correspondent_account):
    if not registration_number:
        print(divider)
        print('В базе данных нет информации о предпринимателе.', end=' ')
        print('Пожалуйста, сначала введите информацию в систему.')
    else:
        print('\nИнформация о предпринимателе')
        print('ОГРНИП:', registration_number)
        print('ИНН:   ', individual_taxpayer_number)
        print('Банковские реквизиты')
        print('Р/с:   ', payment_account)
        print('Банк:  ', bank)
        print('БИК:   ', bank_identification_code)
        print('К/с:   ', correspondent_account)


def no_letter_zipcode(index):
    if index.isdigit():
        return index
    else:
        digital_zipcode = ''
        for symbol in index:
            if symbol.isdigit():
                digital_zipcode += symbol
        return digital_zipcode


name = ''
age = 0
phone_number = ''
email = ''
zipcode = ''
address = ''
more_information = ''
registration_number = 0
individual_taxpayer_number = 0
payment_account = 0
bank = ''
bank_identification_code = 0
correspondent_account = 0
divider = '------------------------------------------'
error_choice_message = '''\nТакого пункта меню не существует.
Пожалуйста, попробуйте выбрать ещё раз.\n'''

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    print(divider)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    user_choice_main_menu = int(input('Введите номер пункта меню: '))
    if not (0 <= user_choice_main_menu <= 2):
        print(error_choice_message)
    elif user_choice_main_menu == 0:
        print('\nРабота программы завершена.')
        print('Спасибо, что выбрали наше приложение!')
        break

    elif user_choice_main_menu == 1:
        while True:
            print(divider)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            user_choice_1 = int(input('Введите номер пункта меню: '))
            if not (0 <= user_choice_1 <= 2):
                print(error_choice_message)
            elif user_choice_1 == 0:
                break

            elif user_choice_1 == 1:
                name = input('Введите имя: ')
                while True:
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    else:
                        print('Введён некорректный возраст. ', end="")
                        print('Пожалуйста, повторите ввод.')
                phone_number = input('Введите номер телефона (+7XXXXXXXXXX): ')
                email = input('Введите адрес электронной почты: ')
                zipcode = no_letter_zipcode(input('Введите почтовый индекс: '))
                address = input('Введите почтовый адрес (без индекса): ')
                more_information = input('Введите дополнительную информацию: ')
                break

            elif user_choice_1 == 2:
                while True:
                    registration_number = int(input('Введите ОГРНИП: '))
                    if len(str(registration_number)) == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр.')
                        print('Пожалуйста, повторите ввод.')
                individual_taxpayer_number = int(input('Введите ИНН: '))
                while True:
                    payment_account = int(input('Введите расчётный счёт: '))
                    if len(str(payment_account)) == 20:
                        break
                    else:
                        print('Расчётный счёт должен содержать 20 цифр.')
                        print('Пожалуйста, повторите ввод.')
                bank = input('Введите название банка: ')
                bank_identification_code = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите корреспондентский счёт: '))

    elif user_choice_main_menu == 2:
        while True:
            print(divider)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            user_choice_2 = int(input('Введите номер пункта меню: '))
            if not (0 <= user_choice_2 <= 2):
                print(error_choice_message)
            elif user_choice_2 == 0:
                break

            elif user_choice_2 == 1:
                show_general_information(name, age, phone_number, email,
                                         zipcode, address, more_information)

            elif user_choice_2 == 2:
                is_continue = show_general_information(name, age, phone_number, email,
                                                       zipcode, address, more_information)
                if is_continue:
                    show_business_information(registration_number, individual_taxpayer_number,
                                              payment_account, bank, bank_identification_code,
                                              correspondent_account)
