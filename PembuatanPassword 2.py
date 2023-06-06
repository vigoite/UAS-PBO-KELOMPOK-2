import random
import string
import PySimpleGUI as sg

class PasswordGenerator:
    def __init__(self): 
        self.window = sg.Window("Pembuatan Password", self.tampilan(), size=(500, 250), background_color=("black"))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == "Keluar" or event == sg.WINDOW_CLOSED:
                break 
            elif event == "Buat Password":
                panjang_input = values["PANJANG"]
                kombinasi = {
                    "kapital": values["kapital"], 
                    "kecil": values["kecil"], 
                    "angka": values["angka"], 
                    "simbol": values["simbol"] 
                }

                if not panjang_input: 
                    sg.popup_ok("Harap masukkan panjang password!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) 
                    continue 
                try: 
                    panjang = int(panjang_input) 
                except ValueError:
                    sg.popup_ok("Karakter yang dimasukkan tidak valid!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue"))
                    continue 
                password = self.generate_password(panjang, kombinasi)
                if password: 
                    self.window["PASSWORD"].update(password)

        self.window.close()

    def tampilan(self):
        return [
            [sg.Text("Panjang Password :", text_color=("white"), background_color=("black")), sg.Input(key="PANJANG",pad=((10, 10), (10, 10)))],
            [sg.Checkbox("Huruf Kapital", key="kapital", text_color=("white"), background_color=("black")), sg.Checkbox("Huruf Kecil", key="kecil", text_color=("white"), background_color=("black"), pad=((15, 10), (10, 10)))], 
            [sg.Checkbox("Angka", key="angka", text_color=("white"), background_color=("black")), sg.Checkbox("Simbol", key="simbol", text_color=("white"), background_color=("black"), pad=((52, 10), (10, 10))),sg.Button("Buat Password", button_color=("white", "darkblue"), pad=((160, 10), (0, 10)))],
            [sg.Text("Password :", text_color=("white"), background_color=("black")), sg.Input(key="PASSWORD", disabled=True, pad=((60, 10), (10, 10)))], 
            [sg.Button("Keluar", button_color=("white", "red"), pad=((413, 10), (10, 10)))], 
        ]

    def generate_password(self, panjang, kombinasi):
        if panjang < 10:
            sg.popup_ok("Panjang password minimal 10 karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue"))
            return
        
        if panjang > 25:
            sg.popup_ok("Panjang password maksimal 25 karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue")) 
            return

        kombinasi_terpilih = []
        if kombinasi["kapital"]:
            kombinasi_terpilih.append(string.ascii_uppercase)
        if kombinasi["kecil"]: 
            kombinasi_terpilih.append(string.ascii_lowercase) 
        if kombinasi["angka"]:
            kombinasi_terpilih.append(string.digits)
        if kombinasi["simbol"]:
            kombinasi_terpilih.append(string.punctuation)

        if not kombinasi_terpilih:
            sg.popup_ok("Harap pilih minimal satu kombinasi karakter!", button_color=("white", "green"), text_color=("black"), background_color=("lightblue"))
            return 

        password = [] 
        for _ in range(panjang):
            char_pool = random.choice(kombinasi_terpilih)
            password.append(random.choice(char_pool))

        random.shuffle(password)
        password = ''.join(password)
        return password

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()
