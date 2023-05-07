import threading
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from logger_class import getLog
from flask import Flask, render_template, request, jsonify, Response, url_for, redirect
from flask_cors import CORS, cross_origin
import pandas as pd
from mongoDBOperations import MongoDBManagement
from FlipkratScrapping import FlipkratScrapper
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


rows = {}
collection_name = None