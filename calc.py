import customtkinter

customtkinter.set_appearance_mode("dark")

# window settings
display = customtkinter.CTk()
display.geometry("493x610")
display.title("iPhone Calculator")
display.resizable(False, False)


def evaluate():
    equation = output.get()
    try:
        result = eval(equation)
        if isinstance(result, float):
            result = round(result, 6)
        output.delete(0, "end")
        output.insert(0, str(result))
    except Exception as e:
        output.delete(0, "end")
        output.insert(0, "Error")


# output box
output = customtkinter.CTkEntry(
    display,
    width=450,
    height=80,
    corner_radius=0,
    fg_color="#242424",
    font=(("Helvetica", 60)),
    justify="right",
    border_width=0,
)
output.grid(row=0, column=0, columnspan=4, padx=10, pady=30)


# number buttons
btn1 = customtkinter.CTkButton(
    display,
    text="1",
    command=lambda: output.insert("end", 1),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=("arial", 30),
)
btn1.grid(row=2, column=0, padx=10, pady=5)

btn2 = customtkinter.CTkButton(
    display,
    text="2",
    command=lambda: output.insert("end", 2),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn2.grid(row=2, column=1, padx=0, pady=5)

btn3 = customtkinter.CTkButton(
    display,
    text="3",
    command=lambda: output.insert("end", 3),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn3.grid(row=2, column=2, padx=10, pady=5)

btn4 = customtkinter.CTkButton(
    display,
    text="4",
    command=lambda: output.insert("end", 4),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn4.grid(row=3, column=0, padx=0, pady=5)

btn5 = customtkinter.CTkButton(
    display,
    text="5",
    command=lambda: output.insert("end", 5),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn5.grid(row=3, column=1, padx=10, pady=5)

btn6 = customtkinter.CTkButton(
    display,
    text="6",
    command=lambda: output.insert("end", 6),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn6.grid(row=3, column=2, padx=0, pady=5)

btn7 = customtkinter.CTkButton(
    display,
    text="7",
    command=lambda: output.insert("end", 7),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn7.grid(row=4, column=0, padx=10, pady=5)

btn8 = customtkinter.CTkButton(
    display,
    text="8",
    command=lambda: output.insert("end", 8),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn8.grid(row=4, column=1, padx=0, pady=5)

btn9 = customtkinter.CTkButton(
    display,
    text="9",
    command=lambda: output.insert("end", 9),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn9.grid(row=4, column=2, padx=10, pady=5)

btn0 = customtkinter.CTkButton(
    display,
    text="0",
    command=lambda: output.insert("end", 0),
    corner_radius=40,
    width=220,
    height=80,
    fg_color="#333333",
    font=(("arial", 30)),
)
btn0.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# function buttons
btnAC = customtkinter.CTkButton(
    display,
    text="C",
    command=lambda: output.delete("0", "end"),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#a5a5a5",
    font=("arial", 30),
)
btnAC.grid(row=1, column=0, padx=10, pady=5)


def toggle_plus_minus():
    current_text = output.get().strip()
    if current_text:
        try:
            current_number = int(current_text)
            current_number = -current_number
            output.delete(0, "end")
            output.insert(0, str(current_number))

        except ValueError:
            pass


btn_plusminus = customtkinter.CTkButton(
    display,
    text="+/-",
    command=toggle_plus_minus,
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#a5a5a5",
    font=("arial", 20),
)
btn_plusminus.grid(row=1, column=1, padx=10, pady=5)


def toggle_percent():
    current_text = output.get().strip()
    if current_text:
        try:
            current_number = float(current_text)
            current_number = current_number / 100
            output.delete("0", "end")
            output.insert("0", str(current_number))

        except ValueError:
            pass


btn_percent = customtkinter.CTkButton(
    display,
    text="%",
    command=toggle_percent,
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#a5a5a5",
    font=("arial", 20),
)
btn_percent.grid(row=1, column=2, padx=10, pady=5)

btndivide = customtkinter.CTkButton(
    display,
    text="÷",
    command=lambda: output.insert("end", " / "),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#ff9f0b",
    font=("arial", 40),
)
btndivide.grid(row=1, column=3, padx=10, pady=5)

btn_decimal = customtkinter.CTkButton(
    display,
    text=".",
    command=lambda: output.insert("end", "."),
    corner_radius=40,
    width=100,
    height=80,
    fg_color="#333333",
    font=(("arial", 40)),
)
btn_decimal.grid(row=5, column=2, padx=0, pady=5)

btn_plus = customtkinter.CTkButton(
    display,
    text="+",
    command=lambda: output.insert("end", " + "),
    corner_radius=40,
    width=100,
    height=80,
    fg_color="#ff9f0b",
    font=(("arial", 40)),
)
btn_plus.grid(row=2, column=3, padx=10, pady=5)

btn_subtract = customtkinter.CTkButton(
    display,
    text="-",
    command=lambda: output.insert("end", " - "),
    corner_radius=40,
    width=100,
    height=80,
    fg_color="#ff9f0b",
    font=(("arial", 40)),
)
btn_subtract.grid(row=3, column=3, padx=0, pady=5)

btn_multiply = customtkinter.CTkButton(
    display,
    text="x",
    command=lambda: output.insert("end", " * "),
    corner_radius=40,
    width=80,
    height=80,
    fg_color="#ff9f0b",
    font=(("arial", 40)),
)
btn_multiply.grid(row=4, column=3, padx=10, pady=5)

btn_equal = customtkinter.CTkButton(
    display,
    text="=",
    command=evaluate,
    corner_radius=40,
    width=100,
    height=80,
    fg_color="#ff9f0b",
    font=(("arial", 40)),
)
btn_equal.grid(row=5, column=3, padx=0, pady=5)

display.mainloop()
