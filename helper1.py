def test123():
    print ("__name__:",__name__)
    print('test123 is called from helper.py')


if __name__ == '__main__':
    # this line only runs if we run helper.py DIRECTLY
    test123()
    print('print statement from helper.py directly')
