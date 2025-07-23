class Strint(int):

    def __lt__(self, other):
        return self % 10 < other % 10

    def __gt__(self, other):
        return self % 10 > other % 10

    def __le__(self, other):
        return self % 10 <= other % 10

    def __ge__(self, other):
        return self % 10 >= other % 10

    def __eq__(self, other):
        return self % 10 == other % 10

    def __ne__(self, other):
        return self % 10 != other % 10

    def __add__(self, other):
        new = str(self) + str(other)
        return Strint(new)

    def __sub__(self, other):
        if str(other) != str(self)[-len(str(other)):]:
            raise ValueError("'The subtraction is not valid!'")
        if str(other) == str(self):
            return Strint(0)
        else:
            return Strint(str(self)[:-len(str(other))])



    def __len__(self):
        return len(str(self))

    def __call__(self):
        pe_en_dict = {'0':'۰',
                      '1':'۱',
                      '2':'۲',
                      '3':'۳',
                      '4':'۴',
                      '5':'۵',
                      '6':'۶',
                      '7':'۷',
                      '8':'۸',
                      '9':'۹'
                      }
        pe = ""
        for ch in str(self):
            pe += pe_en_dict[ch]
        return pe


