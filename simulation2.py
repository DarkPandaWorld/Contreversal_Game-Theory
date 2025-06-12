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

# New Rule: Humans can report Bots
report_threshold_b1 = 8      # B1 wird nach 8 Meldungen geblockt (seltener)
report_threshold_b2 = 3      # B2 wird nach 3 Meldungen geblockt
report_prob_b1 = 0.05        # H1 erkennt B1 fast nie
report_prob_b2 = 0.75        # H1 erkennt B2 relativ leicht

def simulate_game(games):
    # Bots initialized with reports and blocked status
    b1_bots = [{'id': f'B1_{i}', 'reports': 0, 'blocked': False} for i in range(10)]
    b2_bots = [{'id': f'B2_{i}', 'reports': 0, 'blocked': False} for i in range(10)]

    #Tracking blocked bots
    blocked_b1 = []
    blocked_b2 = []

    #Tracking scores
    human_scores = []
    bot_scores = []

    for _ in range(rounds):
        # Randomly pick strategies
        human = np.random.choice(['H1', 'H2'], p=[human_distribution['H1'], human_distribution['H2']])
        bot_type = np.random.choice(['B1', 'B2'], p=[bot_distribution['B1'], bot_distribution['B2']])
        
        # Select an active bot based on type
        if bot_type == 'B1':
            active_bots = [b for b in b1_bots if not b['blocked']] # Filter out blocked bots
            if not active_bots:                                    # If no active bots, skip this round
                continue
            bot = np.random.choice(active_bots)                     # Randomly select one of the active bots
            threshold = report_threshold_b1                         # Set threshold for reporting 
            report_prob = report_prob_b1                            # Set reporting probability 
            blocked_list = blocked_b1                               # List to track blocked B1 bots
        
        else:
            active_bots = [b for b in b2_bots if not b['blocked']]
            if not active_bots:
                continue
            bot = np.random.choice(active_bots)
            threshold = report_threshold_b2
            report_prob = report_prob_b2
            blocked_list = blocked_b2

        # Standard-Payoffs
        h_payoff, b_payoff = payoffs[(human, bot_type)]

        # Human H1 can report Bots [with a certain probability]
        if human == 'H1' and np.random.rand() < report_prob: 
            bot['reports'] += 1                                     # Increment the report count for the bot
            if bot['reports'] >= threshold:                         # Check if the bot has reached the reporting threshold  
                bot['blocked'] = True                               # Block the bot if threshold is reached    
                blocked_list.append(bot['id'])                      # Add the bot to the blocked list  

        human_scores.append(h_payoff)
        bot_scores.append(b_payoff)



    # Plot results
    # Displaying the settings used in the simulation
    settings_text = (
        f"H1/H2: {human_distribution['H1']*100:.0f}% / {human_distribution['H2']*100:.0f}%\n"
        f"B1/B2: {bot_distribution['B1']*100:.0f}% / {bot_distribution['B2']*100:.0f}%\n"
        f"Report Prob B1/B2: {report_prob_b1*100:.0f}% / {report_prob_b2*100:.0f}%\n"
        f"Blocking Threshold B1/B2: {report_threshold_b1} / {report_threshold_b2}"
    )
    # Adjusting the plot layout to include the settings text
    plt.subplots_adjust(bottom=0.2)
    plt.gcf().text(0.01, 0.01, settings_text, fontsize=9, verticalalignment='bottom')

    # Plotting the cumulative scores
    plt.plot(np.cumsum(human_scores), label='Human Payoff', color='red')
    plt.plot(np.cumsum(bot_scores), label='Bot Payoff', color='blue')

    # Adding labels and title to the plot
    plt.xlabel("Round")
    plt.ylabel("Cumulative Payoff")
    plt.title("Authenticity Signal Game – Simulation 2")
    plt.suptitle(f"Number of Game: {games}" , fontsize=10) 
    plt.legend()
    plt.grid(True)

    plt.savefig(f"Results_Sim2/sim2_{games}.png")

    # plt.show()    #shows the picture, which is not needed
    plt.clf()                                                     #deletes plot for next simulation

    #For data analysis, we can return the scores
    return sum(human_scores), sum(bot_scores)
