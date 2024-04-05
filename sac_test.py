import numpy as np
from scipy.stats import binomtest
import matplotlib.pyplot as plt

def hex_to_binary(hex_str):
    # 将十六进制字符串转换为二进制字符串，并去掉前缀'0b'
    binary_str = bin(int(hex_str, 16))[2:]
    return binary_str.zfill(255)  # 补零使长度为255位

def hamming_distance(bin_str1, bin_str2):
    # 计算两个二进制串的汉明距离
    distance = sum(c1 != c2 for c1, c2 in zip(bin_str1, bin_str2))
    return distance

def main(file_name):
    # 从文件中读取哈希数
    with open(file_name, 'r') as file:
        hash_list = [line.strip() for line in file.readlines()[:10000]]

    # 将哈希数转换为二进制串
    binary_hashes = [hex_to_binary(hash_str) for hash_str in hash_list]

    # 计算每对连续哈希数的汉明距离
    hamming_distances = [hamming_distance(binary_hashes[i], binary_hashes[i+1]) for i in range(len(binary_hashes)-1)]

    binary_num=0
    for i in range(len(binary_hashes)-1):
        binary_num += len(binary_hashes[i])
    # 进行二项分布检验
    p_value = binomtest(sum(hamming_distances), binary_num, p=0.5)

    print("汉明距离列表：", hamming_distances)
    print("二项分布检验的p值：", p_value)

    # 绘制汉明距离的图
    plt.plot(range(len(hamming_distances)), hamming_distances, marker='o', markersize=1.5, linestyle='')
    plt.title('Hamming Distances')
    plt.xlabel('Hamming Distance')
    plt.ylabel('Index')
        
    # 保存图片
    plt.savefig('sac_test.png')

    plt.show()

if __name__ == "__main__":
    file_name = '10000_hash.txt'
    main(file_name)
