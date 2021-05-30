import pandas as pd

class String_trainsform:
    def __init__(self):
        self.sef = String_trainsform

    def split_the_list_original_words(self, input_ls):
        two_dimensional_paramls = []
        for input_string in input_ls:
            appendls = list(str(input_string).split())
            two_dimensional_paramls.append(appendls)
        return two_dimensional_paramls

    def return_to_split_list(self, input_ls : list) -> list:
        """
        문자열로 입력된 리스트를 공백기준으로 자르는 함수입니다.
        :param input_ls:
        :return:
        """
        two_dimensional_paramls = self.sef.split_the_list_original_words(input_ls)
        outls = []
        for index_string_list in two_dimensional_paramls:
            for index_string in index_string_list:
                outls.append(str(index_string))
        return outls

    def store_the_sentence_list_for_token_encoding(self, input_ls : list , path = "sentence.csv"):
        pass

if __name__ == '__main__':
    stf = String_trainsform()
    print(stf.split_the_list_original_words(["1 2 3 4", "5 6 7 8"]))
    print(stf.return_to_split_list(["1 2 3 4 5 6", "7 8 9 10"]))