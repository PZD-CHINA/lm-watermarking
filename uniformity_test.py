import matplotlib.pyplot as plt
import numpy as np

def uniformity_test(file_name):
    # 从输出文件中读取数据，并过滤掉非有限值
    hash_values = []
    with open(file_name, 'r') as file:
        for line in file:
            # 将十六进制字符串转换为整数，并将其添加到列表中
            hash_values.append(int(line.strip(), 16))

    # 计算范围内的最小值和最大值
    min_value = min(hash_values)
    max_value = max(hash_values)
    print("min_value:",min_value)
    print("max_value:",max_value)
    
    # 确定频率的区间数
    num_bins = 100
    bin_size = (max_value - min_value) / num_bins

    # 初始化频率数组以统计每个区间内的出现次数
    frequency = np.zeros(num_bins, dtype=int)

    # 计算每个区间内的哈希值出现次数
    for value in hash_values:
        bin_index = int((value - min_value) // bin_size)
        if bin_index == num_bins:
            bin_index -= 1
        frequency[bin_index] += 1

    # 计算卡方值
    # 分子
    numerator = np.sum((frequency * (frequency + 1)) / 2)

    # 分母
    denominator = (len(hash_values) / (2 * num_bins)) * (len(hash_values) + 2 * num_bins - 1)

    # 计算卡方值
    chi_squared = numerator / denominator

    print("frequency:", frequency)
    print("chi_squared score:", chi_squared)

    # 判断
    if 0.95 <= chi_squared <= 1.05:
        print("The hash function is uniformity")
    else:
        print("The hash function is uniformity")

    # 绘制直方图
    bin_edges = np.linspace(min_value, max_value, num_bins+1)
    plt.bar(bin_edges[:-1], frequency, width=bin_size, color='skyblue', edgecolor='black')
    plt.xlabel('value range')
    plt.ylabel('frequency')
    plt.title('uniformity test')
    plt.grid(True)

    # 保存图片
    plt.savefig('uniformity_test.png')

    plt.show()

if __name__ == "__main__":
    uniformity_test('100000_hash.txt')
