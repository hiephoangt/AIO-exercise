def md_nre_single_sample(y,y_hat,n,p):
  return (y**(1/n) - y_hat**(1/n))**p

if __name__ == '__main__':
  print(md_nre_single_sample(100,99.5,2,1))