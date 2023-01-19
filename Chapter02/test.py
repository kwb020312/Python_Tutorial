class Woobin:
    def __init__(self, friends):
        self.friends = friends
    def who(self):
        for cur in self.friends:
            print(cur)

test = Woobin(['영훈', '원석'])

test.who()