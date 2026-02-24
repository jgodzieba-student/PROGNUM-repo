{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73c0f981-0042-4b1f-95ee-c176cdf9f09d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1.8986e+27, 1.9891e+30, 3.3022e+23, 1.0243e+26, 5.9736e+24, 4.8685e+24, 5.6846e+26, 6.4185e+23, 8.681e+25}\n",
      "[4.8685e+24, 6.4185e+23, 3.3022e+23, 7.349e+22, 1.25e+22]\n",
      "1.1853119999999999e+24\n"
     ]
    }
   ],
   "source": [
    "#!/usr/bin/env python\n",
    "\n",
    "masses = [1.9891e+30, 1.8986e+27, \n",
    "          5.6846e+26, 1.0243e+26, 8.6810e+25,\n",
    "          5.9736e+24, 4.8685e+24, 6.4185e+23, \n",
    "          3.3022e+23, 7.349e+22, 1.25e+22]\n",
    "mass2 = []\n",
    "for m in masses:\n",
    "    if m <= 7.349e+22:\n",
    "        mass2.append(m)\n",
    "m1 = set(masses)\n",
    "m2 = set(mass2)\n",
    "new = m1 - m2\n",
    "print(new)\n",
    "\n",
    "sm = masses[6:]\n",
    "print(sm)\n",
    "\n",
    "average = sum(sm)/len(sm)\n",
    "print(average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b922956-4e13-4302-b33b-6cdc59b8bc39",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Anaconda3-2025.06",
   "language": "python",
   "name": "anaconda3-2025.06"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
