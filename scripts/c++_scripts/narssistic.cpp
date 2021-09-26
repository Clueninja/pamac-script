bool is_narcissistic(number){
    int sumof = 0
    int num_str = string(number)
    int len_num = length(num_str)
    for index in range(len_num):
        sumof+=int(num_str[index])**len_num
    if sumof == number:
        return True
    else:
        return False

}