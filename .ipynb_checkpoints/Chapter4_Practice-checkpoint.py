{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1d39684c-6896-4b98-ba13-be9a4b03566b",
   "metadata": {},
   "source": [
    "Kim Leach - 4.2 Defining Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0211d38e-7937-4a8b-a7e0-9b5a5e5e8501",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "49"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def square(number):\n",
    "    \"\"\"Calculate the quare of number.\"\"\"\n",
    "    return number ** 2\n",
    "\n",
    "square(7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7244e52f-cc61-4934-96eb-dd03800bf4b6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6.25"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square(2.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "df4c7d7a-7215-40f3-b0ec-502fc1cc8e4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The square of 7 is 49\n"
     ]
    }
   ],
   "source": [
    "print('The square of 7 is', square(7))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "c3bb57cd-aa3d-4781-bb3c-67fceb47238a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.5"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def square_root(number):\n",
    "    \"\"\"Calculate the square root of number\"\"\"\n",
    "    return number ** (1/2)\n",
    "\n",
    "square_root(6.25)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ea187a6-fa26-4983-b908-5e92e4f21603",
   "metadata": {},
   "source": [
    "4.3 Functions with Multiple Parameters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6232d3e6-4339-4e7a-89f8-4be061f2dc70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "36"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def maximum(value1, value2, value3):\n",
    "    \"\"\"Return the maximum of three values.\"\"\"\n",
    "    max_value = value1\n",
    "    if value2 > max_value:\n",
    "        max_value = value2\n",
    "    if value3 > max_value:\n",
    "        max_value = value3\n",
    "    return max_value\n",
    "\n",
    "maximum(12, 27, 36)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f569dfc4-037b-4d00-a8f6-fa7c270bca4e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "45.6"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maximum(12.3, 45.6, 9.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7eb99c60-c95d-4cd9-a68b-42c8b5ff7a14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'yellow'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maximum('yellow', 'red', 'orange')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b8d4f976-6c08-4f51-827d-bfb29324dcdc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13.5"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "maximum(13.5, -3, 7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d7184859-6393-47ce-a02b-7753999d7947",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'yellow'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max('yellow', 'red', 'orange', 'blue', 'green')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "69679b4a-71bb-440f-b797-e2d98ffd2fbe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min(15, 9, 27, 14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "52b4a627-8a77-4180-8e73-77b9db42c63d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "max([14,27,5,4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "633eade0-d5af-4b84-bc69-974209b71829",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'a'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "min('orange')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5a2e7c6f-9f77-4b35-a9c4-ae690127c47b",
   "metadata": {},
   "source": [
    "4.4 Random-Number Generation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3711743d-2096-4c53-8b7d-d12b7959b739",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0e5600da-97d2-417e-a62b-32771ed0bedf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 6 4 5 2 2 6 4 5 4 "
     ]
    }
   ],
   "source": [
    "for roll in range(10):\n",
    "    print(random.randrange(1,7), end=' ')\n",
    "    roll"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "3e398c14-be95-4530-8cac-e38e2b2f4642",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Face    Frequency\n",
      "   1      1000895\n",
      "   2      1000908\n",
      "   3       999743\n",
      "   4       998590\n",
      "   5       999424\n",
      "   6      1000440\n"
     ]
    }
   ],
   "source": [
    "# fig04_01.py\n",
    "\"\"\"Roll a six-sided die 6,000,000 times.\"\"\"\n",
    "import random\n",
    "\n",
    "# face frequency counters\n",
    "frequency1 = 0\n",
    "frequency2 = 0\n",
    "frequency3 = 0\n",
    "frequency4 = 0\n",
    "frequency5 = 0\n",
    "frequency6 = 0\n",
    "\n",
    "# 6,000,000 die rolls\n",
    "for roll in range(6_000_000): # note underscore separators\n",
    "    face = random.randrange(1, 7)\n",
    "    \n",
    "    #increment appropriate face counter\n",
    "    if face == 1:\n",
    "        frequency1+= 1\n",
    "    if face == 2:\n",
    "        frequency2+= 1\n",
    "    if face == 3:\n",
    "        frequency3+= 1\n",
    "    if face == 4:\n",
    "        frequency4+= 1\n",
    "    if face == 5:\n",
    "        frequency5+= 1\n",
    "    if face == 6:\n",
    "        frequency6+= 1\n",
    "        \n",
    "print(f'Face{\"Frequency\":>13}')\n",
    "print(f'{1:>4}{frequency1:>13}')\n",
    "print(f'{2:>4}{frequency2:>13}')\n",
    "print(f'{3:>4}{frequency3:>13}')\n",
    "print(f'{4:>4}{frequency4:>13}')\n",
    "print(f'{5:>4}{frequency5:>13}')\n",
    "print(f'{6:>4}{frequency6:>13}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "31cc63b4-0e91-47a6-b108-37d6d75a6332",
   "metadata": {},
   "outputs": [],
   "source": [
    "random.seed(32)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "22f0703a-8b1f-4936-921e-de31b23eba61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 2 3 6 2 4 1 6 1 "
     ]
    }
   ],
   "source": [
    "for roll in range(10):\n",
    "    print(random.randrange(1,7), end=' ')\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "94795259-ff88-4537-ab36-83acb62d52cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "H T T H T T H H H T H T H T H T H H H H "
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "for i in range(20):\n",
    "    print('H' if random.randrange(2) == 0 else 'T', end=' ')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a40eb58-8999-4952-b6f8-f12e217c1147",
   "metadata": {},
   "source": [
    "4.5 Case Study: A Game of Chance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "8826db46-8b52-46c4-a2c1-256e362a5e3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Player Rolled 3 + 6 = 9\n",
      "Point is 9\n",
      "Player Rolled 4 + 2 = 6\n",
      "Player Rolled 5 + 6 = 11\n",
      "Player Rolled 3 + 5 = 8\n",
      "Player Rolled 5 + 5 = 10\n",
      "Player Rolled 1 + 1 = 2\n",
      "Player Rolled 5 + 3 = 8\n",
      "Player Rolled 2 + 3 = 5\n",
      "Player Rolled 3 + 1 = 4\n",
      "Player Rolled 2 + 6 = 8\n",
      "Player Rolled 4 + 3 = 7\n",
      "Player Loses\n"
     ]
    }
   ],
   "source": [
    "# fig04_02.py\n",
    "\"\"\"Simulting the dice game Craps.\"\"\"\n",
    "import random\n",
    "\n",
    "def roll_dice():\n",
    "    \"\"\"Roll two dice and return their face values as a tuple.\"\"\"\n",
    "    die1 = random.randrange(1,7)\n",
    "    die2 = random.randrange(1,7)\n",
    "    return (die1, die2) # pack die face values into a tuple\n",
    "\n",
    "def display_dice(dice):\n",
    "    \"\"\"Display one roll of the two dice.\"\"\"\n",
    "    die1, die2 = dice # unpack the tuple into variables die1 and die2\n",
    "    print(f'Player Rolled {die1} + {die2} = {sum(dice)}')\n",
    "    \n",
    "die_values = roll_dice() # first roll\n",
    "display_dice(die_values)\n",
    "    \n",
    "# determine game status and point, based on first roll\n",
    "sum_of_dice = sum(die_values)\n",
    "               \n",
    "if sum_of_dice in (7, 11): # win\n",
    "    game_status = 'WON'\n",
    "elif sum_of_dice in (2, 3, 12): # lose\n",
    "    game_status = 'LOST'\n",
    "else: # remember point\n",
    "    game_status = 'Continue'\n",
    "    my_point = sum_of_dice\n",
    "    print('Point is', my_point)\n",
    "               \n",
    "#contiunue rolling until player wins or loses\n",
    "while game_status == 'Continue':\n",
    "    die_values = roll_dice()\n",
    "    display_dice(die_values)\n",
    "    sum_of_dice = sum(die_values)\n",
    "               \n",
    "    if sum_of_dice == my_point: # win by making point\n",
    "        game_status = 'WON'\n",
    "    elif sum_of_dice == 7: # lose by rolling 7\n",
    "        game_status = 'LOST'\n",
    "               \n",
    "# display \"Wins\" or \"loses\" message\n",
    "if game_status == 'WON':\n",
    "    print('Player Wins')\n",
    "else:\n",
    "    print('Player Loses')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2a43399e-8ded-4098-8085-a37e9b897e05",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Sue', [89, 94, 85])"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student = ('Sue', [89, 94, 85])\n",
    "student"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f51f8250-aa5f-426d-b31c-05eb38254a52",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sue: [89, 94, 85]\n"
     ]
    }
   ],
   "source": [
    "name, grades = student\n",
    "\n",
    "print(f'{name}: {grades}')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "884c28f2-0e2c-4d29-8932-f8794387bcf9",
   "metadata": {},
   "source": [
    "4.7 math Modlue Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "9fa9eb2a-4f92-483e-b953-5a4a9e9ce137",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f9e9592e-e3b3-4ecd-bf69-51186008e678",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30.0"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.sqrt(900)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "67a02c54-c149-46fd-b7ee-30439fb08a96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.fabs(-10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "8df2b4a4-481b-4570-b8c7-0957d7c30c73",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.pow(2,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "59209304-fc83-4607-953a-262a04711275",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "144.0"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.pow(12,2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ce6177cc-f9c9-4ea6-9665-00f0774bc457",
   "metadata": {},
   "source": [
    "4.8 Using IPython Tab Completion for Discovery"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "118f21c7-e630-4225-adb2-583104144efb",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0b01d414-c667-410a-9ccd-eefb62a1f2c5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\u001b[1;31mSignature:\u001b[0m \u001b[0mmath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfabs\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m/\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
       "\u001b[1;31mDocstring:\u001b[0m Return the absolute value of the float x.\n",
       "\u001b[1;31mType:\u001b[0m      builtin_function_or_method\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "math.fabs?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c744e45e-07ba-4d31-979a-ae987e95276d",
   "metadata": {},
   "source": [
    "4.9 Default Parameter Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "569de2f5-915b-4b27-93ed-d6e43a64a711",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rectangle_area(length=2, width=3):\n",
    "    \"\"\"Return a rectangle's area.\"\"\"\n",
    "    return length * width"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "83dd6667-c94a-417c-bc1b-92e250e111cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rectangle_area()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "c2dbc4c2-706c-498b-a53c-09442d322437",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rectangle_area(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "e996884a-6544-4c66-964b-0b87288c1ee2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rectangle_area(10,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0ce03bf9-b70f-4043-a3e6-6e30785fd6d2",
   "metadata": {},
   "source": [
    "4.10 Keyword Arguments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "4cef3a25-18c4-4474-93bb-4fed311678da",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rectange_area(length, width):\n",
    "    \"\"\"Return a rectangle's area\"\"\"\n",
    "    return length * width"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "f29718cc-c398-45ec-9197-1f854b574855",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rectange_area(width=5, length=10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4d442745-1444-467e-be59-de63b8fea762",
   "metadata": {},
   "source": [
    "4.11 Arbitrary Argument Lists"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "43726693-4d36-43b2-9a9f-39a8d6f49130",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.5"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def average(*args):\n",
    "    return sum(args)/ len(args)\n",
    "\n",
    "average(5,10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "3cb2d008-a7b4-484e-b2ab-ab26c9e05e1b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10.0"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "average(5, 10, 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "039a5578-e0b6-4402-a81f-34d470791875",
   "metadata": {},
   "outputs": [],
   "source": [
    "grades = [88, 75, 95, 55, 83]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "bc3406f9-a09a-4ca8-8b8c-a42dd1ab6cb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "79.2"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "average(*grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "0515b0d2-ffea-498f-bcd9-35b11f2dbb46",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_product(*args):\n",
    "    product = 1\n",
    "    for value in args:\n",
    "        product *= value\n",
    "    return product"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "8304f8df-360b-40ad-8c9a-9ca9445c0cdb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6000"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_product(10, 20, 30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "7ed277e9-e360-4863-a69e-c65f2564121c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_product(*range(1,6,2))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f0a70f5b-4146-497d-bce4-6bc7d8322198",
   "metadata": {},
   "source": [
    "4.12 Methods: Functions That Belong to Objects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "a45037a4-071a-4bf5-a8cb-1e9edf5108b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "s = 'Hello'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "84864b32-8480-4d05-a03d-784e425de754",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "6facc929-b1ba-4cc0-b1cf-99c9337e7741",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HELLO'"
      ]
     },
     "execution_count": 66,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "2927deba-13c9-4a74-a06d-1c6c34962636",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hello'"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d1fb0382-91ce-4cbc-bf49-17751488f8e9",
   "metadata": {},
   "source": [
    "4.15 Scope Rules"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "a451d752-5ed3-4ee6-9bcc-319dbcfac40b",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "4a942f24-99c5-46c1-9abd-66af07bd4330",
   "metadata": {},
   "outputs": [],
   "source": [
    "def access_global():\n",
    "    print('x printed from access_global:', x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "f9705286-b7a3-4a98-9ed4-bdcdd0690b23",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x printed from access_global: 7\n"
     ]
    }
   ],
   "source": [
    "access_global()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "4adcda49-5f18-487b-8ceb-998fab3d72ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def try_to_modify_global():\n",
    "    x=3.5\n",
    "    print('x printed from try_to_modify_global:', x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "0f5e1140-ed50-41e3-be25-5841b31d1518",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "x printed from try_to_modify_global: 3.5\n"
     ]
    }
   ],
   "source": [
    "try_to_modify_global()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "fa25aace-7c2a-463d-ba1d-c43f8bc144c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "2a72e659-924c-43c6-9a3b-64cfb4fc392c",
   "metadata": {},
   "outputs": [],
   "source": [
    "total = 10 + 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "id": "8b202ce7-963b-496b-b730-83f5749a1e3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "15"
      ]
     },
     "execution_count": 115,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "id": "d9328a8f-6390-4eb2-9ee7-d9b5d7ad97c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#sum(10,5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f635c94-3b91-4254-a9ba-ff38f8ec2b7c",
   "metadata": {},
   "source": [
    "4.14 import: A Deeper Look"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "58bb7e0f-6193-47ad-b4e3-c4ac0dee0bf6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import ceil, floor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "0157efac-f101-40b3-9c1b-75366793405c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ceil(10.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "bf3addde-5ed6-4694-84fc-58c7d82f61c7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "floor(10.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "3b3fc858-93fb-4aeb-847e-3588b00fc72e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statistics as stats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "1222b379-ce85-4ff0-bce7-92156a5ac500",
   "metadata": {},
   "outputs": [],
   "source": [
    "grades = [85, 93, 45, 87, 93]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "9825efc7-3a39-4701-95b5-4551318cd5c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "80.6"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stats.mean(grades)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "a03b344e-f9aa-4355-9893-28b8eeb8021b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "2eddd374-74f6-46c4-826b-5990a500c90e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import decimal as dec"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "19e5f076-21fa-4c65-a741-5f3a471de0e3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Decimal('6.25')"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "dec.Decimal('2.5') ** 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c0ceb557-9c06-4b38-b913-74bdf7cb8be1",
   "metadata": {},
   "source": [
    "4.15 Passing Arguments to Functions: A Deeper Look"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "ba9799ee-6c71-4bdb-aa7c-324a8fa4d356",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "9849136b-b7a9-4877-9a80-cc8849892fbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1893048609264"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "id(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "0bb08f74-4507-418b-8e8f-b28471bfca2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cube(number):\n",
    "    print('id(number):', id(number))\n",
    "    return number ** 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "a5a18ce2-31a7-4ddf-bed2-d02a2f426d78",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id(number): 1893048609264\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "343"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "id": "ad04cccb-61b2-4875-90ec-a8f617a62028",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cube(number):\n",
    "    print('number is x:', number is x)\n",
    "    return number **3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "id": "3806397f-6cc5-4b60-9203-341a330fa28f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number is x: True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "343"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "id": "6791f199-754b-4052-a838-73dde68f7b6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cube(number):\n",
    "    print('id(number) before modifying number:', id(number))\n",
    "    number **= 3\n",
    "    print('id(number) after modifying number:', id(number))\n",
    "    return number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "77120524-b8bc-404e-88c5-44418bf8fdeb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id(number) before modifying number: 1893048609264\n",
      "id(number) after modifying number: 1893184273104\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "343"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cube(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "id": "eb583598-0349-4bac-92dc-0c5e5d067a1b",
   "metadata": {},
   "outputs": [],
   "source": [
    "width = 15.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "ec21935b-0f35-45c3-aebc-5a88f742e272",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id: 1893184272880 value: 15.5\n"
     ]
    }
   ],
   "source": [
    "print('id:', id(width), 'value:', width)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "783ebb41-8f52-41f8-8c3d-610d33bad204",
   "metadata": {},
   "outputs": [],
   "source": [
    "width = width * 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "4313fc41-0744-4420-8a19-beecf98601bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id: 1893184272432 value: 46.5\n"
     ]
    }
   ],
   "source": [
    "print('id:', id(width), 'value:', width)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "874fdac9-08f2-4cb9-a90e-8f66bd40fe0b",
   "metadata": {},
   "source": [
    "4.16 Function-Call Stack"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2a1df7f-54a0-4803-8fca-a3f445d6b3c6",
   "metadata": {},
   "source": [
    "4.17 Functional-Style Programming"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "df8c3bfb-c60d-421e-bfb3-f794ce4287eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "values = [1, 2, 3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "id": "135a8344-c7df-48c6-94cd-23e68855dbe0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "values"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f38662c2-8ee4-40f4-b6b7-3d8e523ece0e",
   "metadata": {},
   "source": [
    "4.18 Intro to Data Science: Measures of Dispersion"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "id": "76bae2b9-ca5f-4f1f-bc1a-6e35e4b08876",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Variance\n",
    "import statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "id": "fcd64631-55a6-493b-b25d-762fb395467a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.25"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "a98322c0-6e1f-49fd-8912-addf9b6ca970",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.5"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#standard deviation\n",
    "statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "id": "7a2f54a7-b3d3-4103-b40d-813ebbf18843",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "210a78f4-32c0-41a5-a7b0-95a9b52a3fde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.5"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.sqrt(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "id": "6135ed6d-3c7a-4361-85c3-865f4216e5d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-4"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "math.floor (-3.14159)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f45d2b3-e56e-47f7-8276-fefec3abaef7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
