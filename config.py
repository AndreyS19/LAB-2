from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
vvodtype=KeyboardButton('Ввести тип')
vvodname=KeyboardButton('Ввести имя')
zapis=KeyboardButton('Подтвердить участие')
provzapis=KeyboardButton('Проверить запись')
mar=KeyboardButton('Марафон')
halfmar=KeyboardButton('Полумарафон')
tenkil=KeyboardButton('10000 метров')
otherMenu=ReplyKeyboardMarkup().add(vvodtype,vvodname,zapis,provzapis)
runMenu=ReplyKeyboardMarkup().add(halfmar,tenkil,mar)



