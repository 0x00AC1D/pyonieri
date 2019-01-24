import tkinter
from tkinter import ttk, Label, Entry, Button, StringVar, LEFT, messagebox 
import random
import operator

class Priklad:
    def __init__(self, cislo_prikladu):
        self.cislo_prikladu = cislo_prikladu
        self.odpoved = None
        x = random.randint(1, 10)
        y = random.randint(1, 10)

        operace = random.choice([{"znak": "-", "funkce": operator.sub}, 
                                 {"znak": "+", "funkce": operator.add},
                                 {"znak": "*", "funkce": operator.mul}])

        if operace["znak"] == "-" and y > x:
            x, y = y, x

        self.x = x
        self.y = y
        self.zadani = f"{x} {operace['znak']} {y} = "
        self.reseni = operace["funkce"](x, y)

class MaleNezapornePocty:
    def __init__(self, root):
        self.root = root
        self.pocet_spravnych = 0

        self.label_text = StringVar()
        self.label_text.set("Zadej počet příkladů")
        self.label = Label(self.root, textvariable=self.label_text, font=("Courier", 16))
        self.label.grid(row=0, column=0)
        self.entry_text = StringVar()
        self.entry = Entry(self.root, textvariable=self.entry_text, font=("Courier", 16))
        self.entry.grid(row=0, column=1)
        self.button = Button(self.root, text="OK", font=("Courier", 16), command=self.zadej_priklady)
        self.button.grid(row=0, column=2)

    def zadej_priklady(self):
        self.pocet_prikladu = self.precti_entry()
        if self.pocet_prikladu is None:
            return
        elif self.pocet_prikladu < 1:
            messagebox.showinfo("Info", "Ale notak, alespoń jeden!")
            return

        self.button.configure(command=self.vyhodnot_priklad)

        self.priklady = [Priklad(i) for i in range(1, self.pocet_prikladu+1)]
        self.priklady_k_zadani = self.priklady[:]
        self.priklad = self.priklady_k_zadani.pop(0)
        self.label_text.set(self.priklad.zadani)

    def precti_entry(self):
        hodnota = self.entry_text.get()
        self.entry_text.set("")

        try:
            return int(hodnota)
        except Exception as e:
            messagebox.showinfo("Info", "Musíš zadat číslo!")
            return None

    def vyhodnot_priklad(self):
        self.priklad.odpoved = self.precti_entry()
        if self.priklad.odpoved is None:
            return

        self.priklad.je_spravne = self.priklad.odpoved == self.priklad.reseni
        self.pocet_spravnych += self.priklad.je_spravne

        if self.priklady_k_zadani:
            self.priklad = self.priklady_k_zadani.pop(0)
            self.label_text.set(self.priklad.zadani)
        else:
            self.vypis_shrnuti()

    def vypis_shrnuti(self):
        text = ""
        for p in self.priklady:
            text += f"Příklad číslo {p.cislo_prikladu}. ".ljust(20)
            text += f"{p.zadani}{p.reseni}".ljust(15)
            text += f"vaše odpověd: {p.odpoved}".ljust(20)
            text += f"{['Špatně', 'Správně'][p.je_spravne]}\n"
        text += f"Celkem správně: {self.pocet_spravnych} "
        text += f"z{['', 'e'][self.pocet_prikladu in range(2,5)]} {self.pocet_prikladu}"

        self.entry.destroy()
        self.button.destroy()
        self.label_text.set(text)
        self.label.configure(justify=LEFT)

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Malé Počty")
    pocitani = MaleNezapornePocty(root)
    root.mainloop()