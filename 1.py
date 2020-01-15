import subprocess
import chardet
import locale

# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.
STR_1 = 'разработка'
STR_2 = 'сокет'
STR_3 = 'декоратор'
print(STR_1)
print(type(STR_1))
print(STR_2)
print(type(STR_2))
print(STR_3)
print(type(STR_3))

STR_1_U = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
STR_2_U = '\u0441\u043e\u043a\u0435\u0442'
STR_3_U = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(STR_1_U)
print(type(STR_1_U))
print(STR_2_U)
print(type(STR_2_U))
print(STR_3_U)
print(type(STR_3_U))

# 2. Каждое из слов «class», «function», «method» записать в байтовом типе
# без преобразования в последовательность кодов (не используя методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.
STR_4 = b'\u0063\u006c\u0061\u0073\u0073'
STR_5 = b'\u0066\u0075\u006e\u0063\u0074\u0069\u006f\u006e'
STR_6 = b'\u006d\u0065\u0074\u0068\u006f\u0064'

print(STR_4)
print(type(STR_4))
print(len(STR_4))
print(STR_5)
print(type(STR_5))
print(len(STR_5))
print(STR_6)
print(type(STR_6))
print(len(STR_6))

# 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
STR_7 = b'attribute'
print(type(STR_7))
# STR_7 = b'класс'   НЕЛЬЗЯ
# STR_7 = b'функция'   НЕЛЬЗЯ
STR_7 = b'type'
print(type(STR_7))

# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
STR_8 = 'разработка'
STR_8_ENC = STR_8.encode('utf-8')
print(STR_8_ENC)
STR_8_DEC = STR_8_ENC.decode('utf-8')
print(STR_8_DEC)

STR_9 = 'администрирование'
STR_9_ENC = STR_9.encode('utf-8')
print(STR_9_ENC)
STR_9_DEC = STR_9_ENC.decode('utf-8')
print(STR_9_DEC)

STR_10 = 'protocol'
STR_10_ENC = STR_10.encode('utf-8')
print(STR_10_ENC)
STR_10_DEC = STR_10_ENC.decode('utf-8')
print(STR_10_DEC)

STR_11 = 'standard'
STR_11_ENC = STR_11.encode('utf-8')
print(STR_11_ENC)
STR_11_DEC = STR_11_ENC.decode('utf-8')
print(STR_11_DEC)

# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
ARGS = ['ping', 'yandex.ru']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))


ARGS = ['ping', 'youtube.com']
YA_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
for line in YA_PING.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.

F_N = open('test_file.txt', 'w', encoding='utf-8')
F_N.write('сетевое программирование сокет декоратор')
F_N.close()

def_enc = locale.getpreferredencoding()
print(def_enc)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')