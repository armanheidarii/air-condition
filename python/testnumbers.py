from ac import *

if __name__ == "__main__":

    # test ac_simulation
    ac_agent = SimpleACReflexAgent(min_threshold=0, max_threshold=100)
    ac_env = SimpleACEnvironment(ac_agent, starting_temp=50)

    print("AC simulation #1 starting conditions:")
    print(f"min-max thresholds: {ac_agent.min_threshold}, {ac_agent.max_threshold}")
    print(
        f"env temperature: {ac_env.temperature}, num_agent_actions: {ac_env.num_agent_actions}, is_ac_on: {ac_env.is_ac_on}"
    )

    print("-----simulating for 60 timesteps-----")
    # expecting temperature: 90, num_agent_actions: 1, is_ac_on: True
    ac_env.simulate(60)
    print(
        f"env temperature: {ac_env.temperature}, num_agent_actions: {ac_env.num_agent_actions}, is_ac_on: {ac_env.is_ac_on}"
    )
    print("______________________")

    ac_agent = SimpleACReflexAgent(min_threshold=15, max_threshold=25)
    ac_env = SimpleACEnvironment(ac_agent, starting_temp=20)
    print("AC simulation #2 starting conditions:")
    print(f"min-max thresholds: {ac_agent.min_threshold}, {ac_agent.max_threshold}")
    print(
        f"env temperature: {ac_env.temperature}, num_agent_actions: {ac_env.num_agent_actions}, is_ac_on: {ac_env.is_ac_on}"
    )

    print("-----simulating for 48 timesteps-----")
    # expecting temperature: 18, num_agent_actions: 5, is_ac_on: True
    ac_env.simulate(48)
    print(
        f"env temperature: {ac_env.temperature}, num_agent_actions: {ac_env.num_agent_actions}, is_ac_on: {ac_env.is_ac_on}"
    )
    print("_______________________________________________________________________")
