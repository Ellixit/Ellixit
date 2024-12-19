def intro():
    name = "Jeffrey Xiao"
    current_focus = ["Cybersecurity", "Cloud Computing", "Web Development"]
    hobbies = ["Hiking", "Camping", "Skiing", "Programming", "Guitar"]
    role = "Army ROTC Senior Cadet"
    
    print(f"Hello, I'm {name}!")
    print(f"\nI {'love' if 'Programming' in hobbies else 'like'} programming and exploring technology.")
    print("\nCurrently, I'm focusing on:")
    for focus in current_focus:
        print(f"  - {focus}")
    print("\nWhen I'm not coding, you might find me:")
    for hobby in hobbies:
        print(f"  - {hobby}")
    print("\nLet's connect and build something great together!")
    
intro()
