
class monta_protocolo:
    # Classe que monta o protocolo
    def __init__(self):
        self.buffer = None
        self.cabecalho = None
        self.comando = None
        self.tamanho = None
        self.protocolo = None

    def Protocolo(self, buffer):
        self.comando = '0'
        self.buffer = list(buffer)
        print(self.buffer)

        protocolo = ['L', 'U', 'P', 'A','#','#', self.comando, ] + self.buffer

        tam = str(len(protocolo))

        protocolo.remove('#')
        protocolo.insert(4,tam[:1])
        protocolo.remove('#')
        protocolo.insert(5,tam[1:])
        print(type(protocolo))
        self.protocolo = "".join(protocolo)
        return self.protocolo


#
# # Construindo protocolo
# elemento = self.cabecalho + self.comando + item_e_CRC[0]
#
# tam = len(elemento)
#
# self.tamanho = str(tam)
#
# proto = self.cabecalho + self.tamanho + self.comando + item_e_CRC[0] + item_e_CRC[1]
#
# self.protocolo.append(proto)
#
# print(self.protocolo[index])
