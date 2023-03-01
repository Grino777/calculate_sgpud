from tkinter import *
from tkinter import ttk

def calculate(a, b):
    if a < b:
        a, b = b, a
    return round(float((a / b - 1) * 100), 2)


def check_float(field: Entry):
    try:
        if field['background'] == '#ffaaaa' and field.get() != '':
            field['background'] = '#ffffff'
        return float(field.get())
    except ValueError:
        field['background'] = '#ffaaaa'
        return 0


def get_entry_data(entry_data: list):
    field: Entry
    data = []
    for field in entry_data:
        data.append(check_float(field))
    return data


def press_res_button():
    data_before = get_entry_data(before_entry_objects)
    data_after = get_entry_data(after_entry_objects)
    for i, v in enumerate(list(zip(data_before, data_after))):
        result_entry_objects[i].delete(0, END)
        if 0 in v:
            result_entry_objects[i]['background'] = '#ffaaaa'
        else:
            result_entry_objects[i].insert(0, string=str(calculate(*v)))
            result_entry_objects[i]['background'] = '#ffffff'


root = Tk()
root.title('СГПУД-50А')
root.geometry('500x400')

# notebook = ttk.Notebook()
# notebook.grid(row=20, column=20)
#
# frame_1 = ttk.Frame(notebook)
# frame_2 = ttk.Frame(notebook)
#
# frame_1.grid(row=21, column=20)
# frame_2.grid(row=22, column=20)
#
# notebook.add(frame_1, text='Полный расчет')
# notebook.add(frame_2, text='Короткий расчет')



before_text = Label(text='До испытания')
before_text.grid(row=0, column=1)

after_text = Label(text='После испытания')
after_text.grid(row=0, column=3)

result_text = Label(text='Результат, %')
result_text.grid(row=0, column=5)

text = ['R1-1', 'R1-2', 'R1-3', 'R1-4', 'R2-1', 'R2-2', 'R2-3', 'R2-4', 'R3-1', 'R3-2', 'R3-3', 'R3-4', 'R4-1', 'R4-2',
        'R4-3', 'R4-4']
before_entry_objects = [Entry(width=10) for i in range(len(text))]
before_label_objects = [Label(width=7, text=i) for i in text]

for i in range(16):
    before_label_objects[i].grid(row=i + 1, column=0)
    before_entry_objects[i].grid(row=i + 1, column=1)

after_entry_objects = [Entry(width=10) for i in range(len(text))]
after_label_objects = [Label(width=7, text=i) for i in text]

for i in range(16):
    after_label_objects[i].grid(row=i + 1, column=2)
    after_entry_objects[i].grid(row=i + 1, column=3)

result_entry_objects = [Entry(width=10) for i in range(len(text))]
result_label_objects = [Label(width=7, text=i) for i in text]

for i in range(16):
    result_label_objects[i].grid(row=i + 1, column=4)
    result_entry_objects[i].grid(row=i + 1, column=5)

res_button = Button(text='Рассчитать')
res_button.grid(row=18, column=3, padx=10, pady=10)
res_button['command'] = press_res_button

root.mainloop()
