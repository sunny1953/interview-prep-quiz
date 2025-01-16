from typing import List, Set

class UserProfile:
    def __init__(self):
        self.performance_history: List[dict] = []
        self.difficulty_level: str = 'medium'
        self.weak_areas: Set[str] = set()
        self.strong_areas: Set[str] = set()
        self.domain: str = None  # Interview preparation domain
        self.domain_specific_progress: dict = {}  # Track progress in specific topics within domain

    def update_performance(self, question, is_correct: bool):
        self.performance_history.append({
            'question': question,
            'correct': is_correct,
            'domain': self.domain,
            'topic': question.topic
        })
        
        # Update domain-specific progress
        if question.topic not in self.domain_specific_progress:
            self.domain_specific_progress[question.topic] = {
                'total': 0,
                'correct': 0
            }
        
        self.domain_specific_progress[question.topic]['total'] += 1
        if is_correct:
            self.domain_specific_progress[question.topic]['correct'] += 1
            
        # Update weak and strong areas
        topic_stats = self.domain_specific_progress[question.topic]
        success_rate = topic_stats['correct'] / topic_stats['total']
        
        if success_rate < 0.4:
            self.weak_areas.add(question.topic)
            self.strong_areas.discard(question.topic)
        elif success_rate > 0.8:
            self.strong_areas.add(question.topic)
            self.weak_areas.discard(question.topic)
