import random

def gen_data():
  n = random.randint(1,750)
  f = open('test_data.txt','w',encoding='UTF-8')
  
  for i in range(n):
    test = random.randint(2,10**8)
    f.write(str(test)+"\n")
  f.close
if __name__ == "__main__":
  gen_data()

