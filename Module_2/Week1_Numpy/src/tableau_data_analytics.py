import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv(
        r'D:\Github\AIO-exercise\Module_2\Week1_Numpy\data\advertising.csv')
    data = df.to_numpy()

    # Question 15
    sale_column = data[:, 3]
    max_sale = sale_column.max()
    max_sale_index = np.where(sale_column == max_sale)
    print(max_sale_index)

    # Question 16
    TV_column = data[:, 0]
    print(TV_column.mean())

    # Question 17
    print(len(np.where(sale_column >= 20)[0]))

    # Question 18
    ratio_column = data[:, 1]
    indexs_ratio = np.where(sale_column >= 15)[0]

    print(np.sum(ratio_column[indexs_ratio])/len(indexs_ratio))

    # Question 19
    newspaper_column = data[:, 2]
    avagrage_newspaper = newspaper_column.mean()
    indexs_newspaper = np.where((newspaper_column > avagrage_newspaper))[0]
    print(np.sum(sale_column[indexs_newspaper]))

    # Question 20
    avarage_sale = sale_column.mean()
    scores = np.where(sale_column > avarage_sale, 'Good', 'Bad')
    scores = np.where(sale_column == avarage_sale, "Average", scores)
    print(scores[7:10])

    # Question 21
    near_avarage_sale_distance = np.min(np.abs(sale_column - avarage_sale))
    near_avarage_sale_index = np.where(
        np.abs(sale_column - avarage_sale) == near_avarage_sale_distance)
    near_avarage_sale = sale_column[near_avarage_sale_index]
    scores = np.where(sale_column > near_avarage_sale, 'Good', 'Bad')
    scores = np.where(sale_column == near_avarage_sale, "Average", scores)
    print(scores[7:10])
