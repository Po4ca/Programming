import tkinter as tk
from pet import Pet

"""
    TODO: заблокировать кнопки, когда питомец что-то делает
          изменять портрет во время активности
          mood влияет на портрет
          mood = sum() // 3
"""
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.pet = Pet(
            name="Бамбр",
            portrait="assets/calm.png"
        )

        # лейблы с атрибутами питомца
        self.name_lbl = tk.Label(self, text=self.pet.name)
        self.name_lbl.pack()
        self.fullness_lbl = tk.Label(self)
        self.fullness_lbl.pack()
        self.activity_lbl = tk.Label(self)
        self.activity_lbl.pack()
        self.cheerfulness_lbl = tk.Label(self)
        self.cheerfulness_lbl.pack()
        self.mood_lbl = tk.Label(self)
        self.mood_lbl.pack()

        # рисуем портрет питомца в окне
        self.canvas = tk.Canvas(self, width=250, height=256)
        self.canvas.pack()
        self.image = tk.PhotoImage(file=self.pet.portrait)
        self.image = self.image.subsample(2)  # 256
        self.canvas.create_image(128, 128, image=self.image)

        # кнопки (#FIXME: кнопки срабатывают не мгновенно)
        self.feed_btn = tk.Button(
            self,
            text="накормить",
            command=lambda: self.pet.feed(5)
        )
        self.feed_btn.pack()
        self.play_btn = tk.Button(
            self,
            text="поиграть",
            command=lambda: self.pet.play(5)
        )
        self.play_btn.pack()
        self.sleep_btn = tk.Button(
            self,
            text="уложить спать",
            command=lambda: self.pet.sleep(5)
        )
        self.sleep_btn.pack()

    def renew(self):
        self.pet.decrease_stats()
        self.fullness_lbl.config(text=f"сытость: {self.pet.fullness}")
        self.activity_lbl.config(text=f"активность: {self.pet.activity}")
        self.cheerfulness_lbl.config(text=f"бодрость: {self.pet.cheerfulness}")
        self.mood_lbl.config(text=f"настроение: {self.pet.mood}")
        self.after(1000, self.renew)


window = App()
window.renew()
window.mainloop()
