import random

from mylogging import logger
from myconfigparser import config
from generators import *
from constants import *
from decimal import *

getcontext().prec = 6

ITERATIONS = config[ITERATIONS].get(int)

ORDERS = []

if __name__ == '__main__':
    # RED ZONE
    for i in range(300):
        # Get possible statuses randomly by random_index
        random_index = generate_random_number(
            first_entry=config[STATUS][RED][FIRST_ENTRY].get(int),
            step=config[STATUS][RED][STEP].get(float),
            multiplier=config[STATUS][RED][MULTIPLIER].get(float),
            max_entry=len(config[STATUS][RED][VALUES].get()) - 1,
            iteration=i,
            round_result=True
        )
        POSSIBLE_STATUSES = config[STATUS][RED][VALUES].get()[random_index]
        ORDER_PARTIALLY_FILLED = False
        for status in POSSIBLE_STATUSES:
            order_id = format(generate_random_number(
                first_entry=config[ORDER_ID][FIRST_ENTRY].get(int),
                step=config[ORDER_ID][STEP].get(float),
                multiplier=config[ORDER_ID][MULTIPLIER].get(float),
                max_entry=config[ORDER_ID][MAX_ENTRY].get(int),
                iteration=i,
                round_result=True
            ), 'x')
            provider_id = generate_random_value_from_list(
                first_entry=config[PROVIDER_ID][FIRST_ENTRY].get(int),
                step=config[PROVIDER_ID][STEP].get(float),
                multiplier=config[PROVIDER_ID][MULTIPLIER].get(float),
                iteration=i,
                values=config[PROVIDER_ID][VALUES].get(),
            )
            direction = generate_random_value_from_list(
                first_entry=config[DIRECTION][FIRST_ENTRY].get(int),
                step=config[DIRECTION][STEP].get(float),
                multiplier=config[DIRECTION][MULTIPLIER].get(float),
                iteration=i,
                values=config[DIRECTION][VALUES].get(),
            )
            currency_pair = list(generate_random_value_from_list(
                first_entry=config[CURRENCY_PAIR][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR][STEP].get(float),
                multiplier=config[CURRENCY_PAIR][MULTIPLIER].get(float),
                values=config[CURRENCY_PAIR][VALUES].get(),
                iteration=i,
            ).items())[0]
            currency_pair_delta = generate_random_number(
                first_entry=config[CURRENCY_PAIR]['delta'][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR]['delta'][STEP].get(float),
                multiplier=config[CURRENCY_PAIR]['delta'][MULTIPLIER].get(float),
                max_entry=config[CURRENCY_PAIR]['delta'][MAX_ENTRY].get(float),
                iteration=i,
            )
            currency_pair_delta_partially_filled = generate_random_number(
                first_entry=config[CURRENCY_PAIR]['delta_partially_filled'][FIRST_ENTRY].get(int),
                step=config[CURRENCY_PAIR]['delta_partially_filled'][STEP].get(float),
                multiplier=config[CURRENCY_PAIR]['delta_partially_filled'][MULTIPLIER].get(float),
                max_entry=config[CURRENCY_PAIR]['delta_partially_filled'][MAX_ENTRY].get(float),
                iteration=i,
            )
            currency_pair_currency = currency_pair[0]
            if ORDER_PARTIALLY_FILLED is not True and status == 'Partially Filled':
                currency_pair_value = round(currency_pair[1] + currency_pair_delta_partially_filled, 6)
                ORDER_PARTIALLY_FILLED = True
            elif ORDER_PARTIALLY_FILLED is True:
                pass
            else:
                currency_pair_value = round(currency_pair[1] + currency_pair_delta, 6)

            ORDER = [i, order_id, provider_id, direction, status, currency_pair_currency, currency_pair_value]

            # Append generated ORDER list to ORDERS
            ORDERS.append(ORDER)
            logger.info(ORDER)

logger.info('Total orders generated: ' + str(len(ORDERS)))
