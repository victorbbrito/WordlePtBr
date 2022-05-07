class LetterState:
    def __init__(self, caractere: str):
        self.caractere: str = caractere
        self.tem_na_palavra: bool = False
        self.esta_na_posicao: bool = False

    def __repr__(self):
        return f"[{self.caractere} tem_na_palavra:{self.tem_na_palavra} esta_na_posicao: {self.esta_na_posicao}]"
