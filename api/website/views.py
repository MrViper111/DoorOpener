import asyncio
import json
import os
import time
from datetime import datetime
import random
from crypt import methods
from flask import Blueprint, render_template, request, jsonify, redirect
from functools import update_wrapper, wraps

from control import Control


def verify_door_opened():
    return True

def verify_door_closed():
    return True


views = Blueprint("views", __name__)
is_opened = verify_door_opened()
last_updated = time.time()
API_TIMEOUT = 10


@views.route("/")
def home():
    return render_template("home.html")

@views.route("/api/open")
def open_door():
    global is_opened, last_updated
    start_time = time.time()
    Control.open()

    while not verify_door_opened():
        if time.time() - start_time >= API_TIMEOUT:
            return {"success": False}

    is_opened = True
    last_updated = time.time()
    return {"success": True}

@views.route("/api/close")
def close_door():
    global is_opened, last_updated
    start_time = time.time()
    Control.open()

    while not verify_door_closed():
        if time.time() - start_time >= API_TIMEOUT:
            return {"success": False}

    is_opened = False
    last_updated = time.time()
    return {"success": True}

@views.route("api/status")
def status():
    return {"api": True, "opened": is_opened, "position": 100, "power_supply": 30, "wifi_network": "staff-net", "last_updated": int(last_updated)}
