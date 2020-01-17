import gym
import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--display', action='store_true')
    parser.add_argument('game', nargs="?", default="FrozenLake8x8-v0")
    args = parser.parse_args()

    env = gym.make(args.game)
    num_episodes = 1
    num_maxstep = 100

    agent_id = 1
    if agent_id == 1:
        agent = RandomAgent(env.action_space)
    elif agent_id == 2:
        agent = BiasedAgent(env.action_space)

    reward = 0
    done = False

    for i_episode in range(num_episodes):
        observation = env.reset()
        for t in range(num_maxstep):
            env.render()
            action = agent.act(observation, reward, done)
            observation, reward, done, info = env.step(action)
            print('episode {}-step {}, taking action {}, observation {}'.format(i_episode, t, action, observation))
            time.sleep(0.01)
            #if done:
            #    print("Episode finished after {} timesteps".format(t+1))
            #    break
        env.close()





class RandomAgent(object):
    # Each step take a random action from the action space
    def __init__(self, action_space):
        self.action_space = action_space
    def act(self, observation, reward, done):
        return self.action_space.sample()


class BiasedAgent(object):
    # Always take same action
    def __init__(self, action_space):
        self.action_space = action_space
        self.action_always = self.action_space.sample()
    def act(self, observation, reward, done):
        return self.action_always



if __name__ == '__main__':
    main()
