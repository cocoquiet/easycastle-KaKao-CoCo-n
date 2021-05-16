def return_to_split_list(input_ls : list) -> list:
    """
    문자열로 입력된 리스트를 공백기준으로 자르는 함수입니다.
    :param input_ls:
    :return:
    """
    two_dimensional_paramls = []
    outls = []
    for input_string in input_ls:
        appendls = list(str(input_string).split())
        two_dimensional_paramls.append(appendls)
    for index_string_list in two_dimensional_paramls:
        for index_string in index_string_list:
            outls.append(str(index_string))
    return outls



if __name__ == '__main__':
    print(return_to_split_list((['좌배 까는건 ㅇㅂ', '좌배 아져씨 바보'])))