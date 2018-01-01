import lob
import requests
from utils import get_input, get_google_url

lob.api_key = 'test_fd34e1b5ea86a597ec89f7f2e46940c874d'


def create_lob(from_address, to_address, message):
    # Use Lob API to create letter
    try:
        letter = lob.Letter.create(
            description='Letter to Representative',
            # Dictionary from Google response
            to_address=to_address,
            # Dictionary from input
            from_address=from_address,
            file='<html style="padding-top: 3in; margin: .5in;">Dear {{name}},\
            <br><br>{{content}}<br><br><br>Sincerely,<br>{{from_name}}</html>',
            merge_variables={
                'name': to_address['name'],
                'content': message,
                'from_name': from_address['name']
            },
            color=True
        )
    except Exception, e:
        return "Sorry, Couldn't generate a letter with the provided info."

    # Returns the letter to the terminal
    return letter


def generate_letter():
    # Get the input from the command line
    from_address, message = get_input()

    # Generate the URL using the from address input
    google_url = get_google_url(from_address)

    try:
        # Get representative info from google civic info API using user info
        r = requests.get(google_url)

    except Exception as e:
        return "Sorry, Could not find the Representative's information." \
               "Please try again."

    # Load the response
    google_response = r.json()

    # Load representative info into a dictionary
    representative_data = google_response['officials'][0]
    representative_address = representative_data['address'][0]

    to_address = {
        'name': representative_data['name'],
        'address_line1': representative_address['line1'],
        # Because line 2 can be empty, prevents exception
        'address_line2': representative_address.get('line2', ''),
        'address_city': representative_address['city'],
        'address_state': representative_address['state'],
        'address_zip': representative_address['zip']
    }

    # Create letter with above information using Lob
    letter = create_lob(from_address, to_address, message)
    # Print url to the terminal
    print "\nLetter URL:\n{0}\n".format(letter.url)


generate_letter()
