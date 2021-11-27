import telebot
import config
import dbworker
# Создание бота
bot = telebot.TeleBot(config.TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    dbworker.set(dbworker.make_key("STATE_FIRST_NUM", config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    return True

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    dbworker.set(dbworker.make_key("STATE_FIRST_NUM", config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)


# Обработка первого числа
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key("STATE_FIRST_NUM", config.CURRENT_STATE)) == config.States.STATE_FIRST_NUM.value)
def first_num(message):
    if not message.isdigit():
        return None
    else:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key("STATE_SECOND_NUM", config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key("first", config.States.STATE_FIRST_NUM.value), message)
    return message


# Обработка второго числа
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key("STATE_SECOND_NUM", config.CURRENT_STATE)) == config.States.STATE_SECOND_NUM.value)
def second_num(message):
    if not message.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        return None
    else:
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key("STATE_OPERATION", config.CURRENT_STATE), config.States.STATE_OPERATION.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key("second", config.States.STATE_SECOND_NUM.value), message)
    return message
       


# Выбор действия
@bot.message_handler(func=lambda message: dbworker.get(dbworker.make_key("STATE_OPERATION", config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
def operation(message):
    # Текущее действие
    op = message
    # Читаем операнды из базы данных
    v1 = dbworker.get(dbworker.make_key("first", config.States.STATE_FIRST_NUM.value))
    v2 = dbworker.get(dbworker.make_key("second", config.States.STATE_SECOND_NUM.value))
    # Выполняем действие
    fv1 = float(v1)
    fv2 = float(v2)
    res = None

    try:
        if op == '+':
            res = fv1 + fv2
        elif op == '*':
            res = fv1 * fv2
        elif op == '-':
            res = fv1 - fv2
        else:
            res = fv1 / fv2
            res = f'{res:.2f}'
    except:
        pass

    return res