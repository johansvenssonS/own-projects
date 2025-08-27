"""Modul för sorteringsalgoritmer"""
from src.unorderedlist import UnorderedList
#from unorderedlist import UnorderedList


def insertion_sort(unordered_list):
    """ Insertion sort """
    end_index = unordered_list.size()
    for i in range(1, end_index):
        data = unordered_list.get(i)
        j = i - 1
        while j >= 0 and unordered_list.get(j) > data:
            unordered_list.set(j+1, unordered_list.get(j))#index j+1, get(j) = data
            j -= 1
        unordered_list.set(j+1, data)
    return unordered_list

def recursive_insertion(unordered_list, size):
    """Recursive insertion sort"""
    if size <= 1:#base case
        return
    recursive_insertion(unordered_list, size-1)
    current = unordered_list.get(size-1)
    j = size -2
    while j >= 0 and unordered_list.get(j)[1] < current[1]:
        unordered_list.set(j+1, unordered_list.get(j))
        j -= 1
    unordered_list.set(j+1, current)
# if __name__ == "__main__":
#     ul = UnorderedList()
#     ul.append('108', 108)
#     ul.append('48', 48)
#     ul.append('hejsan', 272)
#     recursive_insertion(ul, ul.size())
#     ul.print_list()
