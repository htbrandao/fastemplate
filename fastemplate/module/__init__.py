# ========================================================== #
# Mock examples to interact the api without sending new data #
# ========================================================== #

# Base cart ------------------------------------------------ #
MOCK_BASE_CART = {
    'breakfast': {
        'milk': 5.0,
        'capuccino': 3.0,
        'banana': 2.5,
    },
    'dinner': {
        'wine': 3.0,
        'potato': 2.45,
        'fish': 20.75,
        'ice cream': 8.30
    }
}

# Fridge --------------------------------------------------- #
MOCK_FRIDGE = {
    'rice': {'amount': 2, 'unit': 'kg'},
    'beans': {'amount': 1, 'unit': 'kg'},
    'green salad': {'amount': 500, 'unit': 'g'},
    'ice cream': {'amount': 1, 'unit': 'box'},
    'candy': {'amount': 2, 'unit': 'units'}
}

MOCK_CELSIUS_TEMPERATURES = '-18.0 -18.5 -19.0 -19.5 -20.0'.split()

# Owner/Admin ---------------------------------------------- #
MOCK_FRIDGE_USERS = {
    'iPayMyBills': {
        'username': 'iPayMyBills',
        'full_name': 'Working Class',
        'hashed_password': '4br4',
        'owner': True
    },
    'Blacklicious': {
        'username': 'Blacklicious',
        'full_name': 'Mr. Comfy Slippers',
        'hashed_password': 'k4d4br4',
        'owner': False
    }
}
