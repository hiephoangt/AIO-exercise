import math


def f1_score_cal(tp, fp, fn):
    if (type(tp) != int):
        print('tp must be int')
    elif (type(fp) != int):
        print('fp must be int')
    elif (type(fn) != int):
        print('fn must be int')
    else:
        if (tp <= 0 or fp <= 0 or fn <= 0):
            print('tp and fp and fn must be greater than zero')
        else:
            precision = tp/(tp+fp)
            recall = tp/(tp+fn)
            f1_score = 2*(precision*recall)/(precision + recall)
            print(f"F1-score = {f1_score}")


if __name__ == '__main__':
    f1_score_cal(10, 2, 3)
    f1_score_cal('a', 2, 9)
