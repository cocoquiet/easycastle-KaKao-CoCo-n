import pandas as pd

def split_the_list_original(input_ls : list) -> list:
    two_dimensional_paramls = []
    for input_string in input_ls:
        appendls = list(str(input_string).split())
        two_dimensional_paramls.append(appendls)
    return two_dimensional_paramls

def change_df_to_dict(input_df):
    number = input_df['number']
    sentence = input_df['sentence']
    ls = [[n,s] for n,s in zip(sentence, number)]
    out_dict = {}
    for i in ls:
        out_dict[f"{i[0]}"] = i[1]
    return out_dict

def return_to_split_list(input_ls : list) -> list:
    """
    문자열로 입력된 리스트를 공백기준으로 자르는 함수입니다.
    :param input_ls:
    :return:
    """
    two_dimensional_paramls = split_the_list_original(input_ls)
    outls = []
    for index_string_list in two_dimensional_paramls:
        for index_string in index_string_list:
            outls.append(str(index_string))
    return outls

def token_encoding(input_ls : list) -> list:
    """
    토큰 인코딩을 사용하여 단어를 인코딩
    :param input_ls:
    :return:
    """
    dict_loop = change_df_to_dict(pd.read_csv("/content/sentence.csv"))
    string_ls = split_the_list_original(input_ls)
    out_ls = []
    outls = []
    output = []
    for i in string_ls:
        for j in i:
            outls.append(dict_loop[j])
        output.append(outls)
        outls = []
    return output


if __name__ == '__main__':
    while True:
        print('마코천재')