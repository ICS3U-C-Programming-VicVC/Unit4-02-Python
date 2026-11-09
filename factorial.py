#!/usr/bin/env python3
# Created By: Victor Victor-Calixte
# Date: 11/8/26
# This program calculates the factorial of the given number

import constants


def main():

    # Getting the factorial number from the user
    factorial_num_str = input(constants.INPT_MSG)

    # the try statement will make sure the code safely with invalid user inputs
    try:
        factorial_num = int(factorial_num_str)
        total_loops = abs(factorial_num)

        # Setting the needed variables
        crnt_loop = 0
        sum_num = 1

        # calculating the factorial
        while True:

            crnt_loop += 1

            sum_num *= crnt_loop

            if crnt_loop >= total_loops:
                break

        if factorial_num < 0:
            sum_num *= -1

        # Displaying the results to the user
        print(constants.FINAL_MSG.format(factorial_num, sum_num))

        # else:

    except:
        print(constants.ERR_MSG.format(factorial_num_str))


if __name__ == "__main__":
    main()
