
my_word = "antidisestablishmentarianism"
print(len(my_word))

string_left = "bat"
string_right = "man"
print(string_left + string_right)


string_one = "heebie"
string_two = "jeebies"
print(string_one + " " + string_two)

string1 = "Animals"
string2 = "Badger"
string3 = "Honey Bee"
string4 = "Honeybadger"

print(string1.lower())
print(string2.lower())
print(string3.lower())
print(string4.lower())


a = input("Enter a number: ")
b = input("Enter another number: ")
product = float(a) * float(b)
print("The product of " + a + " and " + b + " is " + str(product) + ".")



my_input = input("Type something: ")
print(my_input.find("X"))

my_text = input("Enter some text: ")

my_text = my_text.replace("a", "4")
my_text = my_text.replace("b", "8")
my_text = my_text.replace("e", "3")
my_text = my_text.replace("l", "1")
my_text = my_text.replace("o", "0")
my_text = my_text.replace("s", "5")
my_text = my_text.replace("t", "7")

print(my_text)


def invest(amount, rate, years):
    """Display year on year growth of an initial investment"""
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate = float(input("Enter an anual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)

captains = {}

captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"


if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"
if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}.")

del captains["Discovery"]

captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ]
)



