{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d0aefbde-2fc8-4bc8-a15e-2afc363a34c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The maximum value is 36\n",
      "The minimum value is 9\n",
      "My name is Kim Leach\n"
     ]
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
    "maximum(12, 27, 36)\n",
    "\n",
    "def minimum(value1, value2, value3, value4):\n",
    "    \"\"\"Return the minimum of four values.\"\"\"\n",
    "    min_value = value1\n",
    "    if value2 < min_value:\n",
    "        min_value = value2\n",
    "    if value3 < min_value:\n",
    "        min_value = value3\n",
    "    if value4 < min_value:\n",
    "        min_value = value4\n",
    "    return min_value\n",
    "\n",
    "minimum(15, 9, 27, 14)\n",
    "\n",
    "print(f'The maximum value is', maximum(12, 27, 36))\n",
    "print(f'The minimum value is', minimum(15, 9, 27, 14))\n",
    "print('My name is Kim Leach')"
   ]
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
