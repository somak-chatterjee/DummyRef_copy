"""Rename & Extract Method
"""


class example_class:
    def methodC(self):
        print(0)
        if True:
            x = 1 + 2 + 3
        self.methodD()

    def methodD(self):
        print("Extract_Rename")
