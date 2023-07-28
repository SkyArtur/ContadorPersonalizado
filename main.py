class Counter:
    def __init__(self, count: int = 1, start: int = 0, step: int = 1, /) -> None:
        """O ternário permite que a declaração possa ser mais intuitiva.
        Por exemplo: Counter(1, 10) e Counter(10, 1), ambas vão entregar uma
        contagem de 1 até 9 com passo 1.
        :param count: Número de contagens a serem realizadas.
        :param start: Início da contagem.
        :param step: Passo da contagem.
        """
        self.start: int = start if count > start else count
        self.limit: int = count if count > start else start
        self.step: int = step

    def __iter__(self) -> object:
        return self

    def __item(self) -> int:
        if self.step < 0:
            item = self.limit
            self.limit += self.step
        else:
            item = self.start
            self.start += self.step
        return item

    def __next__(self) -> int | Exception:
        """Para um comportamento mais literal, entregando o número limite, basta alterar a condicional
        para 'menor ou igual'."""
        if self.start < self.limit:
            return self.__item()
        raise StopIteration


if __name__ == '__main__':
    # exemplo de utilização 1: contando de 0 a 10;
    for i in Counter(10):
        print(i)
    print('-' * 10)
    # exemplo de utilização 2: Contando de um início até um limite.
    for j in Counter(10, 1):
        print(j)
    print('-' * 10)
    # exemplo de utilização 3: Declarando início e fim de forma mais intuitiva.
    for n in Counter(1, 10):
        print(n)
    print('-' * 10)
    # exemplo de utilização 4: Declarando o step.
    for n in Counter(1, 10, 2):
        print(n)
