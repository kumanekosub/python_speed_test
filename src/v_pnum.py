import time

# シンプルO(x)
def pnum1(x):
  if x <= 1:
    return False

  for i in range(2,x-1):
    if x % i == 0:
      return False
  return True

## テストデータ実行用
def main():
  f = open('test_data.txt','r',encoding='UTF-8')
  datal = f.readlines()
  output = [0] * len(datal)

  i = 0
  ## pnum 判定
  for data in datal:
    
    ## 素数判定関数
    result = pnum1(int(data))

    output[i] = int(result)
    i += 1

  return sum(output)


if __name__ == '__main__':

  start = time.time()
  output = main()
  end = time.time()
  print('finish \n','result: ',output,'\ntime: ',end - start)
