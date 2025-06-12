import numpy as np
import matplotlib.pyplot as plt

#Human Users (H):
#   H1: Seek Authenticity
#   H2: Engage with Flow

#Bot Operators (B):
#   B1: Mimic Humanity
#   B2: Mass Produce

# Payoff-Matrix: [H1 vs B1, H1 vs B2, H2 vs B1, H2 vs B2]
payoffs = {
    ('H1', 'B1'): (20, 10),
    ('H1', 'B2'): (30, 0),
    ('H2', 'B1'): (0, 20),
    ('H2', 'B2'): (-20, 30)
}

# Number of rounds to simulate
rounds = 100

# Initial distribution (can be adjusted)
human_distribution = {'H1': 0.5, 'H2': 0.5}
bot_distribution = {'B1': 0.5, 'B2': 0.5}

def simulate_game(games):

    #Tracking scores
    human_scores = []
    bot_scores = []


    for _ in range(rounds):
        # Randomly pick strategies
        human = np.random.choice(['H1', 'H2'], p=[human_distribution['H1'], human_distribution['H2']])
        bot = np.random.choice(['B1', 'B2'], p=[bot_distribution['B1'], bot_distribution['B2']])
        
        # Get payoffs based on the chosen strategies
        h_payoff, b_payoff = payoffs[(human, bot)]

        # Update scores
        human_scores.append(h_payoff)
        bot_scores.append(b_payoff)

    # Plot results
    # Display the settings used in the simulation
    settings_text = (
        f"H1/H2: {human_distribution['H1']*100:.0f}% / {human_distribution['H2']*100:.0f}%\n"
        f"B1/B2: {bot_distribution['B1']*100:.0f}% / {bot_distribution['B2']*100:.0f}%\n"
    )

    # Adjusting the plot layout to include settings text
    plt.subplots_adjust(bottom=0.2)
    plt.gcf().text(0.01, 0.01, settings_text, fontsize=9, verticalalignment='bottom')

    # Plotting cumulative scores
    plt.plot(np.cumsum(human_scores), label='Human Payoff', color='red')
    plt.plot(np.cumsum(bot_scores), label='Bot Payoff', color='blue')

    # Adding labels and title to the plot
    plt.xlabel("Round")
    plt.ylabel("Cumulative Payoff")
    plt.title("Authenticity Signal Game – Simulation 1")          #Title displayed on the plot
    plt.suptitle(f"Number of Game: {games}" , fontsize=10)        #Subtitle displayed on the plot
    plt.legend()                                                  #adds legend to the plot
    plt.grid(True)                                                #adds grid to the plot


    plt.savefig(f"Results_Sim1/sim1_{games}.png")
    plt.clf()                                                     #deletes plot for next simulation

    # plt.show()                                                  #shows the picture, which is not needed

    #For data analysis, we can return the scores
    return sum(human_scores), sum(bot_scores)

# simulate_game(6)
