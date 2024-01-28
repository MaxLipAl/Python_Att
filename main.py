# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список
# заметок, редактировать заметку, удалять заметк

import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    # Загрузка заметок из файла JSON
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    # Сохранение заметок в файл JSON
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=2)

def show_notes():
    # Вывод списка заметок
    notes = load_notes()
    if not notes:
        print("Нет сохраненных заметок.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата/время: {note['timestamp']}")
            print(note['body'])
            print("-" * 30)

def add_note():
    # Добавление новой заметки
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")

    notes = load_notes()
    new_note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": str(datetime.now())
    }
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def edit_note():
    # Редактирование существующей заметки
    notes = load_notes()
    show_notes()

    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Новый заголовок заметки: ")
            note['body'] = input("Новый текст заметки: ")
            note['timestamp'] = str(datetime.now())
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return

    print("Заметка с указанным ID не найдена.")

def delete_note():
    # Удаление существующей заметки
    notes = load_notes()
    show_notes()

    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return

    print("Заметка с указанным ID не найдена.")

def main():
    # Основная функция, управляющая работой приложения
    while True:
        print("\n===== КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ ЗАМЕТКИ =====")
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            show_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Пока!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 5.")

if __name__ == "__main__":
    main()