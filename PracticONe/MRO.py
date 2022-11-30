class A:
    def rk(self):
        print("In class A")


# Example of Method resolution Order

class B:
    def rk(self):
        print("In class B")


r = B()
r.rk()
