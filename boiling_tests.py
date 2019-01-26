""" Test functions in boiling.py """
import boiling

def test_is_name_private_smoke():
    """ Test boiling.is_name_private with always public user """
    assert boiling.is_name_private('instagram') is not True

def test_is_private_bool_smoke():
    """ Test boiling.is_private_bool """
    test_script_dict = {
        'entry_data': {
            'ProfilePage': [{
                'graphql': {
                    'user': {
                        'is_private': True}}}]}}
    assert boiling.is_private_bool(test_script_dict) is True
