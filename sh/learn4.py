'''accountname = 'kadhar'
accountbalance = 500
accountpassword = 'whatis'

while True:
    print('press b to get the bank balance \n press d to make to deposit \n press w to make a withdrawal \n press s to show the account \n press q to quit')

    action = input('what do you want to do ???')
    action = action.lower()
    action = action[0] # taking only first letter of the string 

    if action == 'b':
        print('GETTING BALANCE YOU NEED TO PROVE THAT YOU ACCOUNT')
        userPassword  = input('enter your password : ')
        if userPassword != accountpassword :
            print('inccort password')
        else: 
            print('YOUR BALANCE :', accountbalance)
    if action == 'd':
        print('depoist')
        userPassword  = input('enter your password : ')
        if userPassword != accountpassword :
            print('inccort password')
        else:
            userdeposit = input('enter your number how much you deposit')
            userdeposit = int(userdeposit)

            if userdeposit < 0 :
                print('you can not enter less than zero values')
            #elif userdepodsit == userdeposit.isalpha():
             #d   print('enter text is not please enter number')
            else:
                print(accountbalance + userdeposit)
    if action == 's':
        print('account number  :', accountname , '\n','account balance' , accountbalance,)
    if action == 'w':
        print('withdrawl ammount')
        withdraw = input('enter ammount you want to with draw :') 
        withdraw = int(withdraw)
        userPassword = input('enter your passward')
        if withdraw < 0 :
            print('you cannot enter less than zero')
        elif userPassword  !=  accountpassword :
            print('password is incorret') 
        elif withdraw > accountbalance :
            print('you cant with draw greater then balance')
    if action == 'q':
        break
'''
#object orient programming put all together

class Account_details():
    def __inti__(self,name,balance,password):
        self.name = name
        self.password = password 
        self.balance = int(balance)
    