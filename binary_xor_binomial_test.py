from scipy.stats import binomtest

def hex_to_binary(hex_str):
    # 将十六进制字符串转换为二进制字符串，并去掉前缀'0b'
    binary_str = bin(int(hex_str, 16))[2:]
    return binary_str

def xor_binary(bin_str1, bin_str2):
    result = ""
    # 遍历每一位进行异或操作
    for b1, b2 in zip(bin_str1, bin_str2):
        if b1 != b2:
            result += '1'
        else:
            result += '0'
    return result

def binomial_test(binary_str):
    ones_count = binary_str.count('1')
    result = binomtest(ones_count, len(binary_str), p=0.5)
    return result

def main(file_name):
    with open(file_name, 'r') as file:
        hex_str1 = file.readline().strip()  
        hex_strs = [file.readline().strip() for _ in range(100)]  # 第二行到第101行

    # 将第一行的十六进制字符串转换为二进制串，并重复100次
    binary_str1 = hex_to_binary(hex_str1)
    binary_str1_repeated = binary_str1 * 100

    # 将第二行到第101行的十六进制字符串转换为二进制串，并拼接在一起
    binary_str2_to_101 = ''
    for hex_str in hex_strs:
        binary_str2_to_101 += hex_to_binary(hex_str)

    # 对两个长二进制串进行异或操作
    xor_result = xor_binary(binary_str1_repeated, binary_str2_to_101)

    # 进行二项分布检验
    binomial_test_result = binomial_test(xor_result)

    #print("01 string：", xor_result)
    print(binomial_test_result)
    # print info: BinomTestResult(k=12648, n=25300, alternative='two-sided', statistic=0.4999209486166008, pvalue=0.9849521699499312)

if __name__ == "__main__":
    file_name = '10000_hash.txt'
    main(file_name)
