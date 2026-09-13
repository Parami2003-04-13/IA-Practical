class KnowledgeBase:
    def __init__(self):
        # Set to store unique string facts 
        self.facts = set()
        # List to store rules (Horn Clauses) : ( [premises], conclusion )
        self.rules = []

    def tell_fact(self, fact_string: str):
        """Add single fact to KB"""
        self.facts.add(fact_string)

    def tell_rule(self, premise_list: list, conclusion_string: str):
        """Add rule as a tuple into KB"""
        self.rules.append((premise_list, conclusion_string))

    def clear_facts(self):
        """Remove all facts from KB instead of rules."""
        self.facts.clear()

if __name__ == "__main__":
    kb = KnowledgeBase()
    
    # Add facts and rules
    kb.tell_fact("TargetVisible")
    kb.tell_rule(["TargetVisible", "InRange"], "CanAttack")
    
    print("Current Facts:", kb.facts)
    print("Current Rules:", kb.rules)
    
    # Remove facts
    kb.clear_facts()
    print("Facts after clearing:", kb.facts)