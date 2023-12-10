## pnum1, main関数以外の関数は 
## @ppza53893さんのqiita(https://qiita.com/ppza53893/items/e0f464340d6f97760cd5)に記載されている関数を引用しました.
import random
import time

# シンプルO(x)
def pnum1(x):
  if x <= 1:
    return False

  for i in range(2,x-1):
    if x % i == 0:
      return False
  return True


# Wheel factorization 2,3,5 が既知の素数として7からスタート
def trial_wheel_factorize(n: int):
    assert n > 1
    if n in [2, 3, 5]:
        return True
    elif n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    i = 7
    c = 0
    wheel = [4, 2, 4, 2, 4, 6, 2, 6]
    while i < n**0.5+1:
        if n%i == 0:
            return False
        i += wheel[c%8]
        c += 1
    return True

## ミラーラビン 素数判定法
def mr_test_normal(n: int):
    assert n > 1
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    d = n - 1
    s = 0
    while d & 1 == 0:
        s += 1; d >>= 1
    
    k = 20
    for _ in range(k):
        a = random.randint(2, n-1)
        x = pow(a, d, n) # a^d mod n
        if x == 1 or x == n-1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == n-1: # a^(d*2^r) mod n
                break
        else: return False
    return True

## ミラーラビン K不使用
def mr_test(n: int):
    assert n > 1
    if n == 2:
        return True
    elif n%2 == 0:
        return False
    assert n < int(3.317 * 10**24)

    d = n - 1
    s = 0
    while d & 1 == 0:
        s += 1; d >>= 1
    it = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)
    for a in it:
        if a == n:
            return False
        a %= n
        x = pow(a, d, n) # a^d mod n
        if x == 1 or x == n-1:
            continue
        for _ in range(s):
            x = pow(x, 2, n)
            if x == n-1: # a^(d*2^r) mod n
                break
        else: return False
    return True



## テストデータ実行用
def main(algorithm):
  f = open('test_data.txt','r',encoding='UTF-8')
  datal = f.readlines()
  output = [0] * len(datal)

  i = 0
  ## pnum 判定
  for data in datal:
    
    ## 素数判定関数
    result = algorithm(int(data))

    output[i] = int(result)
    i += 1

  return sum(output)


if __name__ == '__main__':

  start = time.time()
  output = main(pnum1)
  end = time.time()
  print('algorithm: 単純素数判定','\nresult: ',output,'\ntime: ',end - start)
  print("-----")
  
  start = time.time()
  output = main(trial_wheel_factorize)
  end = time.time()
  print('algorithm: Wheel factorization','\nresult: ',output,'\ntime: ',end - start)
  print("-----")
  
  start = time.time()
  output = main(mr_test_normal)
  end = time.time()
  print('algorithm: ミラーラビン素数判定法(kを使用)','\nresult: ',output,'\ntime: ',end - start)
  print("-----")
  
  start = time.time()
  output = main(mr_test)
  end = time.time()
  print('algorithm: ミラーラビン素数判定法(k不使用)','\nresult: ',output,'\ntime: ',end - start)
  print("-----")
