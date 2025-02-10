## Описание проекта: ##
Виджет банковских операций. Выпоняет 2 функции:
- Фильтрация по результату выполнения операции (выполнена, отклонена).
- Сортировка банковских операций по дате выполнения.

## Установка ##
1. Клонируйте проект в свой репозиторий по ссылке:
```
git clone git@github.com:DashulyaE/homework_10.git
```
2. Зайдите в модуль *processing.py* и внесите необходимые данные в переменные, например:
 ```
choose_state = "CANCELED"
sort_date = False
```
3. Запустите файл *main.py* в терминале.
## Результат работы программы ##
В результате запуска модуля main.py в окне должны появится 2 списка с результатами работы двух функций:
1. Список банковских операций, отфильтрованный по результату выполнения операций.
2. Список банковских операций, отсортированных по дате их выполнения
