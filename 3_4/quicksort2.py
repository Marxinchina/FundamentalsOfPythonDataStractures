import random


def quicksort(array):
    if len(array) < 2:
        return array  # base case: array that is empty or contains
        # only one element is ordered
    else:
        pivot = array[0]  # recursive case and pivot, partitioning
        less = [i for i in array[1:] if i <= pivot]
        print('less:{}'.format(less))
        greater = [i for i in array[1:] if i > pivot]
        print('greater:{}'.format(greater))
        return quicksort(less) + [pivot] + quicksort(greater)


def main(size=20):
    l = [random.randint(1, size + 1) for _ in range(size)]
    # l = []
    # for count in range(size):
    #     l.append(random.randint(1, size + 1))
    print(l)
    l = quicksort(l)
    print(l)


if __name__ == '__main__':
    main()

