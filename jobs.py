import tkinter
# features:
# number of companies and number of jobs total
# database..?
# django..?


def insert():
    with open('jobs.csv', 'a', encoding='UTF-8') as file:
        file.write(f'\n"{company_field.get()}","{position_field.get()}","{oa_field.get()}","{rejected_field.get()}","{number_field.get()}"')

    clear()


def clear():
    company_field.delete(0, tkinter.END)
    position_field.delete(0, tkinter.END)
    oa_field.delete(0, tkinter.END)
    rejected_field.delete(0, tkinter.END)
    number_field.delete(0, tkinter.END)


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title('Insert Job')

    company = tkinter.Label(root ,text = "Company").grid(row = 0,column = 0)
    position = tkinter.Label(root ,text = "Position(s)").grid(row = 1,column = 0)
    oa = tkinter.Label(root ,text = "OA?").grid(row = 2,column = 0)
    rejected = tkinter.Label(root ,text = "Rejected?").grid(row = 3,column = 0)
    number = tkinter.Label(root ,text = "Number").grid(row = 4,column = 0)

    company_field = tkinter.Entry(root)
    company_field.grid(row = 0,column = 1)
    position_field = tkinter.Entry(root)
    position_field.grid(row = 1,column = 1)
    oa_field = tkinter.Entry(root)
    oa_field.grid(row = 2,column = 1)
    rejected_field = tkinter.Entry(root)
    rejected_field.grid(row = 3,column = 1)
    number_field = tkinter.Entry(root)
    number_field.grid(row = 4,column = 1)

    submit = tkinter.Button(root, text="Submit", command=insert).grid(row = 5,column = 0)

    root.mainloop()