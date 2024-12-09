from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

while 1:
    sense.show_message("Welcome to ()!", scroll_speed=0.06)
    sense.show_message("Press any button to start!", scroll_speed=0.06)
    for event in sense.stick.get_events():
        if event.action == "pressed":
            sense.clear()
            break
    else:
        continue
    break

questions = [
    ("What is the largest continent?", ["Africa", "Asia", "Europe", "North America"], 1),
    ("What is the process by which plants make their own food using sunlight?", ["Respiration", "Digestion", "Photosynthesis", "Germination"], 2),
    ("What is the longest river in the world?", ["Amazon River", "Nile River", "Mississippi River", "Yangtze"], 1),
    ("Which of these is an example of a solid?", ["Water", "Ice", "Air", "Vapor"], 1),
    ("Who was the first president of the United States?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], 0),
    ("What is the largest desert in the world?", ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Kalahari Desert"], 0),
    ("How many continents are there on Earth?", ["5", "6", "7", "8"], 2),
    ("Which animal is the fastest on land?", ["Horse", "Lion", "Kangaroo", "Cheetah"], 3),
    ("What is the tallest mountain in the world?", ["Mountain Everest", "K2", "Mount Kilimanjaro", "Mount Fuji"], 0),
    ("What gas do plants absorb from the atmosphere for photosynthesis?", ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"], 0),
    ("Which ocean is the largest on Earth?", ["Atlantic Ocean", "Pacific Ocean", "Arctic Ocean", "Indian Ocean"], 1),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", ["Sally Ride", "Bessie Coleman", "Amelia Earhart", "Harriet Quimby"], 2),
    ("What is the capital of the United States?", ["Los Angeles", "New York", "Chicago", "Washington"], 3),
    ("What is the capital of Indiana?", ["Gary", "Indianapolis", "Bloomington", "Fort Wayne"], 1),
    ("How many states are there in the United States?", ["49", "50", "51", "48"], 1),
    ("Who invented the light bulb?", ["Albert Einstein", "Nikola Tesla", "Thomas Edison", "Benjamin Franklin"], 2),
    ("What is the largest country in the world?", ["United States", "Canada", "China", "Russia"], 3),
    ("How many colors are there in the rainbow?", ["5", "6", "7", "8"], 2),
    ("What is the main purpose of the heart?", ["Pumping blood", "Digest food", "Process thoughts", "Storing energy"], 0),
    ("Which animal is known for its ability to change color?", ["Kangaroo", "Dolphin", "Chameleon", "Tiger"], 2),
    ("How many planets are there in our solar system?", ["6", "7", "8", "9"], 2),
    ("What do you call a baby frog?", ["Cub", "Tadpole", "Calf", "Kitten"], 1),
    ("What is the process where water turns into a vapor?", ["Condensation", "Precipitation", "Evaporation", "Sublimation"], 2),
    ("What is the largest bird in the world?", ["Ostrich", "Eagle", "Penguin", "Flamingo"], 0),
    ("Which ocean is the smallest?", ["Atlantic Ocean", "Arctic Ocean", "Indian Ocean", "Pacific Ocean"], 1),
    ("What is the name of the famous clock tower in London?", ["Big Ben", "Leaning Tower", "Eiffel Tower", "Liberty Bell"], 0),
    ("What do you call a baby kangaroo?", ["Joey", "Cub", "Pup", "Calf"], 0),
    ("What is the largest island in the world?", ["Australia", "Greenland", "Madagascar", "Iceland"], 1),
    ("Which animal has 8 arms?", ["Squid", "Jellyfish", "Octopus", "Starfish"], 2),
    ("Which planet in our solar system is known for having rings?", ["Venus", "Jupiter", "Saturn", "Pluto"], 2),
    ("Which of these is a type of cloud formation?", ["Rainbow", "Cirrus", "Thunderstorm", "Sunbeam"], 1),
    ("What is the smallest U.S. state?", ["Rhode Island", "Delaware", "Vermont", "New Hampshire"], 0),
    ("What part of a plant absorbs water and nutrients?", ["Stem", "Roots", "Leaves", "Flowers"], 1),
    ("What is the process when a caterpillar turns into a butterfly?", ["Photosynthesis", "Hibernation", "Metamorphosis", "Germination"], 2),
    ("What state is known as the home of the Statue of Liberty?", ["Washington D.C.", "Seattle, WA", "Boston, MA", "New York City, NY"], 3),
    ("What do we call the imaginary line that divides the North and South Hemisphere?", ["Prime Meridian", "Equator", "The Divider", "Arctic Circle"], 1),
    ("What is the process in which a liquid is changed to a solid referred to?", ["Freezing", "Melting", "Evaporation", "Condensation"], 0),
    ("What gas do humans exhale?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], 2),
    ("What is the longest river in North America?", ["Amazon River", "Mississippi River", "Colorado River", "Rio Grande"], 1),
    ("Which part of the plant makes seeds?", ["Stem", "Roots", "Flower", "Leaves"], 2),
    ("Which of these is a synonym for 'happy'?", ["Sad", "Angry", "Joyful", "Tired"], 2),
    ("What is the freezing point of water in degrees Celsius?", ["32", "0", "100", "-1"], 1),
    ("What is the largest type of bear?", ["Black Bear", "Grizzly Bear", "Polar Bear", "Panda Bear"], 2),
    ("What is the boiling point of water in degrees Celsius?", ["90", "100", "110", "120"], 1),
    ("Which of these is a continent?", ["Africa", "Antarctica", "Asia", "All of the above"], 3),
    ("Which of these is NOT a renewable resource?", ["Solar Energy", "Wind Energy", "Coal", "Hydropower"], 2),
    ("Which of these is a landform?", ["River", "Mountain", "Ocean", "Cloud"], 1),
    ("Which of these is a herbivore?", ["Wolf", "Lion", "Elephant", "Shark"], 2),
    ("Which animal can live in both water and on land?", ["Fish", "Bird", "Amphibian", "Reptile"], 2),
    ("Which of these animals is not a mammal?", ["Dolphin", "Bat", "Fish", "Whale"], 2),
    ("Which of these is a weather phenomenon?", ["Earthquake", "Tornado", "Volcano", "Avalanche"], 1),
    ("What is the smallest country in the world?", ["United States", "Canada", "Vatican City", "United Kingdom"], 2),
    ("Which is not a form of precipitation?", ["Rain", "Snow", "Hail", "Wind"], 3),
    ("Which of these is NOT a type of rock?", ["Igneous", "Sedimentary", "Metamorphic", "Muddy"], 3),
    ("What is the name of the first manned space mission to the moon?", ["Apollo 13", "Apollo 11", "Gemini 5", "Mercury 7"], 1),
    ("What do you call the process of water turning into gas?", ["Condensation", "Freezing", "Evaporation", "Melting"], 2),
    ("What is the hardest natural substance on earth?", ["Gold", "Iron", "Diamond", "Steel"], 2),
    ("What do you call a group of birds?", ["Pack", "School", "Flock", "Colony"], 2),
    ("What do we call a person who studies stars and planets?", ["Astronomer", "Biologist", "Chemist", "Doctor"], 0),
    ("Which of these animals can regenerate lost body parts?", ["Shark", "Starfish", "Giraffe", "Elephant"], 1),
    ("What is the name of the system of bones in the human body?", ["Nervous System", "Respiratory System", "Skeletal System", "Circulatory System"], 2),
    ("What animal is known for building dams?", ["Beaver", "Rabbit", "Bear", "Deer"], 0),
    ("Which of these countries is in South America?", ["Canada", "Argentina", "Australia", "China"], 1),
    ("Which of these animals is nocturnal?", ["Owl", "Squirrel", "Dog", "Deer"], 0),
    ("Which of these is the closest star to Earth?", ["Alpha Centauri", "Proxima Centauri", "The Sun", "Sirius"], 2),
    ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], 2),
    ("Which of these animals is known for its ability to fly backwards?", ["Bird", "Bat", "Hummingbird", "Butterfly"], 2),
    ("What do we call a baby horse?", ["Calf", "Foal", "Lamb", "Cub"], 1),
    ("Which of these is a type of tree that does not lose its leaves in winter?", ["Oak", "Pine", "Maple", "Birch"], 1),
    ("What do we call a group of stars that form a pattern in the sky?", ["Galaxy", "Comet", "Constellation", "Planet"], 2),
    ("Which of these planets is closest to the Sun?", ["Venus", "Earth", "Mercury", "Mars"], 2),
    ("What is the force that pulls objects towards the Earth?", ["Magnetism", "Gravity", "Friction", "Inertia"], 1),
    ("What do you call the boundary between two tectonic plates?", ["Rift", "Volcano", "Fault", "Mountain"], 2),
    ("What year did Christopher Columbus sail to America?", ["1492", "1620", "1776", "1498"], 0),
    ("What was the name of the ship that carried the Pilgrims to America in 1620?", ["Mayflower", "Santa Maria", "Nina", "Pinta"], 0),
    ("Which ocean is on the east coast of the United States?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], 1),
    ("Which of these words is an adjective?", ["Quickly", "Beautiful", "Swim", "Run"], 1),
    ("Which of these words is a noun?", ["Quickly", "Cat", "Jump", "Laugh"], 1),
    ("What is the past tense of 'go'?", ["Went", "Going", "Gone", "Goes"], 0),
    ("What is the capital of Canada?", ["Toronto", "Montreal", "Ottawa", "Vancouver"], 2),
]

def get_answer(question_data, question_number):
    question, options, correct_answer = question_data
    sense.clear()
    
    while 1:
        sense.show_message(f"Q{question_number}: {question}", scroll_speed=0.06)
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "up":
                    return 0
                elif event.direction == "down":
                    return 1
                elif event.direction == "left":
                    return 2
                elif event.direction == "right":
                    return 3

question_number = 1
for question_data in questions:
    user_answer = get_answer(question_data, question_number)
    if user_answer == question_data[2]:
        sense.show_message("Correct!", text_colour=[0, 255, 0], scroll_speed=0.06)
    else:
        sense.show_message("Wrong!", text_colour=[255, 0, 0], scroll_speed=0.06)
    question_number += 1

sense.clear()
