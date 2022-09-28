
import io
import sys


def capture_output(func, *args):
    """ 
    Capture console output resulting from funcion func() so it can be used in tests.
    
    Input: a function that prints something to the console
    Returns: a string consisting of the console output
    """
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    func(*args)

    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()
