import string
import random
def user_id_gen_by_user():
   random_letter = ''
   letters = list(string.ascii_letters) + list(string.digits)
   for i in range(10):
       k = random.randint(0,len(letters)-1)
       random_letter = random_letter+letters[k]
   
   return random_letter

if __name__ == '__main__':
    print(user_id_gen_by_user())