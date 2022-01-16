
import GameData
import random

class Ruleset():

###############
## PLAY RULES
###############

    @staticmethod 
    def play_best_safe_card(agent, observation):
        ################
        #  Do we need to add some checks (?) don't think so
        ################
        card_pos = agent.card_play_manager.play_best_safe_card(observation)

        if card_pos is not None:
            print(">>>play best safe card: ", card_pos)
            return GameData.ClientPlayerPlayCardRequest(agent.name, card_pos)
        return None

    @staticmethod 
    def maybe_play_lowest_playable_card(agent, observation):
        ################
        #  Do we need to add some checks (?) don't think so
        ################
        card_pos = agent.card_play_manager.maybe_play_lowest_playable_card(observation)

        if card_pos is not None:
            print(">>>play lowest playable card: ", card_pos)
            return GameData.ClientPlayerPlayCardRequest(agent.name, card_pos)
        return None

###############
## HINT RULES
###############

    @staticmethod 
    def give_helpful_hint(agent, observation):
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.give_helpful_hint(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the helpful hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    @staticmethod 
    def get_low_value_hint(agent, observation):
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.get_low_value_hint(observation)
            assert (destination_name, value, type) != (None, None, None)
            print(">>>give the low_value hint ", type, " ", value, " to ", destination_name)
            return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    @staticmethod
    def tell_randomly(agent, observation):
        '''Tell to a random player a random information prioritizing color'''
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.tell_randomly(observation)
            assert (destination_name, value, type) != (None, None, None)
            print(">>>give the random hint ", type, " ", value, " to ", destination_name)
            return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    @staticmethod
    def tell_fives(agent, observation):
        '''Tell 5s to a random player if it has them'''
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.tell_fives(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the tell_five hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    @staticmethod
    def tell_ones(agent, observation):
        '''Tell 1s to a random player if it has them'''
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.tell_ones(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the tell_ones hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    # Prioritize color, just next player is considered
    @staticmethod
    def tell_unknown(agent, observation):
        '''Tell a random player an unknown information prioritizing color'''
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.tell_unknown(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the tell_unknow hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

    @staticmethod
    def tell_anyone_useless_card(agent, observation):
        pass

    @staticmethod
    def tell_most_information_to_next(agent, observation):
        '''Tell 1s to a random player if it has them'''
        if observation['usedNoteTokens'] < 8:
            destination_name, value, type = agent.card_hints_manager.tell_most_information_to_next(observation)
            if (destination_name, value, type) != (None, None, None):  # found a best hint
                print(">>>give the most information hint ", type, " ", value, " to ", destination_name)
                return GameData.ClientHintData(agent.name, destination_name, type, value)
        return None

###############
## DISCARD RULES
###############

    @staticmethod 
    def discard_useless_card(agent, observation):
        if observation['usedNoteTokens'] != 0:
            card_pos = agent.card_discard_manager.discard_useless_card(observation)
            if (card_pos is not None):
                print(">>>discard useless card:", card_pos)
                return GameData.ClientPlayerDiscardCardRequest(agent.name, card_pos)
        return None
    
    @staticmethod 
    def discard_less_relevant(agent, observation):
        if observation['usedNoteTokens'] != 0:
            card_pos = agent.card_discard_manager.discard_less_relevant(observation)
            if (card_pos is not None):
                print(">>>discard less relevant card:", card_pos)
                return GameData.ClientPlayerDiscardCardRequest(agent.name, card_pos)
        return None


    @staticmethod
    def discard_duplicate_card(agent, observation):
        '''
        Discard a card that I see in some other player's hand
        '''
        if observation['usedNoteTokens'] != 0:
            card_pos = agent.card_discard_manager.discard_duplicate_card(observation)
            if (card_pos is not None):
                print(">>>discard duplicate card:", card_pos)
                return GameData.ClientPlayerDiscardCardRequest(agent.name, card_pos)
        return None
    




