1.	Исходный код задач представлен в директориях SimpleTasks, MediumTasks, HardTasks и HardestTasks для каждого типа задач соответственно.
2.	Приложения написаны на Python 3, поэтому, запуск приложений возможен
    •	Из консоли с помощью интерпретатора Python 3 (python filename.py)
    •	Удобный запуск через IDE PyCharm из данного проекта
Для запуска задачи с веб-сервером необходимо установить библиотеки:
    •	Flask
    •	Json
    •	Asyncio
    •	BS4
Простые задачи:
•	Программа, возвращающая 2-й по величине элемент набора чисел.
    (S1)
    Тестирование:
    Проверка на то, что введено корректное число исходных данных (введено больше двух чисел разделенных пробелом)
    Проверка на то, что введены именно числа, а не произвольные строки
    Проверка алгоритма на тестовых данных
•	Программа, выполняющая разложение числа на набор простых множителей̆
    (S2)
    Тестирование:
    Проверка на то, что введено число, а не произвольные символы
    Число больше 1
    Проверка алгоритма на тестовых данных
•	Программа, выполняющая проверку строки на то, что она является палиндромом (S3)
    Тестирование:
    Проверка на то, что введены данные
    Проверка алгоритма на тестовых данных
•	Программа, выполняющая поиск подстроки в строке.
    (S5)
    Тестирование:
    Проверка на то, что введены данные
    Проверка алгоритма на тестовых данных
    Задачи средней сложности:
•	Программа, возвращающая n-й по величине элемент набора чисел.  (M1)
    Тестирование:
    Проверка на то, что введены именно числа, а не произвольные строки
    Проверка индекса <= длины массива
    Проверка алгоритма на тестовых данных
•	Программа, выполняющая Run-length encoding кодирование строки (aaabccdd -> 3a1b2c2d)
    Тестирование:
    Проверка введения данных
    Проверка алгоритма на тестовых данных
•	Программа выполняющая Run-length encoding декодирование строки (3a1b2c2d->aaabccdd).
    Тестирование:
    Проверка введения данных
    Проверка алгоритма на тестовых данных
Задача высокой сложности:
    Тестирование:
    •	Проверка передачи параметра имени файла из консоли
    •	Проверка чтения из файла
    •	Проверка корректного распознания команд
    •	Проверка работы каждого из алгоритмов на тестовых данных
    •	Проверка записи результатов работы в файл

    Ответы на вопросы:
    •	Файл может содержать большое количество строк. Данная проблема частично решается подходом в моей программе – построчным чтением. При таком подходе будет более оптимальное использование памяти. Однако, при такой реализации более сложно разбить на потоки решение задачи. Для разбиения на потоки можно было бы читывать файл блоками и сразу же писать блоками.
    •	Программа поддерживает расширяемость количества ф-ий, так как все они динамически выбираются из словаря, размер которого легко может быть увеличен.
    •	Количество операндов также без проблем может быть увеличено, так как они передаются массивом и алгоритм сам решает, сколько ему нужно данных.
    •	Основные предположения – первый аргумент в файле – название алгоритма, если алгоритма для аргумента нет – произойдет ошибка. Также сделано предположение о том, что аргументы по умолчанию не могут содержать пробелы – пробел является разделителем, а файл расположен рядом с исполняемым файлом. Еще одним минусом является тот факт, что приложение работает в один поток.
Задача самой высокой сложности:
    При реализации задачи мной было обнаружено, что указанный в задании адрес API более не поддерживается Яндекс, поэтому, мной было взято другое решение от Яндекс – поиск Яндекс.XML. (xml.yandex.ru)
    Необходимые для работы данные – имя пользователя и ключ API указываются в файле config_file.json. Там же можно указать порт работы веб сервера и ограничить максимальное количество одновременных подключений к API Яндекс
    Запускать следует файл app.py
    Также в папке находится файл 1.xml и код по его чтению для проверки работы алгоритма без обращения к API Яндекс.
        Тестирование:
    •	Проверка запуска веб сервера на нужном порту
    •	Проверка обработки GET запросов по адресу /search
    •	Проверка чтения аргументов запроса
    •	Проверка запросов к API Яндекс – сверка с результатами из Postman
    •	Проверка корректной обработки результатов – проверка с собственно полученными результатами
    •	Проверка возврата json ответа сервером
    •	Проверка работы сервера при большом количестве запросов
    •	Проверка отсутствия поисковых запросов при запросе /search
    •	Проверка параллельности выполнения запросов к Яндекс
    •	Проверка ограничений на количество соединений
    Ответы на доп задания:
    1.	Русский язык поддерживается в кодировке UTF-8.
    2.	Запросы выполняются параллельно (однако, проверить нормально не получилось из-за ограничений по количеству запросов от Яндекс)
    3.	Ограничение на количество запросов присутствует
    4.	Выдача отформатирована pretty print.





