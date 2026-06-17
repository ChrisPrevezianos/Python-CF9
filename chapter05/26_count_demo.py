def count_with_manual_loop(my_list):
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
        print("Manual loop:", frequency_dict)
 
def count_with_get_method(my_list):
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
        print("Count with get method:", frequency_dict)
 
def count_with_dict_compr(my_list):
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print("Count with dict compr:", frequency_dict)
 
from collections import Counter
 
def count_with_counter(my_list):
    frequency_dict = Counter(my_list)
    print("Using  counter:", frequency_dict)
 
    sorted_freq_dict = frequency_dict.most_common()
    print(sorted_freq_dict)
 
 
def main():
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]
    count_with_counter(my_list)
 
 
if __name__ == "__main__":
    main()
