class LockedClass:
    __slots__ = ("first_name",)

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError("Adding new attributes is not allowed!")
        super().__setattr__(name, value)

