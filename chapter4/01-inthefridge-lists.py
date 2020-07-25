##def breakfast_sandwich:
##    sandwich = ['bacon', 'cheese', 'sausage']
##    for name in inFridge:
##        check if each item in sandwich is in inFridge
##          if all items are in inFridge:
##        return True
##      print('You can make a breakfast sandwich with what's in the fridge!')
def newItem(addNew):
    addNew = input()
    inFridge.append(addNew)
    print('You have added ' + addNew + '. Here are the items in your fridge:')
    for name in inFridge:
        print('  ' + name)
        

inFridge = ['bacon', 'eggs', 'cheese', 'potatoes']
print('Enter the name of an item:')
name = input()
if name not in inFridge:
    print('I do not have ' + name + ' in the fridge')
else:
    print(name + ' is in the fridge')
print('Would you like to add an item to the fridge?')
addItem = input()
if addItem == 'no':
        print('No problem. Here are the items in your fridge')
        for name in inFridge:
            print('  ' + name)
elif addItem == 'yes':
    print('What would you like to add?')
    newItem(inFridge)
       








