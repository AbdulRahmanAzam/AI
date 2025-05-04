
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# 1 define structure
model = DiscreteBayesianNetwork([
    ('intelligence','grade'),
    ('studyhours','grade'),
    ('difficulty','grade'),
    ('grade','pass')
])
# 2 define cpds
cpd_intelligence = TabularCPD(
    variable='intelligence',
    variable_card=2,
    values=[[0.7],[0.3]],
    state_names={'intelligence':['high','low']}
)
cpd_studyhours = TabularCPD(
    variable='studyhours',
    variable_card=2,
    values=[[0.6],[0.4]],
    state_names={'studyhours':['sufficient','insufficient']}
)
cpd_difficulty = TabularCPD(
    variable='difficulty',
    variable_card=2,
    values=[[0.4],[0.6]],
    state_names={'difficulty':['hard','easy']}
)
cpd_grade = TabularCPD(
    variable='grade',
    variable_card=3,
    values=[
        [0.3, 0.3, 0.3, 0.3, 0.4, 0.4, 0.4, 0.4],  # Grade A probabilities for different combinations
        [0.4, 0.4, 0.4, 0.4, 0.5, 0.5, 0.5, 0.5],  # Grade B probabilities for different combinations
        [0.3, 0.3, 0.3, 0.3, 0.1, 0.1, 0.1, 0.1]   # Grade C probabilities for different combinations
    ],
    evidence=['intelligence', 'studyhours', 'difficulty'],
    evidence_card=[2, 2, 2],
    state_names={'grade':['A','B','C'], 
                 'intelligence':['high','low'],
                 'studyhours':['sufficient','insufficient'],
                 'difficulty':['hard','easy']}
)
cpd_pass = TabularCPD(
    variable='pass',
    variable_card=2,
    values=[
        [0.95, 0.8, 0.5],
        [0.05, 0.2, 0.5]
    ],
    evidence=['grade'],
    evidence_card=[3],
    state_names={'pass':['yes','no'], 'grade':['A','B','C']}
)
# 3 add cpd to model
model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)
# 4 verify the model
assert model.check_model()

# 5 perform inference
inference = VariableElimination(model)

# 6 query
result = inference.query(variables=['pass'], evidence={'intelligence':'high', 'studyhours':'sufficient', 'difficulty':'easy'})
print(result)
