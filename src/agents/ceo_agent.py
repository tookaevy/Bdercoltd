class CEOAgent:
    def __init__(self, config, principles):
        self.config = config
        self.principles = principles

    def evaluate_request(self, confidence_score):
        if confidence_score >= self.config['threshold']:
            return "AUTO-APPROVED"
        return "ESCALATE TO HUMAN"
