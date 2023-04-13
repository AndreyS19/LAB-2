from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu=KeyboardButton('Главное меню')
zabeg=KeyboardButton('Записаться на марафон')
vvodtype=KeyboardButton('Ввести тип')
vvodname=KeyboardButton('Ввести имя')
proverka=KeyboardButton('Подтвердить участие')
mar=KeyboardButton('Марафон')
halfmar=KeyboardButton('Полумарафон')
tenkil=KeyboardButton('10000 метров')
otherMenu=ReplyKeyboardMarkup().add(vvodtype,vvodname,menu,proverka)
runMenu=ReplyKeyboardMarkup().add(halfmar,tenkil,mar)
mainMenu=ReplyKeyboardMarkup().add(zabeg)


