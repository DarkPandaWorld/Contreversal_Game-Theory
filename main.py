import simulation1 as sim1
import simulation2 as sim2
import simulation1_5 as sim1_5

# Change the followng lines to adjust the simulations
games = 500          # Here we define the number of games that we run 
chosen = 2          # This variable can be used to choose which simulation to run, e.g., sim1 or sim2

# We define some variables for some statistics
human_wins = 0
bot_wins = 0

# We gather the total scores of the human and bot players
human_total_score = 0
bot_total_score = 0

# We create a mapping of the simulations to choose from, s.t. we only need to change one variable to switch between them
sim_map = {
    1: sim1,
    2: sim2,
    1_5: sim1_5
}

# We check if the chosen simulation is valid (Error handling)
if chosen not in sim_map:
    raise ValueError("chosen must be 1 or 2")

# We get the simulation object based on the chosen variable
sim = sim_map[chosen]

# We run the simulation for the defined number of games
for i in range(games):

    # We simulate the game and get the scores
    (human_score, bot_score) = sim.simulate_game(i) 

    # We add the scores to the total scores
    human_total_score += human_score
    bot_total_score += bot_score

    # We check who won the game and add to the win counter
    if(human_score > bot_score):
        human_wins += 1
        print(f"Game {i+1}: Human wins with score {human_score} vs Bot score {bot_score}")
    elif(human_score < bot_score):
        bot_wins += 1
        
# We print the results of the simulation, to analyse them
print(f"For {games} games, we get the ratio of human wins: {human_wins/games:.2f} and bot wins: {bot_wins/games:.2f}")
print(f"Total Human Score: {human_total_score}, Total Bot Score: {bot_total_score} which gives us a ratio of {human_total_score/bot_total_score:.2f}")

# We write the results to a file, so we can analyse them later
with open(f"simulation{chosen}_results.txt", "w") as file:

    file.write(f"Number of Games: {games}\n")

    file.write(f"Human Distribution: {sim.human_distribution}\n")
    file.write(f"Bot Distribution: {sim.bot_distribution}\n")

    file.write(f"Total Human Score: {human_total_score}\n")
    file.write(f"Total Bot Score: {bot_total_score}\n")
    file.write(f"Human Wins: {human_wins} ({100*human_wins/games:.2f}%)\n")
    file.write(f"Bot Wins: {bot_wins} ({100*bot_wins/games:.2f}%)\n")
    file.write(f"Score Ratio (Human/Bot): {human_total_score/bot_total_score:.2f}\n")

    
