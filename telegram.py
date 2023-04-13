from aiogram import Bot, Dispatcher, executor, types
from openpyxl.reader.excel import load_workbook
import config as nav
def botik():
    global schet
    global bufname
    bufname=''
    BOT_TOKEN='6024152220:AAHt7nUYHdf_fHSCjUHYd9NYL_yg77OrWas'
    bot =Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    @dp.message_handler(commands=['start'])
    async def send_welcome(message: types.Message):
        await bot.send_message(message.from_user.id,"Привет! нажми кнопку записи в меню или кнопку проверку записи, чтобы узнать записан ли ты", reply_markup=nav.mainMenu)
    @dp.message_handler(text=['Главное меню'])
    async def send_message(message: types.Message):
        await bot.send_message(message.from_user.id, 'принял',reply_markup=nav.mainMenu)
    @dp.message_handler(text='Записаться на марафон')
    async def send_message(message: types.Message):
        await bot.send_message(message.from_user.id,'введите свои данные', reply_markup=nav.otherMenu)
    @dp.message_handler(text=['Ввести тип'])
    async def send_message(message: types.Message):
        await bot.send_message(message.from_user.id, 'введите тип марафона', reply_markup=nav.runMenu)
    @dp.message_handler(text=['Подтвердить участие'])
    async def send_message(message: types.Message):
        try:
            row = (name, type)  # <--- новая строка
            fn = r"C:\Users\msiuser\PycharmProjects\лаба2\laba2.xlsx"
            wb = load_workbook(fn)
            ws = wb["Sheet1"]
            ws.append(row)
            wb.save(fn)
            wb.close()
            await bot.send_message(message.from_user.id, 'вы записаны', reply_markup=nav.mainMenu)
        except:
            print('не все данные введены')
            await bot.send_message(message.from_user.id, 'не все данные введены')

    @dp.message_handler()
    async def send_message(message: types.Message):
        if message.text=='Марафон':
            global type
            type=message.text
            await bot.send_message(message.from_user.id, 'принял', reply_markup=nav.otherMenu)
        elif message.text=='Полумарафон':
            type = message.text
            await bot.send_message(message.from_user.id, 'принял', reply_markup=nav.otherMenu)
        elif message.text=='10000 метров':
            type = message.text
            await bot.send_message(message.from_user.id, 'принял', reply_markup=nav.otherMenu)
        elif message.text=='Ввести имя':
            global bufname
            bufname=message.text
            await bot.send_message(message.from_user.id, 'Вводите имя',reply_markup=types.ReplyKeyboardRemove())
        elif bufname=='Ввести имя':
            global name
            name = message.text
            bufname=''
            await bot.send_message(message.from_user.id, 'принял', reply_markup=nav.otherMenu)
        else:
            await bot.send_message(message.from_user.id, 'выберите что-нибудь')

    executor.start_polling(dp, skip_updates=True)