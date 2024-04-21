def solution(clothes):
    var_dict = {}
    for product, class_ in clothes:
        #count = var_dict.get(class_,0) 
        # dict.get(a,b) : dictionary에 a라는 key값이 없으면 count 값이 0이 된다.
        if not class_ in var_dict:
            # print('a')
            var_dict[class_] = [product]
        else:
            var_dict[class_].append(product)
    a = 1
    for i in var_dict.values():
        a = a * (len(i)+1)
    return a - 1