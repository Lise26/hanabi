from agentM import Agent
import GameData
import random

class Ruleset():

    @staticmethod 
    def get_best_play(agent: Agent, observation):
        ################
        #  Do we need to add some checks (?) don't think so
        ################
        card_pos = agent.get_best_play(observation)

        if card_pos is not None:
            print(">>>play the card number:", card_pos)
            return GameData.ClientPlayerPlayCardRequest(agent.name, card_pos)
        return None

    @staticmethod 
    def get_best_hint(agent: Agent, observation):
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.get_best_hint(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the helpful hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None
    
    @staticmethod 
    def get_low_value_hint(agent: Agent, observation):
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.get_low_value_hint(observation)
            print(">>>give the low_value hint ", type, " ", value, " to ", destination_name)
            return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    # Prioritize color, just next player is considered
    @staticmethod
    def tell_randomly(agent: Agent, observation):
        if observation['usedNoteTokens'] < 8:
            destination_name = agent.name
            while destination_name == agent.name:
                destination_name = agent.players_names[random.randint(0, len(observation['players'])-1)]
            for player_info in observation['players']:
                if player_info.name == destination_name:
                    destination_hand = player_info.hand
            
            card = random.choice([card for card in destination_hand if card is not None])
            if random.randint(0, 1) == 0:
                type = "color"
                value = card.color
            else:
                type = "value"
                value = card.value
            return GameData.ClientHintData(agent.name, destination_name, type, value)
        
        return None

    @staticmethod
    def tell_fives(agent: Agent, observation):
        '''Tell 5s to a random player if it has them'''
        if observation['usedNoteTokens'] < 8:
            destination_name = agent.name
            while destination_name == agent.name:
                destination_name = agent.players_names[random.randint(0, len(observation['players'])-1)]

            for player_info in observation['players']:
                if player_info.name == destination_name:
                    destination_hand = player_info.hand
            for card in destination_hand:
                if card.value == 5:
                    return GameData.ClientHintData(agent.name, destination_name, "value", card.value)
        return None

    @staticmethod
    def tell_ones(agent: Agent, observation):
        '''Tell 1s to a random player if it has them'''
        if observation['usedNoteTokens'] < 8:
            destination_name = agent.name
            while destination_name == agent.name:
                destination_name = agent.players_names[random.randint(0, len(observation['players'])-1)]

            for player_info in observation['players']:
                if player_info.name == destination_name:
                    destination_hand = player_info.hand
            for card in destination_hand:
                if card.value == 1:
                    return GameData.ClientHintData(agent.name, destination_name, "value", card.value)
        return None

    @staticmethod 
    def get_best_discard(agent: Agent, observation):
        if observation['usedNoteTokens'] != 0:
            card_pos, _, _ = agent.get_best_discard(observation)
            print(">>>discard the card number:", card_pos)
            return GameData.ClientPlayerDiscardCardRequest(agent.name, card_pos)
        return None

#############################
# From this point ahead must be expanded
#############################

    # Prioritize color, just next player is considered
    @staticmethod
    def tell_unknown(agent: Agent, observation):
        pass

    @staticmethod
    def tell_anyone_useless_card(agent: Agent, observation):
        pass

    @staticmethod
    def tell_most_information(agent: Agent, observation):
        pass
        

