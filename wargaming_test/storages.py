from pymemcache.client import base


class FibonacciSlice:
    key = 'fibonacci'
    default_len = 10

    def __init__(self, storage: base.Client):
        self.storage = storage
        self._refresh_collection(self.default_len)

    def get(self, start: int, end: int) -> list[int]:
        """
        Вернуть срез чисел.

        Если срез больше, чем чисел сохранено в хранилище,
        то сначала вычисляется и сохраняется новая коллекция.
        """
        collection = self._get_collection()
        if end > len(collection):
            collection = self._refresh_collection(end)
        return collection[start:end]

    def _get_collection(self) -> list[int]:
        """Вернуть всю сохранённую коллекцию чисел"""
        raw_data = self.storage.get(self.key)
        return list(map(int, raw_data.decode().split(',')))

    def _refresh_collection(self, n: int) -> list[int]:
        """Генерирует коллекцию чисел длинной n и сохраняет в хранилище"""
        collection = list(self._generate(n))
        self.storage.set(self.key, ','.join([str(num) for num in collection]))
        return collection

    @staticmethod
    def _generate(n):
        a, b = 1, 1
        for i in range(n):
            yield a
            a, b = b, a + b


fibonacci_slice = FibonacciSlice(
    storage=base.Client(('memcached', 11211)),
)
