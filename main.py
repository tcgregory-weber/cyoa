# Choose Your Own Adventure game

class Adventure:
    def __init__(self):
        self.story_so_far = ""
        self.game_over = False
        self.sequence = ""
        self.story = {
            '0': "It was a late evening in 1958, and John found himself in his cluttered laboratory,\n" + \
                "surrounded by stacks of research papers and the hum of scientific equipment.\n" + \
                "As a dedicated nuclear scientist, he had been chasing a breakthrough for months,\n" + \
                "devoting countless hours to his work. But tonight, a new challenge confronted him.\n" + \
                "The decision he was about to make would shape not only his career but also his family life.\n"
                "John looked at the clock. It was 8:30pm. He had been working for 12 hours straight.\n" + \
                "He was exhausted, and he knew that he was close to a breakthrough.\n" + \
                "He could feel it in his bones. He could almost taste it.\n" + \
                "But he also knew that he had a family at home, and that he had promised to be there for dinner.\n" + \
                "He had to make a choice. Should he keep working (1), or should he go home (2)?\n",
            '1': "Feeling determined, John decided to keep working. He had been working for 12 hours straight,\n" + \
                "and he was exhausted, but he knew that he was close to a breakthrough.\n" + \
                "Seizing this opportunity could have a profound impact on his career.\n" + \
                "With renewed focus, he returned to his work.\n" + \
                "Hours flew by as he meticulously analyzed data, adjusted variables, and conducted experiments\n" + \
                "The lab became a world of its own,\n" + \
                "illuminated by the soft glow of beakers and the rhythmic hum of machinery.\n" + \
                "Does John make a breakthrough (1), or does something go awry (2)?\n",
            '2': "John decided to go home. He knew the importance of family and the need for balance.\n" + \
                "His wife and children had always been supportive of his work,\n" + \
                "and he wanted to be there for them. He packed up his things and headed home.\n" + \
                "As he stepped out of the lab, he felt a sense of relief.\n" + \
                "He was looking forward to a nice dinner with his family,\n" + \
                "and he knew he had made the right choice.\n" + \
                "Upon reaching a fork in the road, John noticed a peculiar glimmer from a nearby fountain.\n" + \
                "Should he investigate (1), or should he keep driving (2)?\n",
            '11': "John made a breakthrough! The experiments finally yielded the desired results,\n" + \
                "confirming John's hypothesis and opening up new possibilities in nuclear science.\n" + \
                "News of his discovery spread quickly, and he was soon recognized as a leading expert in the field.\n" + \
                "He was invited to speak at conferences around the world, and he was offered a prestigious position\n" + \
                "at a top university. His career was on the rise, and he was on top of the world.\n" + \
                "Should John embrace the spotlight (1) or should he stay humble (2)?\n",
            '12': "Something went awry! The experiments did not yield the desired results,\n" + \
                "and John's hypothesis was disproven. He was devastated.\n" + \
                "He had been so close to a breakthrough, and he had been so confident in his hypothesis.\n" + \
                "He felt like a failure, and he was not sure what to do next.\n" + \
                "Should John give up (1) or should he try again (2)?\n",
            '21': "John decided to investigate. He was curious about the glimmer,\n" + \
                "and he wanted to see what it was. He walked over to the fountain and looked inside.\n" + \
                "He saw a small object at the bottom of the fountain.\n" + \
                "Should he reach in and grab it (1) or should he leave it alone (2)?\n",
            '22': "John decided to keep driving. He was tired and wanted to get home as soon as possible.\n" + \
                "He drove past the fountain and continued on his way.\n" + \
                "As he drove, he thought about his family and the importance of balance.\n" + \
                "He was looking forward to a nice dinner with his family,\n" + \
                "and he knew he had made the right choice.\n" + \
                "THE END\n",
            '111': "John embraced the spotlight. He was excited about his discovery,\n" + \
                "and he wanted to share it with the world. He gave talks at conferences around the world,\n" + \
                "and he accepted the prestigious position at a top university.\n" + \
                "He was on top of the world, and his career was on the rise.\n" + \
                "But as his career took off, he found himself spending less time with his family.\n" + \
                "He was so focused on his work that he neglected his family.\n" + \
                "His wife and children felt neglected, and they grew distant from him.\n" + \
                "John was devastated. He had achieved his dream of becoming a leading expert in the field,\n" + \
                "but he had lost his family in the process.\n" + \
                "THE END\n",
            '112': "John stayed humble. He was excited about his discovery,\n" + \
                "but he did not want to let it go to his head. He continued to work hard and do his best,\n" + \
                "and he was rewarded with a promotion and a raise.\n" + \
                "He was happy with his career, and he was happy with his family.\n" + \
                "He had achieved his dream of becoming a leading expert in the field,\n" + \
                "and he had done it without sacrificing his family.\n" + \
                "THE END\n",
            '121': "John gave up. He was devastated by the failure of his experiments,\n" + \
                "and he did not know what to do next. He decided to quit his job and pursue a different career.\n" + \
                "He was never able to find the same level of success in his new career,\n" + \
                "and he never achieved his dream of becoming a leading expert in the field.\n" + \
                "He was unhappy with his career, and he was unhappy with his family.\n" + \
                "He had sacrificed his career for his family, but he had lost both in the process.\n" + \
                "THE END\n",
            '122': "John tried again. He was devastated by the failure of his experiments,\n" + \
                "but he was determined to find a solution. He continued to work hard and do his best,\n" + \
                "and he eventually made a breakthrough.\n" + \
                "Enter 1 to continue.\n",
            '211': "John reached in and grabbed the object. It was a small golden key.\n" + \
                "He wondered what it was for, he did not have a lot of time,\n" + \
                "but he had to find out what the key was for.\n" + \
                "Should he look for a lock in the fountain (1) or should he look along the road (2)?\n",
            '212': "John left the object alone. He was curious about it, but he did not have a lot of time,\n" + \
                "and he did not want to risk getting caught. He continued on his way.\n" + \
                "He was glad he had made the right choice, and he was looking forward to a nice dinner with his family.\n" + \
                "His children were excited to see him, and his wife had prepared his favorite meal.\n" + \
                "THE END\n",
            '2111': "John looked for a lock in the fountain. He found a small lock on the side of the fountain,\n" + \
                "and he tried the key. It fit perfectly, and the lock opened.\n" + \
                "Inside the lock was a small note. It was a riddle that read:\n" + \
                "What is the answer to life, the universe, and everything?\n" + \
                "Collect change from the fountain to form your answer.\n" + \
                "Should John answer 42 (1) or should he answer 43 (2)?\n",
            '2112': "John looked along the road. He never found a lock, and forgot about the key.\n" + \
                "He was glad he had made the right choice, and he was looking forward to a nice dinner with his family.\n" + \
                "His children were excited to see him, and his wife had prepared his favorite meal.\n" + \
                "THE END\n",
            '21111': "John collected 42 cents from the fountain and placed it in the lock.\n" + \
                "He was not sure if this was how to answer, but he did not know of any other way to answer.\n" + \
                "John waited a minute, and to his amazement, the fountain began to glow.\n" + \
                "The water in the fountain began to swirl, and a small door opened in the side of the fountain.\n" + \
                "John walked into the door, and found himself in a small room.\n" + \
                "The room was filled with books, and in the center of the room was a small table.\n" + \
                "Press 1 to continue.\n",
            '21112': "John collected 43 cents from the fountain and placed it in the lock.\n" + \
                "He was not sure if this was how to answer, but he did not know of any other way to answer.\n" + \
                "John waited for a minute, but nothing happened.\n" + \
                "Disappointed, John left the fountain and continued on his way.\n" + \
                "He was glad he had made the right choice, and he was looking forward to a nice dinner with his family.\n" + \
                "His children were excited to see him, and his wife had prepared his favorite meal.\n" + \
                "THE END\n",
            '211111': "John walked up to the books and as he opened one, he heard the door shut behind him.\n" + \
                "He turned around and saw that there was now a strange man in the room with him.\n" + \
                "The man had no mouth, but he heard clearly in his head:\n" + \
                "You have answered the riddle correctly, please take a seat.\n" + \
                "What is is that you desire about all else?\n" + \
                "John thought for a moment, and then answered:\n" + \
                "Press 1 to continue.\n",
            '2111111': "John answered: I desire to be a leading expert in my field.\n" + \
                "The man nodded, and then said:\n" + \
                "Very well, please take a seat.\n" + \
                "John sat down, and as he did, the man reached for a book, and set it on the table.\n" + \
                "'In here you will find what you seek.'\n" + \
                "John opened the book, and found that it was filled with information about his field.\n" + \
                "He was amazed, and he began to read.\n" + \
                "He read for hours, and when he was done, he closed the book.\n" + \
                "When he looked up, the man was gone and the door was open.\n" + \
                "John walked out of the room, and found himself back at the fountain.\n" + \
                "He immediately returned to his lab to begin his experiments,\n" + \
                "now knowing exactly what he needed to do.\n" + \
                "Press 1 to continue.\n",
            '21111111': "Upon returning to his lab, John began his experiments.\n" + \
                "He followed what he had read in the book, and was easily able to replicate the results.\n" + \
                "He was amazed that the book had given him all the information he needed.\n" + \
                "News of his discovery spread quickly, and he was soon recognized as a leading expert in the field.\n" + \
                "He was invited to speak at conferences around the world, and he was offered a prestigious position\n" + \
                "at a top university. His career was on the rise, and he was on top of the world.\n" + \
                "Should John embrace the spotlight (1) or should he stay humble (2)?\n"                
        }

    def start(self):
        print("Welcome to the Choose Your Own Adventure game!\n" + \
            "You will be presented with a series of choices. Enter 1 for the first choice,\n" + \
            "and 2 for the second choice. You can also type 'quit' at any time to exit the game.\n" + \
            "Let's begin!\n")
        self.sequence = "0"


    def play(self):
        self.start()
        while not self.game_over:
            print(self.story[self.sequence])
            if self.sequence == "0":
                self.sequence = ""
            print("What happens next?")
            next_move = input()
            if next_move == "1":
                self.sequence += "1"
            elif next_move == "2":
                self.sequence += "2"
            elif next_move == "quit":
                self.game_over = True
            else:
                print("Invalid input. Please try again.")
                continue

            # This is just to have it jump back to a previous sequence
            if self.sequence == "122":
                self.story_so_far += (self.story[self.sequence] + "\n")
                self.sequence = "11"
            elif self.sequence == "211111111":
                self.story_so_far += (self.story["21111111"] + "\n")
                self.sequence = "111"
            elif self.sequence == "2111111112":
                self.story_so_far += (self.story["21111111"] + "\n")
                self.sequence = "112"


            
            self.story_so_far += (self.story[self.sequence] + "\n")
            if "THE END" in self.story[self.sequence]:
                print(self.story[self.sequence])
                self.game_over = True
        self.print_story_to_file()

    def print_story_to_file(self):
        with open("story.txt", "w") as f:
            f.write(self.story_so_far)

if __name__ == "__main__":
    adventure = Adventure()
    adventure.play()


