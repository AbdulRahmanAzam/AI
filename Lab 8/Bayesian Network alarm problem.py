from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1. Bayesian Network
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm'),
    ('Alarm', 'JohnCalls'),
    ('Alarm', 'MaryCalls')
])

# 2. Define CPDS
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2, values=[
    [0.999, 0.71, 0.06, 0.05], # False
    [0.001, 0.29, 0.94, 0.95] # True
], evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])
cpd_john = TabularCPD(variable='JohnCalls', variable_card=2, values=[
    [0.3, 0.9], # False
    [0.7, 0.1] # True
], evidence=['Alarm'], evidence_card=[2])
cpd_mary = TabularCPD(variable='MaryCalls', variable_card=2, values=[
    [0.2, 0.99], # False
    [0.8, 0.01] # True
], evidence=['Alarm'], evidence_card=[2])

# 3. Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)

# 4. Check if the model is valid
assert model.check_model()

# 5. Inference
inference = VariableElimination(model)

# 6. Query: What is the probability of a burglary given that John and Mary both call?
query = inference.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1})
print(query)

# 6. Query: What is the probability of an earthquake given that the alarm sounds?
query = inference.query(variables=['Earthquake'], evidence={'Alarm': 1})
print(query)


