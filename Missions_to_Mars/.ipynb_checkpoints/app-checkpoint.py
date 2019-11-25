{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "import scrape_mars\n",
    "\n",
    "\n",
    "# Flask Setup\n",
    "app = Flask(__name__)\n",
    "\n",
    "# PyMongo Connection Setup\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)\n",
    "\n",
    "# Flask Routes\n",
    "# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars=mars)\n",
    "\n",
    "# Scrape Route to Import `scrape_mars.py` Script & Call `scrape` Function\n",
    "@app.route(\"/scrape\")\n",
    "def scrapper():\n",
    "    mars = mongo.db.mars\n",
    "    mars_data = scrape_mars.scrape_all()\n",
    "    mars.update({}, mars_data, upsert=True)\n",
    "    return \"Scraping Successful\"\n",
    "\n",
    "# Define Main Behavior\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
