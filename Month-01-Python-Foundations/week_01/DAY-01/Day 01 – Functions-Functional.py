def shipping_label(*args, **kwargs):
    # Printing name from positional arguments
    for arg in args:
        print(arg, end=" ")
    print()
    
    # Printing address details from keyword arguments
    if "apartment" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")


shipping_label("Dr.", "SpongeBob", "Harold", "SquarePants", 
               street="123 Fake St", apartment="100", 
               city="Detroit", state="Michigan", zip="54321")


def atteancee_list(*names,**details):
    for name in names:
        print(name)
    print()
    for key, value in details.items():
        print(f"{key}: {value}")

atteancee_list("SpongeBob", "Patrick", "Squidward",
                date="2024-06-01", time="10:00 AM", location="Bikini Bottom Community Center")

#Decorators
            