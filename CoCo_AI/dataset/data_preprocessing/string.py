import pandas as pd

class String_trainsform:
    def __init__(self):
        pass
    def split_the_list_original_words(self, input_ls):
        two_dimensional_paramls = []
        for input_string in input_ls:
            appendls = list(str(input_string).split())
            two_dimensional_paramls.append(appendls)
        return two_dimensional_paramls

if __name__ == '__main__':
    stf = String_trainsform()
    print(stf.split_the_list_original_words(["1 2 3 4", "5 6 7 8"]))