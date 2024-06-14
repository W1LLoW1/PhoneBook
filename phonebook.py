import tkinter as tk
from tkinter import messagebox

def read_txt(filename): 

    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def print_result(phone_book, root):
    result_window = tk.Toplevel(root)
    result_window.title("Справочник")
    text = tk.Text(result_window)
    for contact in phone_book:
        formatted_contact = f"Фамилия: {contact.get('Фамилия', 'N/A')}, Имя: {contact.get('Имя', 'N/A')}, Телефон: {contact.get('Телефон', 'N/A')}, Описание: {contact.get('Описание', 'N/A')}"
        text.insert(tk.END, formatted_contact + '\n')
    text.pack()

def find_by_lastname(phone_book, last_name):
    return [contact for contact in phone_book if contact['Фамилия'] == last_name]

def change_number(phone_book,last_name,new_number):
    update_number = []
    found = False
    for contact in phone_book:
        if contact['Фамилия'] == last_name:
            contact['Телефон'] = new_number
            found = True
    if not found:
        return "Контакт не найден"
    return 'Контакт обновлен'

def delete_by_lastname(phone_book,lastname):
    check_length = len(phone_book)
    phone_book[:] = [contact for contact in phone_book if contact['Фамилия'] != lastname]
    if len(phone_book) == check_length:
        return "Контакт не найден"
    return "Контакт удален"

def find_by_number(phone_book,number):
    return [contact for contact in phone_book if contact ['Телефон'] == number]

def add_user(phone_book,user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
    phone_book.append(record)
    return "Контакт добавлен"

def write_txt(filename , phone_book):

    with open(filename,'w',encoding='utf-8') as phout:
        for contact in phone_book:
            phout.write(','.join(contact.values()) + '\n')

def work_with_phonebook():
    phone_book=read_txt('phon.txt')
    
    def show_all():
        print_result(phone_book, root)
    
    def find_by_last_name_action():
        last_name = entry_lastname.get()
        result = find_by_lastname(phone_book, last_name)
        if result:
            result_window = tk.Toplevel(root)
            result_window.title("Найденные контакты")
            text = tk.Text(result_window)
            for contact in result:
                formatted_contact = f"Фамилия: {contact.get('Фамилия', 'N/A')}, Имя: {contact.get('Имя', 'N/A')}, Телефон: {contact.get('Телефон', 'N/A')}, Описание: {contact.get('Описание', 'N/A')}"
                text.insert(tk.END, formatted_contact + '\n')
            text.pack()
        else:
            messagebox.showinfo('Результат', 'Контакт не найден')

    def change_number_action():
        last_name = entry_lastname.get()
        new_number = entry_lastname.get()
        result = change_number(phone_book, last_name, new_number)
        messagebox.showinfo('Результат', result)
        write_txt('phonebook.txt', phone_book)

    def delete_by_lastname_action():
        lastname = entry_number.get()
        result = delete_by_lastname(phone_book, lastname)
        messagebox.showinfo('Результат', result)
        write_txt('phonebook.txt', phone_book)

    def find_by_number_action():
        number = entry_number.get()
        result = find_by_number(phone_book, number)
        if result:
            result_window = tk.Toplevel(root)
            result_window.title("Найденные контакты")
            text = tk.Text(result_window)
            for contact in result:
                text.insert(tk.END, str(contact) + '\n')
            text.pack()
        else:
            messagebox.showinfo('Результат', "Контакт не найден")

    def add_user_acition():
        user_data = entry_user_data.get()
        result = add_user(phone_book, user_data)
        messagebox.showinfo('Результат', result)
        write_txt('phonebook.txt', phone_book)

    root = tk.Tk()
    root.title("Телефонная книга")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    button_show_all = tk.Button(frame, text="Отобразить весь справочник", command=show_all)
    button_show_all.grid(row=0, column=0, padx=10, pady=5)

    label_lastname = tk.Label(frame, text='Фамилия')
    label_lastname.grid(row=1, column=0, padx=10, pady=5)
    entry_lastname = tk.Entry(frame)
    entry_lastname.grid(row=1, column=1, padx=10, pady=5)

    button_find_by_lastname = tk.Button(frame, text='Найти контакт по фамилии', command=find_by_last_name_action)
    button_find_by_lastname.grid(row=2,column=0,columnspan=2,padx=10,pady=5)

    button_change_number = tk.Button(frame, text='Изменить номер по фамилии', command=change_number_action)
    button_change_number.grid(row=3,column=0,columnspan=2,padx=10,pady=5)

    button_delete_by_lastname = tk.Button(frame, text='Удалить номер по фамилии', command = delete_by_lastname_action)
    button_delete_by_lastname.grid(row=4,column=0,columnspan=2,padx=10,pady=5)

    label_number = tk.Label(frame, text='Номер')
    label_number.grid(row=5,column=0,padx=10,pady=5)
    entry_number = tk.Entry(frame)
    entry_number.grid(row=5,column=1,padx=10,pady=5)

    button_find_by_number = tk.Button(frame, text='Найти контакт по номеру', command= find_by_number_action)
    button_find_by_number.grid(row=6, column=0,columnspan=2,padx=10,pady=5)

    label_user_data = tk.Label(frame, text='Новые данные (Фамилия, Имя, Телефон, Описание)')
    label_user_data.grid(row=7, column=0, padx=10, pady=5)
    entry_user_data = tk.Entry(frame)
    entry_user_data.grid(row=7,column=1,padx=10,pady=5)

    label_line_number = tk.Label(frame, text= 'Номер строки для копирования')
    label_line_number.grid(row=9, column=0, padx=10, pady=5)
    entry_line_number = tk.Entry(frame)
    entry_line_number.grid(row=9,column=1,padx=10,pady=5)

    button_add_user = tk.Button(frame, text='Добавить новый контакт', command=add_user_acition)
    button_add_user.grid(row=8,column=0,columnspan=2,padx=10,pady=5)

    button_exit = tk.Button(frame, text='Выход', command=root.quit)
    button_exit.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

work_with_phonebook()