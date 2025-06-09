import numpy as np
import matplotlib.pyplot as plt
# import pandas as pd

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

rounds = 100
human_scores = []
bot_scores = []

# Initial distribution (can be adjusted)
human_distribution = {'H1': 0.5, 'H2': 0.5}
bot_distribution = {'B1': 0.5, 'B2': 0.5}

# Neue Regel: Mensch kann Bot B2 melden
report_threshold_b2 = 3      # B2 wird nach 3 Meldungen geblockt
report_threshold_b1 = 8      # B1 wird nach 8 Meldungen geblockt (seltener)
report_prob_b2 = 0.25        # H1 erkennt B2 relativ leicht
report_prob_b1 = 0.05        # H1 erkennt B1 fast nie

# --- Bot-Populationen ---
b1_bots = [{'id': f'B1_{i}', 'reports': 0, 'blocked': False} for i in range(10)]
b2_bots = [{'id': f'B2_{i}', 'reports': 0, 'blocked': False} for i in range(10)]

#Tracking blocked bots
blocked_b1 = []
blocked_b2 = []

for _ in range(rounds):
    # Randomly pick strategies
    human = np.random.choice(['H1', 'H2'], p=[human_distribution['H1'], human_distribution['H2']])
    bot_type = np.random.choice(['B1', 'B2'], p=[bot_distribution['B1'], bot_distribution['B2']])
    
    # Wähle aktiven Bot
    if bot_type == 'B1':
        active_bots = [b for b in b1_bots if not b['blocked']]
        if not active_bots:
            continue
        bot = np.random.choice(active_bots)
        threshold = report_threshold_b1
        report_prob = report_prob_b1
        blocked_list = blocked_b1
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

    # Meldung durch H1 möglich
    if human == 'H1' and np.random.rand() < report_prob:
        bot['reports'] += 1
        if bot['reports'] >= threshold:
            bot['blocked'] = True
            blocked_list.append(bot['id'])

    human_scores.append(h_payoff)
    bot_scores.append(b_payoff)



# Plot results
plt.plot(np.cumsum(human_scores), label='Human Payoff', color='red')
plt.plot(np.cumsum(bot_scores), label='Bot Payoff', color='blue')
plt.xlabel("Round")
plt.ylabel("Cumulative Payoff")
plt.title("Authenticity Signal Game – Simulation 2")
plt.legend()
plt.grid(True)
plt.savefig("simulation2_ergebnis.png")

plt.show()
