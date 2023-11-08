# Function 1
def get_current_weather(location, unit='fahrenheit'):
    # This function is a placeholder for getting current weather
    # Replace with actual API call or logic to get weather
    return {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }

# Function 2
def calculate_tax(amount, tax_rate):
    return amount * tax_rate

# Function 3
def generate_password(length):
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function 4
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Function 5
def get_file_extension(filename):
    return filename.split('.')[-1]

# Function 6
def convert_km_to_miles(km):
    return km * 0.621371

# Function 7
def send_email(sender, receiver, subject, body):
    # Placeholder function for sending an email
    print("Email sent from", sender, "to", receiver)

# Function 8
def sort_list(input_list):
    return sorted(input_list)

# Function 9
def is_prime(number):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if (number % i) == 0:
                return False
        return True
    else:
        return False

# Function 10
def countdown_timer(seconds):
    import time
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
