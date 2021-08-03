class example:
    def methodA(self):
        self.methodB()

    def methodB(self):
        ext_obj = obj1.func1()
        obj = ext_obj.func2().func3()
        print("End")
