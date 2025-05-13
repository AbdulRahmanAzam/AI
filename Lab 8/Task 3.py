from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
model = DiscreteBayesianNetwork(
    [
        ("Disease","Fever"),("Disease","Cough"),("Disease","Fatigue"),
        ("Disease","Chills")
    ]
)
 
#independnet Probablities

cpd_dis = TabularCPD("Disease",2,[[0.3],[0.7]],state_names={"Disease" : ["Flu","Cold"] })
#dependent probablities

cpd_fev = TabularCPD(
    "Fever",2,
    [[0.9,0.5],[0.1,0.5]],
    evidence = ["Disease"],
    evidence_card= [2],
    state_names={
        "Fever": ["Yes","No"],
        "Disease": ["Flu","Cold"]
    }
)

cpd_cou = TabularCPD(
    "Cough",2,
    [[0.8,0.6],[0.2,0.4]],
    evidence = ["Disease"],
    evidence_card= [2],
    state_names={
        "Cough": ["Yes","No"],
        "Disease": ["Flu","Cold"]
    }
)
cpd_fat = TabularCPD(
    "Fatigue",2,
    [[0.7,0.3],[0.3,0.7]],
    evidence = ["Disease"],
    evidence_card= [2],
    state_names={
        "Fatigue": ["Yes","No"],
        "Disease": ["Flu","Cold"]
    }
)
cpd_chil = TabularCPD(
    "Chills",2,
    [[0.6,0.4],[0.4,0.6]],
    evidence = ["Disease"],
    evidence_card= [2],
    state_names={
        "Chills": ["Yes","No"],
        "Disease": ["Flu","Cold"]
    }
)
model.add_cpds(cpd_dis,cpd_fev,cpd_cou,cpd_fat,cpd_chil)
model.check_model()

inference = VariableElimination(model)
#t1
t1 = inference.query(variables=["Disease"],evidence={"Fever":"Yes","Cough":"Yes"})
print("T1:\n",t1)
t2 = inference.query(variables=["Disease"],evidence={"Fever":"Yes","Cough":"Yes","Chills":"Yes"})
print("T2:\n",t2)
t3 = inference.query(variables=["Fatigue"],evidence={"Disease":"Flu"})
print("T3:\n",t3)
