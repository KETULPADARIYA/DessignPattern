import time
import timeit


class FormattedText:

    def __init__(self,plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def  capitalize(self,start,end):
        for capital_letter_index in range(start,end):
            self.caps[capital_letter_index] = True


    def __str__(self):
        return "".join( text.upper() if is_capital else text for text,is_capital in zip(self.plain_text,self.caps) )


class BetterFormattedText:
    def __init__(self,plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:

        def __init__(self,start,end,capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self,position):
            return self.start <= position <= self.end

    def get_range(self,start,end):
        text_capital_range = self.TextRange(start,end)
        self.formatting.append(text_capital_range)
        return text_capital_range

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c= c.upper()
            result.append(c)
        return "".join(result)



def time_it(func_st):
    st_time= time.time()
    exec(func_st)
    time_diff = time.time() -st_time
    # time_diff = timeit.repeat(stmt=func_st,number=100,repeat=2,globals=vars())

    print(f"time is a {time_diff*1000} ms")


text = "This is a brave new world"
ft = FormattedText(text)

word_to_find = "brave"
brave_index = text.find(word_to_find)
print(ft)

time_it("ft.capitalize(brave_index,brave_index+len(word_to_find))")

bft = BetterFormattedText(text)
# bft.get_range(16,19).capitalize = True
time_it("bft.get_range(16,19).capitalize = True")
print(bft)