# Importing Modules:
from tkinter import*
import random
root=Tk()# main window
root.minsize(250,50)
root.maxsize(250,50)
root.title('Password Genereater')
# All Password Charcters:
special_charcter='!','@','#','%','^','&','*','(',')','_','-','+','=','~','`','/','?','>','.','<'
special_charcter_1='!','@','#','%','^','&','*','(',')','_','-','+','=','~','`','/','?','>','.','<'
capital_letters='Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
capital_letters_1='Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'
small_letters='q','w','r','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
small_letters_1='q','w','r','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
numbers='1','2','3','4','5','6','7','8','9'
numbers_1='1','2','3','4','5','6','7','8','9'
# Genereating Password:
def passwords():
	for x in small_letters,capital_letters,numbers_1,small_letters_1,special_charcter,capital_letters_1,special_charcter_1,capital_letters_1,small_letters_1,numbers:
		password_1=(random.choice(x))
		print(password_1[::-1],end='')
	print(' ')                                    
genereate=Button(root,text='Generete A Pasword',command=passwords)
genereate.pack()
print('The Pasword Are Down Below:')
mainloop()
# End!