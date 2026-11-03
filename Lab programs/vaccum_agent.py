def vaccum_agent(location,statusA,statusB):
    if location=="A" and statusA=="Dirty":
        return "SUCK"
    elif location =="B" and statusB=="Dirty":
        return "SUCK"
    elif statusA=="Dirty":
        return "Left"
    elif statusB=="Dirty":
        return "Right"
    else:
        return "No-op"

def vaccum_simulation(location,statA,statB):
    print(f"Start Location:{location}  Status A:{statA}   Status B:{statB}")
    while True:
        action = vaccum_agent(location,statA,statB)
        if action=="No-op":
            break
        if action=="SUCK" and location=="A":
            statA="Clean"
        elif action=="SUCK" and location=="B":
            statB="Clean"
        elif action=="Left":
            location="A"
        elif action=="Right":
            location="B"
        print(f"-----> Action:{action}   Current Location : {location}   Status A:{statA}  Status B:{statB}")
    print(f"Final Location:{location}  Status A:{statA}   Status B:{statB}")

print("----------------------------")
print("-------Test Cases-----------")
print("----------------------------")

print("Test Case 1")
vaccum_simulation("A","Dirty","Dirty")

print("Test Case 2")
vaccum_simulation("A","Clean","Dirty")

print("Test Case 3")
vaccum_simulation("B","Clean","Clean")

print("Test Case 4")
vaccum_simulation("B","Dirty","Dirty")

print("Test Case 5")
vaccum_simulation("B","Dirty","Clean")

print("Test Case 6")
vaccum_simulation("B","Clean","Dirty")

print("Test Case 7")
vaccum_simulation("A","Clean","Clean")

