# Key Players:

**Human Users (H):**
- H1: Seek Authenticity
- H2: Engage with Flow

**Bot Operators (B):**
- B1: Mimic Humanity
- B2: Mass Produce

# Adjustable Parameters
- \#rounds
- payoff matrix: [H1 vs B1, H1 vs B2, H2 vs B1, H2 vs B2]
- human/bot distribution: probability of which strategy is taken (either H1/H2 for Humans, B1/B2 for Bots)

**Simulation 2: contains ability to report malicious behaviour, therefore additionaly contains the following parameters:**
- *report_threshold_b2*:  Number of reports after which B2 is blocked
- *report_threshold_b1*: Number of reports after which B1 is blocked (rare)
- *report_prob_b2*: Ease of Detection for H1 of B2 ($0<=r<=1$, the higher -> the easier to detect)
- *report_prob_b1*: Ease of Detection for H1 of B1 


