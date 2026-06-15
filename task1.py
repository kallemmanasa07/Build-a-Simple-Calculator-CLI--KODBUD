import tkinter as tk
from tkinter import messagebox

# ---------------- FUNCTIONS ---------------- #

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace(event=None):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
    return "break"  # Prevent default backspace action

def calculate(event=None):
    try:
        expression = entry.get().strip()

        if not expression:
            return

        result = eval(expression)

        entry.delete(0, tk.END)
        entry.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

    except Exception:
        messagebox.showerror("Error", "Invalid Expression!")

# ---------------- WINDOW ---------------- #

root = tk.Tk()
root.title("Simple Calculator")
root.state("zoomed")  # Full Screen
root.configure(bg="#dfeaf5")

# ---------------- MAIN FRAME ---------------- #

frame = tk.Frame(
    root,
    bg="white",
    bd=5,
    relief="ridge",
    padx=30,
    pady=30
)

frame.place(relx=0.5, rely=0.5, anchor="center")

# ---------------- TITLE ---------------- #

title = tk.Label(
    frame,
    text="Simple Calculator",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="#1f4e79"
)

title.grid(row=0, column=0, columnspan=4, pady=15)

# ---------------- DISPLAY ---------------- #

entry = tk.Entry(
    frame,
    font=("Arial", 24),
    width=20,
    justify="right",
    bd=8
)

entry.grid(row=1, column=0, columnspan=4, padx=10, pady=20)
entry.focus_set()

# ---------------- BUTTONS ---------------- #

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '⌫', '+'],
    ['=']
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):

        if char == "=":
            cmd = calculate
            color = "#28a745"

        elif char == "C":
            cmd = clear
            color = "#dc3545"

        elif char == "⌫":
            cmd = backspace
            color = "#ff9800"

        else:
            cmd = lambda x=char: click(x)
            color = "#1f4e79"

        btn = tk.Button(
            frame,
            text=char,
            command=cmd,
            font=("Arial", 20, "bold"),
            width=5,
            height=2,
            bg=color,
            fg="white"
        )

        if char == "=":
            btn.grid(
                row=r + 2,
                column=0,
                columnspan=4,
                sticky="nsew",
                padx=8,
                pady=8
            )
        else:
            btn.grid(
                row=r + 2,
                column=c,
                padx=8,
                pady=8
            )

# ---------------- KEYBOARD SUPPORT ---------------- #

root.bind("<Return>", calculate)      # Enter key
entry.bind("<BackSpace>", backspace)  # Backspace key

# ---------------- FOOTER ---------------- #

footer = tk.Label(
    root,
    text="Press Enter to Calculate | Backspace to Delete",
    font=("Arial", 12),
    bg="#dfeaf5",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

# ---------------- RUN ---------------- #

root.mainloop()
