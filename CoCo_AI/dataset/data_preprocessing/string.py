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

def split_the_list_original(input_ls : list) -> list:
    two_dimensional_paramls = []
    for input_string in input_ls:
        appendls = list(str(input_string).split())
        two_dimensional_paramls.append(appendls)
    return two_dimensional_paramls

def one_hot_encoding(input_ls : list) -> list:
    """
    원핫 인코딩을 사용하여 단어를 인코딩
    :param input_ls:
    :return:
    """
    dict_loop_index = 0
    dict_loop = {}
    set_input_ls = set(return_to_split_list(input_ls))
    for st in set_input_ls:
        dict_loop[f"{st}"] = dict_loop_index
        dict_loop_index += 1
    string_ls = split_the_list_original(input_ls)
    outls = []
    output = []
    for i in string_ls:
        for j in i:
            outls.append(dict_loop[j])
        output.append(outls)
        outls = []
    return output