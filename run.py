import os 
import time


#


def main():
    x=0
    for i in range(0,1):
        x+=1     
        try:
            time.sleep(2.5)
            os.system("python3 script.py " + " &")         
            print('running bot # ', x)
        except:
            print('failed bot # ', x)
            break
           


if __name__== "__main__":
  main()


