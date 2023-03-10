from notes_add import notes_add
from notes_add2 import notes_addContinue
from notes_dateSelect import notes_dateSelect
from notes_delete import notes_delete
from notes_edit import notes_edit
from notes_list import notes_list

print("Добрый день, введите, пожалуйста команду для дальнейшей работы с заметками\n"
      "list - Вывод всех заметок\n"
      "add_New - создание нового файла для заметок (ЗАПИСЫВАТЬСЯ ТОЛЬКО ОДИН РАЗ, ПРИ ДАЛЬНЕЙШЕМ ИСПОЛЬЗОВАНИИ БУДЕТ ПЕРЕЗАПИСЬ)\n"
      "add - создание новой заметки, в существующий файл\n"
      "dateSelect - сортировка по дате\n"
      "delete - удаление заметки по заголовку\n"
      "edit - редактирование заметки\n"
      )
command = input("Введите пожалуйста команду: ")

match command:
    case "list":
        notes_list()
    case "add_New":
        notes_add()
    case "add":
        notes_addContinue()
    case "dateSelect":
        notes_dateSelect()
    case "delete":
        notes_delete()
    case "edit":
        notes_edit()
    case _:
        print("Warring: Неизвестная команда")