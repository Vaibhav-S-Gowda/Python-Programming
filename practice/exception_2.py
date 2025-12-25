class DuplicateUserError(Exception):
    pass

class WeakPasswordError(DuplicateUserError):
    pass

class User:

    user_name = set()

    def __init__(self, un, mob, pwd):
        self.un = un
        self.mob = mob
        self.pwd = pwd
        self.add_user()
        self.validate()

    def add_user(self):
        if self.un in User.user_name:
            raise DuplicateUserError\
            ('Username already exist')
        else:
            User.user_name.add(self.un)

    def validate(self):
        uc = lc = sp = num = 0
        for i in self.pwd:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isdigit():
                num += 1
            else:
                sp += 1

        if len(self.pwd) < 6 or uc == 0 or\
        lc == 0 or num == 0 or sp == 0:
            raise WeakPasswordError \
            ('Password not strong enough')
        
def main():
    un = 'VaibHin'
    mob = 2234556
    pwd = '@Hin2330'
    try:
        u1 = User(un, mob, pwd)
    except DuplicateUserError as e:
        print(e)
    except WeakPasswordError as e:
        print(e)
    except:
        print('Exception occured')
    else:
        print('Account created successfully')

main()