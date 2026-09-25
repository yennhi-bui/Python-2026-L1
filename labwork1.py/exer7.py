def remove_dollar_sign(s):  #Tôi muốn tạo 1 hàm mới,(s) is parameter(tham số).Ví dụ remove_dollar_sign(Hello$$$)
    out = ""   #tạo 1 string rỗng
    for c in s: #lấy từng ký tự trong s và gọi ký tự đó là c(c thường được viết cho character=lý tự)-hoàn toàn có thể viết for character in c
        if c != "$":   #nếu c khác $
            out = out + c  #lấy out hiện tại + ký tự c,rồi lưu lại vào out 
    return out
print(remove_dollar_sign("Yennhi$$"))
    