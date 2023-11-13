def gabung_list(list1, list2):
    gabung =list1+list2
    list_gabung= list(set(gabung))
    return list_gabung
print(gabung_list([1, 2, 3], [2, 3, 4]))
print(gabung_list(["a", "b", "c"], ["d", "e", "f"])) 