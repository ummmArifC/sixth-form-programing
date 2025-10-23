# membership for rock climbing 
# allow entry of more than oone membership
# retrieve details form a file
# allow searching for stored users 

membership = []
while True:
    name = input('enter your name:')
    phone_number = int(input('enter your phone number:'))
    emergency_contact_number = int(input('enter an emergency contact number:'))
    age = int(input('enter your age:'))
    expirience = input('enter the level of rock climber you are (beginner/intermediate/expert):')
    
    print('\n--------------MEMBERSHIP DETAILS-----------------')
    print('name:' + str(name))
    print('phone number:' + str(phone_number))
    print('emergency contact number:' + str(emergency_contact_number))
    print('age:' + str(age))
    print('expirience' + str(expirience)) 


    confirm = input('are the details correct,(yes/no)').strip().lower()
    if confirm == 'yes':
        membership.append({
        'name': name,
        'phone number': phone_number,
        'emergency contact number': emergency_contact_number,
        'age': age,
        'expirience': expirience,
    }) 
           
    print('membership details saved!\n')    
    break
else:
    print('details have been erased, you can now re-enter the data') 
   


    