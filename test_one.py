# the definition takes a string as input and its job is to return a Boolean depending on the contents of the string.
def str_to_bool(value):
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

## this an updated version of the previous definition, but in this it's possible to reassign the value variable to be lowercase using value.lower().
def str_to_bool(value):
    value = value.lower()
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

# this definition raises an AttributeError if a non-string value is used, this is detected by calling value.lower().
def str_to_bool(value):
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

import unittest

class TestStrToBool(unittest.TestCase):

# the following two assert methods only work for the first two definitions
    def test_y_is_true(self):
         result = str_to_bool('y')
         self.assertTrue(result)

    def test_yes_is_true(self):
         result = str_to_bool('Yes')
         self.assertTrue(result)

# this new assert method works with the third definition
    def test_invalid_input(self):
            with self.assertRaises(AttributeError):
                str_to_bool(1)

# this new assert method works with the third definition

if __name__ == '__main__':
    unittest.main()