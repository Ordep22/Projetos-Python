class monta_protocolo:
    # Classe que monta o protocolo
    def __init__(self):
        self.string_protocolo = None
        self.buffer = None
        self.cabecalho = None
        self.comando = None
        self.tamanho = None
        self.protocolo = None

    def Protocolo(self, buffer):
        self.comando = 0X04

        self.buffer = list(buffer)
        # print(self.buffer)

        # Recebe o buffer em formato de lista e adiona as informações do protocolo LUPA+ESPAÇODOTAMANHO+COMANDO+PACOTE
        buffer_protocolo = ['L', 'U', 'P', 'A', '#', '#', str(self.comando), ] + self.buffer

        buffer_protocolo_saida = []

        # Calcula a quantidade de caracteres(1 caracter =  Byte) do pacote
        tamanho = len(buffer_protocolo)

        # Divide o tamanho em dois Bytes, mais significativo e menos significativo
        tamnho_primeirosbytes = (tamanho & 0xFF00) >> 8
        tamnho_ultimosirosbytes = (tamanho & 0x00FF)

        # Remove os carcteres # e adiciona o Bytes do tamanho
        buffer_protocolo.remove('#')
        buffer_protocolo.insert(4, str(tamnho_ultimosirosbytes))
        buffer_protocolo.remove('#')
        buffer_protocolo.insert(5, str(tamnho_primeirosbytes))

        # Transforma a lista protocolo em uma string
        self.string_protocolo = "".join(buffer_protocolo)

        # Percorre a string codificando os elementos em Bytes
        for i in range(0, len(buffer_protocolo), 1):

            # Codifica os elemento do tamanho do pacote em hexadecimal
            if i == 4 or i == 5:

                elemento_hexa = int(buffer_protocolo[i])
                buffer_protocolo_saida.append(elemento_hexa)

            elif i == 6:
                buffer_protocolo_saida.append(int(buffer_protocolo[i]))

            else:

                # Encontra o correpondente decimal do caracter informado
                elemento_hexa = ord(buffer_protocolo[i])

                # Adiciona ao vetor o codigo hexa do caracter
                buffer_protocolo_saida.append(elemento_hexa)

        return buffer_protocolo, buffer_protocolo_saida
