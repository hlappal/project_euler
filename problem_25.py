class Number:

    def __init__(self, n):
        self.chunks = []
        self.limit = int(1e3)
        self.cache_id = None
        self.chunkify(n)

    def chunkify(self, n):
        # Chunkify a given number
        self.chunks.append(int(n % self.limit))
        while n > self.limit:
            n = int(n / self.limit)
            self.chunks.append(int(n % self.limit))
        return self.chunks

    def add(self, n):
        # Perform addition Number + n
        if len(self.chunks) > len(n.chunks):
            larger = self.chunks
            smaller = n.chunks
        else:
            larger = n.chunks
            smaller = self.chunks

        r = 0
        new = []
        l = len(smaller)
        for i in range(l):
            new.append(int((larger[i] + smaller[i] + r) % self.limit))
            r = int((larger[i] + smaller[i] + r) / self.limit)
        for i in range(l, len(larger)):
            new.append(int((larger[i] + r) % self.limit))
            r = int((larger[i] + r) / self.limit)

        self.chunks = new

    def subtract(self, n):
        # Perfor subtraction Number - n
        # Here, n is either 1 or 2
        print(f"n in the beginning of subtract: {n}")
        print(f"chunks in the beginning of subtract: {self.chunks}")
        if self.chunks[0] - n < 0 and len(self.chunks) > 2:
            self.chunks[1] -= 1
            self.chunks[0] += (self.limit - n)
        else:
            self.chunks[0] -= n


class Fibonacci:

    def __init__(self):
        n0 = Number(0)
        n0.cache_id = 0
        n1 = Number(1)
        n1.cache_id = 1
        self.cache = [n0, n1]

    def __call__(self, n):
        print(f"n has chunks: {n.chunks} and cache_id: {n.cache_id}")
        for chunk in n.chunks:
            if not (isinstance(chunk, int) and chunk >= 0):
                raise ValueError(f"Positive integer number expected, got {chunk}")

        # Check computed Fibonacci numbers
        if n.cache_id:
            return self.cache[n.cache_id]
        else:
            # Compute and cache the requested Fibonacci number
            n1 = n
            n2 = n
            print(f"n1 chunks before subtract: {n1.chunks}")
            n1.subtract(1)
            print(f"n2 chunks after subtract: {n1.chunks}")
            n2.subtract(2)
            n1.add(n2)
            print(f"n1 after addition: {n1.chunks}")
            fib = self(n1)
            n.cache_id = len(self.cache)
            self.cache.append(fib)

        return fib


def main():
    i = Number(1)
    fib = Fibonacci()
    while True:
        n = fib(i)
        print(f"n after fib(i): {n.chunks}, {n.cache_id}")
        #if n % 100 == 0:
        #    print(f"The {i}'th Fibonacci number is {n}")
        if len(n.chunks) > 2:
            break
        i += 1
    print(f"The first to have {1000} digits is the {i}'th Fibonacci number {n}")


main()
