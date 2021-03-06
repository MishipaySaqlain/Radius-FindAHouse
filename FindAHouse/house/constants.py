class RelaxationType:
    PERCENTAGE = 'percentage'
    VALUE = 'VALUE'

MINIMUM_SCORE_FOR_MATCH = 40

DISTANCE_SCORE_CONTRIBUTION = 30
BUDGET_SCORE_CONTRIBUTION = 30
ROOM_SCORE_CONTRIBUTION = 20
BATH_SCORE_CONTRIBUTION = 20

NUM_ROOMS_RELAXATION = 2
BUDGET_RELAXATION_PERCENTAGE = 25
MAX_SEARCH_RADIUS = 16.093  # (10 miles in KM)
MAX_SCORE_DISTANCE = 3.2186 # (2 miles in KM)

assert (
    DISTANCE_SCORE_CONTRIBUTION + BUDGET_SCORE_CONTRIBUTION +
    ROOM_SCORE_CONTRIBUTION + BATH_SCORE_CONTRIBUTION
) == 100
