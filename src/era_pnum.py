import time

# エラトステネスのふるい
def eratosthenes(x):
  
  elist = [1.0] * (x+1)  
  elist[1] = 0.0
  elist[0] = 0.0

  for i in range(2,int(x**0.5)+1):
    if elist[i]:
      j = i + i
      while j <= x:
        elist[j] = 0
        j = j + i

  return elist
  


def main():
  f = open('test_data.txt','r',encoding='UTF-8')
  datal = f.readlines()
  
  output =  eratosthenes(int(max(datal)))
  
  i = 0
  for data in datal:
      if output[int(data)] == 1:
        i += 1 

  return i


if __name__ == '__main__':

  start = time.time()
  output = main()
  end = time.time()
  print('eratosthenes','\nresult: ',output,'\ntime: ',end - start)