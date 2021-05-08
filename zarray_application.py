class Zarr_a:
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    def search(self):
        concat = self.pattern + "$" + self.string
        l = len(concat)

        z = [0] * l
        self.getZarr(concat, z)

        for i in range(l):
            if z[i] == len(self.pattern):
                return i - len(self.pattern) - 1
        return -1

    @staticmethod
    def getZarr(string, z):
        n = len(string)

        l, r, k = 0, 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i

                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l

                if z[k] < r - i + 1:
                    z[i] = z[k]

                else:
                    l = i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
