
INSTALL
------------
Run requirements::

    $ virtualenv --python=python3.12 .venv
	$ source .venv/bin/activate 
    $ pip3 install -r requirements.txt

RUN
------------
    $ python3 task_1.py
	$ python3 task_2.py
	$ python3 task_3.py


# Завдання 1

Код виконується і повертає максимальну можливу загальну кількість вироблених продуктів "Лимонад" та "Фруктовий сік", враховуючи обмеження на кількість ресурсів.

# Завдання 2

Програмно реалізовано алгоритм пошуку визначеного інтеграла за допомогою методу Монте-Карло. Код виконується та повертає значення інтеграла.

Виконано порівняльний аналіз результату, отриманого за допомогою алгоритму, з результатом, отриманим аналітично або за допомогою функції quad з підмодуля integrate бібліотеки SciPy.

Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих результатів і результатів, які дає функція quad або аналітичне обчислення інтеграла. Висновки оформлено у вигляді файлу readme.md домашнього завдання.


## Висновки

Обчислено значення інтегралу двома методами: 
- методом Монте-Карло
- за допомогою функції `quad` з підмодуля `integrate` бібліотеки `SciPy`.

Результати проведених обчислень:

> Знаходження значення інтеграла методом Монте-Карло:\
> 1000 зразків - 2.63372468

> Знаходження значення інтеграла методом Монте-Карло:\
> 10000 зразків - 2.72299797

> Перевірка обчисленнь за допомогою функції `quad`: 2.66666667

Як видно із результатів обчислень, наведених вище, точність розрахунку є досить високою, навіть при невеликому обсязі точок.

Отже, метод Монте-Карло, який використовує випадковість та ймовірність для розв’язання проблем, найкраще підходить у випадках, які можуть бути складними або неможливими для точного розв'язання традиційними методами. Цей метод дуже ефективний, коли прямі обчислення надто складні або ресурсоємні.