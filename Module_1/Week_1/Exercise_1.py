import math

def F1_score_cal(tp,fp,fn):
  if(type(tp)!= int):
    print('tp must be int')
  elif(type(fp)!= int):
    print('fp must be int')
  elif(type(fn)!= int):
    print('fn must be int')
  else:
    if(tp<=0 or fp<=0 or fn <=0):
      print('tp and fp and fn must be greater than zero')
    else:
      Precision = tp/(tp+fp)
      Recall = tp/(tp+fn)
      F1_Score = 2*(Precision*Recall)/(Precision + Recall)
      print(f"F1-score = {F1_Score}")
if __name__ == '__main__':
  F1_score_cal(10,2,3)
  F1_score_cal('a',2,9)

