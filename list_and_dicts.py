def run():
    my_list = [1,'hello',True,4.5]
    my_dict = {"firstname":"Walther","lastname":"Smith"}

    super_list = [
        {"firstname":"Walther","lastname":"Smith"},
        {"firstname":"Juan","lastname":"Garcia"},
        {"firstname":"Diego","lastname":"Quiroz"},
        {"firstname":"Andres","lastname":"Paez"},
        {"firstname":"Camila","lastname":"Saenz"},
    ]

    super_dict = {
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,2.2,3.3,4.4,5.5],
    }


    for key,value in super_dict.items():
        print(f"{key}:{value}")


if __name__ == '__main__':
    run()