example = open("example.txt", "r")
final = open("final.txt", "r")


class Scratchcard:
    winning_nums = []
    played_nums = []
    matches = 0
    number_of_cards = 1
    
    def __init__(self, line):
        # Process the line into two sorted lists of integers, one for the winning numbers, and one for the played
        # numbers on the card. This makes it easier to then process the number of points
        line = line.split(':')[1]
        winning_nums, played_nums = line.strip().split(' | ')
        winning_nums = map(lambda x: 0 if x == '' else int(x), winning_nums.split(' '))
        self.winning_nums = list(filter(lambda x: x, winning_nums))
        played_nums = map(lambda x: 0 if x == '' else int(x), played_nums.split(' '))
        self.played_nums = list(filter(lambda x: x, played_nums))
        self.winning_nums.sort()
        self.played_nums.sort()

        self.find_matches() # Once line is process into two lists, find the number of matches
        
    def find_matches(self):
        current_num = self.winning_nums.pop(0)  # Take the first winning number
        while self.played_nums:  # If we still have played numbers to process
            # Check if current winning number is smaller than the current played number
            if current_num < self.played_nums[0]:  
                if self.winning_nums:
                    current_num = self.winning_nums.pop(0)  # If there are any winning numbers left, get another
                else:
                    break  # If not, stop looking, as there can be no matches with no winning numbers
            else:
                if current_num == self.played_nums[0]: self.matches += 1
                self.played_nums.pop(0)


def get_num_of_scratchcards(file):
    scratchcards = get_scratchcards(file) # Get a list of all the scratchcards in one file
    for index in range(len(scratchcards)): # Loop through the scratchcards
        scratchcard = scratchcards[index]
        """
        Loop through the next few cards equal to the number of matches on the current scratchcard. Increment the number
        of those scratchcards by the number of current scratchcards.
        """
        for step in range(scratchcard.matches):
            scratchcards[index + step + 1].number_of_cards += scratchcard.number_of_cards

    # Get the sum of how many scratchcards there are after the multiplication of cards by matches.
    num_scratchcards = list(map(lambda scratchcard: scratchcard.number_of_cards, scratchcards))
    return sum(num_scratchcards)


def get_scratchcards(file):
    scratchcards = []
    for line in file.readlines():
        scratchcards.append(Scratchcard(line)) # Create a scratchcard object with each line
    return scratchcards


print(f"Example Result: {get_num_of_scratchcards(example)}")
print(f"Expected Example Result: 30")
print(f"Actual Test Result: {get_num_of_scratchcards(final)}")

example.close()
final.close()