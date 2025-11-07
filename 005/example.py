def person(name, age, city):
    print ({
        "name": name,
        "age": age,
        "city": city
    })

data = {
    "name": "Jane",
    "age": 41,
    "city": "Finland"
}

person( **data )