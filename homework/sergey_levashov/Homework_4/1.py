my_dict = {
    'tuple': (6, 8, 6, "bmx", "snowboard"),
    'list': ["trick", "barspin", 360, 180, True],
    'dict': {'eggs': 2,
              'milk': 100,
              3: 'tomato',
              False: 'chicken',
              True: 'cheese'
              },
    'set': {True, 2, 3, 4, False}
           }

print(my_dict["tuple"][-1])

my_dict["list"].append("talewhip")
my_dict["list"].pop(1)
my_dict["dict"][('i am a tuple',)] = 'yes'
my_dict["dict"].pop(False)
my_dict['set'].add(5)
my_dict["set"].pop()

print(my_dict.items())
