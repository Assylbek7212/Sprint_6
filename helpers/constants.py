import random

url = 'https://qa-scooter.praktikum-services.ru/'
yandex_main = 'https://dzen.ru/?yredirect=true'

answer_to_question0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
answer_to_question1 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
answer_to_question2 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
answer_to_question3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
answer_to_question4 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
answer_to_question5 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
answer_to_question6 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
answer_to_question7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

answer_to_questions = [
    answer_to_question0,
    answer_to_question1,
    answer_to_question2,
    answer_to_question3,
    answer_to_question4,
    answer_to_question5,
    answer_to_question6,
    answer_to_question7
]

names = ["Алиса", "Лика", "Маша", "Пуговка", "Даша", "Галя", "Женя"]

def generate_random_name():
    return random.choice(names)

lastname = ["Иванова", "Ахматова", "Достоевская", "Васнецова", "Генадьева", "Чехова", "Каренина"]

def generate_random_lastname():
    return random.choice(lastname)

address = ["Москва", "Саратов", "Красноярс", "Казань", "Архангельск", "Барнаул", "Астрахань"]

def generate_random_address():
    return random.choice(address)

stmetro = ["Черкизовская", "Бульвар Рокоссовского", "Сокольники", "Лубянка"]
def generate_random_stmetro():
    return random.choice(stmetro)

def generate_random_phone_number():
    country_code = "+7"
    area_code = str(random.randint(100, 999))
    first_part = str(random.randint(100, 999))
    second_part = str(random.randint(1000, 9999))

    phone_number = f"{country_code}{area_code}{first_part}{second_part}"
    return phone_number

name_form = generate_random_name()
lastname_form = generate_random_lastname()
address_form = generate_random_address()
number_form = generate_random_phone_number()

comment_form = 'test form'

success_text = 'Заказ оформлен'