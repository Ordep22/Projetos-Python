import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports
from serial import *

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title('MPA 2023')

        ##Velocidades de conexão
        #Esses valores numca podem ser alterados
        self.velocidades  = ("300","600","1200","2400","4800","9600","19200","1200","38400","115200")

        #Caixa de seleção
        #self.combobox = ttk.Combobox(self,values = self.porta_serial())

        #Variável de opção
        self.variavel_opcao = tk.StringVar(self)

        #Instanciando uma janela
        self.criando_janela()

    def criando_janela(self):

        ##posicionamento
        paddings = {'padx': 5,'pady':5}

        #Texto menu de seleção portas COM
        combobox_label  = ttk.Label(self, text= "COM:")
        combobox_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # Menu de seleção portas COM
        combobox = ttk.Combobox(self,values = self.porta_serial())
        combobox.grid(column=0, row=1, sticky=tk.W, **paddings)



        #Texto e seleção de velocidadw de concção
        label  = ttk.Label(self, text= "Valocidade:")
        label.grid(column=3, row=0, sticky=tk.W, **paddings)

        #Menu de seleção de coneção
        menu_opcao = ttk.OptionMenu(
            self,
            self.variavel_opcao,
            self.velocidades[0],
            *self.velocidades,
            command = self.opcao_mudada) #Essa variável será utilizada para ser passada para conexaão
        menu_opcao.grid(column=3, row=1, sticky=tk.W, **paddings)

    def porta_serial(self):

        return serial.tools.list_ports.comports()


    def opcao_mudada(self,*args):

        self. self.output_label['text'] = f'You selected: {self.option_var.get()}'



if __name__ == "__main__":
    app = Application()
    app.mainloop()


