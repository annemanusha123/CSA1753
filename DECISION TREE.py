# Simple Decision Tree (Hardcoded logic - Exam friendly)

# Dataset: [Outlook, Humidity] -> Play
data = [
    ['Sunny','High','No'],
    ['Sunny','Normal','Yes'],
    ['Rain','High','Yes'],
    ['Rain','Normal','Yes'],
    ['Sunny','High','No']
]

def decision_tree(outlook, humidity):
    if outlook == 'Sunny':
        if humidity == 'High':
            return 'No'
        else:
            return 'Yes'
    elif outlook == 'Rain':
        return 'Yes'

# Test cases
print("Decision Tree Predictions:")
print("Sunny, High   ->", decision_tree('Sunny','High'))
print("Sunny, Normal ->", decision_tree('Sunny','Normal'))
print("Rain, High    ->", decision_tree('Rain','High'))
print("Rain, Normal  ->", decision_tree('Rain','Normal'))
