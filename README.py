def intro():
    name = "Jeffrey Xiao"
    current_focus = ["Security", "Cloud Computing", "Web Development"]
    hobbies = ["Hiking", "Camping", "Skiing", "Programming", "Photography", "Playing Guitar"]
    personal_website = "jeffreyxiao.info/"
    
    print(f"Hello, I'm {name}!")
    print(f"\nI love programming and exploring technology.")
    print("\nCurrently, I'm focusing on:")
    for focus in current_focus:
        print(f"  - {focus}")
    print("\nWhen I'm not coding, you might find me:")
    for hobby in hobbies:
        print(f"  - {hobby}")
    print("\nLet's connect and build something great together!")
    
intro()
