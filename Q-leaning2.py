import gymnasium as gym
import numpy as np

mapSize = 4
render_type = 1

if render_type == 0:
    render_type = 'human'
else:
    render_type = 'ansi'

def run():
    env = gym.make('FrozenLake-v1',map_name=f'{mapSize}x{mapSize}',is_slippery=False, render_mode=f'{render_type}')

    numActions = env.action_space.n # 4 ações possíveis
    numStates = env.observation_space.n # 16 estados possíveis (4x4), 64 estados possíveis (8x8)
    qTable = np.zeros((numStates, numActions))


    # CONFIGURAÇÕES DO TREINAMENTO
    episodes = 500 # número de episódios

    alpha = 0.3 # taxa de aprendizado
    gamma = 0.9 # fator de desconto

    epsilon = 1 # taxa de exploração
    epsilon_decay = 0.0001 # decaimento da taxa de exploração
    random_factor = np.random.default_rng() # fator de aleatoriedade

    for currentEpisode in range(episodes):
        state = env.reset()[0] 
        terminated = False # Se está em um estado terminal (tesouro ou buraco)
        truncated = False   # Se o episódio foi interrompido por limite de passos

        while not terminated and not truncated:
            if random_factor.random() < epsilon:
                action = env.action_space.sample() # ações 0 = esquerda, 1 = baixo, 2 = direita, 3 = cima
            else:
                action = np.argmax(qTable[state,:])

            
            new_state, reward, terminated, truncated, info = env.step(action)

            #if (terminated or truncated) and reward == 0 :
            #    reward = -1
            #elif (terminated or truncated) and reward == 1:
            #    reward = 10
            


            # Atualiza a tabela Q
            qTable[state, action] = ((1-alpha) * qTable[state, action]) + alpha * (reward + (gamma * np.max(qTable[new_state,:])))
            #qTable[state, action] + alpha * (reward + gamma * np.max(qTable[new_state,:]))# - qTable[state, action])

            state = new_state
    
            epsilon = max(epsilon - epsilon_decay, 0)

            if(epsilon==0):
                alpha = 0.0001
        #env.close()


    print(qTable)   
run()