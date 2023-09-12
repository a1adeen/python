# ROBO SPEAKER
import os



if __name__ == '__main__':
    while True:
     print('welcome to robo speaker')
     x = input('enter what to want to say')
     if x == 'quit':
         break
     command = f'say {x}'
     os.system(command)


