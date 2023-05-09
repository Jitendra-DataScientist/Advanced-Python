import multiprocessing
import time
import datetime

def yourfunction(x):
    print ('yourfunction getting excuted at ',datetime.datetime.now())
    time.sleep(1)
    return True

if __name__ == '__main__':
    with multiprocessing.Pool(processes=3) as pool:
        data = pool.map(yourfunction, [1, 2, 3, 4, 5, 6, 7])
