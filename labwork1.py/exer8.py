def extract_even(l):
    result = [] #list rỗng để chứa các số chắn tìm được
    for x in l:
        if x % 2 == 0:
            result.append(x) #nếu chẵn thêm vào result
    return result            #trả về list mới
print(extract_even([1,2,5,-1,4,10]))

