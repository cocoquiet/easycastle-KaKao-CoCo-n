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

if __name__ == '__main__':
    print(return_to_split_list(["123 456", "789 10"]))