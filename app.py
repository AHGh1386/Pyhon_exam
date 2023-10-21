import helper


participants = []
while True:
    user_input = input("insert 'reg' o enroll,'info' to get your information,'admin' enter admin control panel: ").lower()
    if user_input == "reg":
        while True:
            lec_check = input("Are you a lecturer ? (Yes or No)").lower()
            if lec_check == "yes":
                lec = helper.get_lecturer_info()
                participants.append(lec)
                break
            else:
                std = helper.get_student_info()
                participants.append(std)
                break
            
                
                     
    elif user_input == "info":
            while True:
                user_code = input(
                    "Please enter your Code(enter 'back' to exit): ").lower()
                if user_code == "back":
                    break
                for item in participants_list:
                    if item.code == user_code:
                        item.show_info()
                        break
                else:
                    print(
                        "Your code is not correct or You're not register in our list.")
        elif user_input == "admin":
            while True:
                admin_code = input(
                    "Please enter your Administrator code: ")
                if admin_code == "0000":
                    helper.create_csv(participants_list)
                    helper.create_json(participants_list)
                    print("Your files has been created")
                    break
                else:
                    print("Wrong Code!")
                    break
        else:
            print("Wrong Option!")
