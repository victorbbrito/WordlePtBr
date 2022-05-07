from letter_state import LetterState

class Wordle:

    MAX_TENTATIVAS = 7
    TAMANHO_PALAVRA = 5

    def __init__(self, palavra: str):
        self.palavra: str = palavra.upper()
        self.tentativas = []
        pass
    
    def tentativa(self, palavra: str):
        palavra = palavra.upper()
        self.tentativas.append(palavra)

    def adivinhar(self, palavra: str):
        palavra = palavra.upper()
        resultado = []

        for i in range(self.TAMANHO_PALAVRA):
            caractere = palavra[i]
            letter = LetterState(caractere)
            letter.tem_na_palavra = caractere in self.palavra
            letter.esta_na_posicao = caractere == self.palavra[i]
            resultado.append(letter)

        return resultado

    @property
    def resolvido(self):
        return len(self.tentativas) > 0 and self.tentativas[-1] == self.palavra

    @property
    def tentativas_restantes(self) -> int:
        return self.MAX_TENTATIVAS - len(self.tentativas)

    @property
    def posso_tentar(self):
        return self.tentativas_restantes > 0 and not self.resolvido
