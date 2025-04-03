import time

def music_player():
    repeat_music = False
    while 1:
        user_input = input("enter r repeat music, q to quit:") #getting user input
        user_input.lower()
        if user_input == 'r':
            repeat_music = not repeat_music #toggle repeat
            if repeat_music:
                print("repeat mode ON, playing music.....")
            else:
                print("repeat mode OFF, Stoping music.....")
        elif user_input == 'q':
            print("Exiting music player.")
            break
        while repeat_music:
            print("playing music....")
            time.sleep(2) # simulating song duration

            user_input = input("enter r repeat music, q to quit:") #getting user input
            user_input.lower()
            if user_input == 'r':
                repeat_music = not repeat_music #toggle repeat
                if repeat_music:
                          print("repeat mode ON, playing music.....")
                else:
                      print("repeat mode OFF, Stoping music.....")
            elif user_input == 'q':
                print("Exiting music player.")

print("Welcom to music player\n")
enter_input = input("Enter p to play music\n").lower()
if enter_input == 'p':
     print('playing music.....\n')
     music_player()


