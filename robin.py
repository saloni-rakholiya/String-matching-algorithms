# class Robin:
#     def __init__(self, text, pattern):
#         self.text = text
#         self.pattern = pattern
#         self.q = 7919
#         self.d = 256
#     def search(self):
#         M = len(self.pattern)
#         N = len(self.text)
#         i = 0
#         j = 0
#         p = 0
#         t = 0
#         h = 1

#         for i in range(M-1):
#             h = (h*self.d)%self.q

#         for i in range(M):
#             p = (self.d*p + ord(self.pattern[i]))%self.q
#             t = (self.d*t + ord(self.text[i]))%self.q

#         for i in range(N-M+1):
#             if p==t:
#                 for j in range(M):
#                     if self.text[i+j] != self.pattern[j]:
#                         break
#                     else: j+=1
#                     if j==M:
#                         return i

#             if i < N-M:
#                 t = (self.d*(t-ord(self.text[i])*h) + ord(self.text[i+M]))%self.q
#                 if t < 0:
#                     t = t+self.q
#         return -1

class Robin:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.q = 7919
        self.d = 256
    def search(self):
        M = len(self.pattern)
        N = len(self.text)
        i = 0
        j = 0
        p = 0
        t = 0
        h = 1
        flag=0
        ans="Pattern found at "
        for i in range(M-1):
            h = (h*self.d)%self.q

        for i in range(M):
            p = (self.d*p + ord(self.pattern[i]))%self.q
            t = (self.d*t + ord(self.text[i]))%self.q

        for i in range(N-M+1):
            if p==t:
                for j in range(M):
                    if self.text[i+j] != self.pattern[j]:
                        break
                    else: j+=1
                    if j==M:
                        flag=1
                        ans+=str(i)+", "

            if i < N-M:
                t = (self.d*(t-ord(self.text[i])*h) + ord(self.text[i+M]))%self.q
                if t < 0:
                    t = t+self.q
        if flag == 1:
            return ans            
        return "Pattern not found"