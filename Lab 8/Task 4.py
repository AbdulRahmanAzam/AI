import numpy as np

states = ["Sunny","Cloudy","Rainy"]

tr_mat = [[0.33,0.33,0.34],[0.34,0.33,0.33],[0.33,0.34,0.33]]


def simulate(initial_state,steps):
    cur_state = initial_state
    all_states = [cur_state]
    rainy_cnt =0;
    for i in range(steps):
        if cur_state == "Sunny":
            all_states.append(np.random.choice(states, p=tr_mat[1]))
        elif cur_state == "Cloudy":
            all_states.append(np.random.choice(states, p=tr_mat[2]))
        else:
            rainy_cnt +=1
            all_states.append(np.random.choice(states, p=tr_mat[0]))
        cur_state = all_states[-1]
    all_states.append(rainy_cnt)
    return (all_states)
initial_state = "Sunny"
res = simulate(initial_state,10)
rainy_cnt = res[-1]
res.pop()
print(f"10 Days Weather Prediction: {res}")
print(f"Probablity of rainy weather in next 10 days is {rainy_cnt/10}")
