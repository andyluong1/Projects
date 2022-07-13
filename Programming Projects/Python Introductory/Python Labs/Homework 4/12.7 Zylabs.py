# Andy Luong 1525166
# Zylabs 12.7

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        # TODO: Raise excpetion for invalid ages
        return age
    raise ValueError

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = .7 * (220-age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        print("Fat burning heart rate for a {} year-old: {} bpm".format(age,fat_burning_heart_rate(age)))
    except ValueError:
        print("Invalid age.")
        print("Could not calculate heart rate info.\n")