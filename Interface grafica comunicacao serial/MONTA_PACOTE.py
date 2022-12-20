class monta_pacote:

    def __init__(self):
        self.buffer_crc16 = None
        self.buffer_pacote = None
        self.saida = None

    def dados(self, buffer_pacote, buffer_crc16):
        self.buffer_pacote = buffer_pacote
        self.buffer_crc16 = buffer_crc16
        buffer_pacote_bytes = []

        # Adciona o CRC ao array com as informações do pacote
        for i in range(0, len(buffer_crc16), 1):
            self.buffer_pacote.append(self.buffer_crc16[i])

        for j in range(0, len(buffer_pacote), 1):

            buffer_pacote_bytes.append(buffer_pacote[j].to_bytes(1, 'little'))

        return buffer_pacote_bytes
