import tkinter as tk
# Membuat jendela utama
window = tk.Tk()
window.title("Contoh Tkinter")
# Menambahkan label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()
# Fungsi untuk mengubah teks label
def on_button_click():
    label.config(text="Tombol telah diklik!")
# Menambahkan tombol
button = tk.Button(window, text="Klik Saya", command=on_button_click)
button.pack()
# Menampilkan jendela
window.mainloop()