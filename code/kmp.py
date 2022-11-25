
class KMP:
    def __init__(self, pat):
        self.pat = pat
        M = len(pat)
        R = 256 # radix
        self.dfa = [[0 for c in range(0, M)] for r in range(0, R)]
        self.dfa[ord(pat[0])][0] = 1
        X = 0
        for j in range(1, M):
            for c in range(0, R):
                self.dfa[c][j] = self.dfa[c][X]  # Copy mismatch cases
            self.dfa[ord(pat[j])][j] = j + 1  # Set match case
            X = self.dfa[ord(pat[j])][X]  # Update restart state
        self.j = 0
        self.i = 0
        self.M = M

    def step(self, c): 
        self.j = self.dfa[ord(c)][self.j]
        if self.j == self.M:
            self.j = 0
            return True 
        else:
            return False

# SIMULTANEOUS string search!!
line = input()
out = []
smiles = list(map(KMP, [';)',':)',';-)',':-)']))
for i in range(len(line)):
    for smile in smiles:
        if smile.step(line[i]):
            out.append(str(i - smile.M + 1))

