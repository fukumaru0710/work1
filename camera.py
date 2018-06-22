{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "\n",
    "while(True):\n",
    "\n",
    "    # Capture frame-by-frame\n",
    "    ret, frame = cap.read()\n",
    "\n",
    "    # Display the resulting frame\n",
    "    cv2.imshow('frame', frame)\n",
    "    if cv2.waitKey(1) == 27:\n",
    "        break\n",
    "\n",
    "# When everything done, release the capture\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
# second
