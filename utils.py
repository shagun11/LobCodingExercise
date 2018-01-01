import os
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


def get_input():
    # Get input from the command line and store
    # the response into a dictionary

    from_address = {
        'name': raw_input('From Name: '),
        'address_line1': raw_input('From Address Line 1: '),
        'address_line2': raw_input('From Address Line 2: '),
        'address_city': raw_input('From City: '),
        'address_state': raw_input('From State: '),
        'address_country': raw_input('From Country: '),
        'address_zip': raw_input('From Zip Code: '),
    }
    message = raw_input('Message: ')
    return from_address, message


def get_google_url(from_address):
    # Format address string to create url for google API

    from_address_string = ''.join([
        from_address['address_line1'],
        from_address.get('address_line2', ''),
        from_address['address_city'],
        from_address['address_state'],
        from_address['address_country'],
        from_address['address_zip'],
    ])

    # Create custom url with user info
    get_rep_url = "https://www.googleapis.com/civicinfo/v2/representatives?" \
                  "address={0}&includeOffices=true&levels=administrativeArea1&" \
                  "roles=headOfGovernment&key={1}".format(from_address_string,
                                                          GOOGLE_API_KEY)

    return get_rep_url
