

def my_func(*args):
    return min(args, key=max)

if __name__ == '__main__':
    sol = my_func('1, 2, 3, 4 , 5', 'almafa', "Kati", "megszentségteleníthetetlenséges")
    print(sol)
