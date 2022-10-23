# 9/26/22

class FilenameNotFoundError(Exception):

    def __init__(self, filename):
        self.filename = filename
        super().__init__(self.filename)


class FilenameAlreadyExistsError(Exception):

    def __init__(self, filename):
        self.filename = filename
        super().__init__(self.filename)
        