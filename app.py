# A very simple Flask Hello World app for you to get started with...

from datetime import datetime
from flask import Flask, jsonify, render_template, make_response
import requests
from collections import Counter
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

especiales = [	"S34a Pascala", "S35a Chocolate Chimes", "S36a Rabbit Radio", "S24a Scary Mary", "S25a Drop Dead Drums", "S26a No Face Bass", "S27a Christmas Choir",
				"S28a Happy Lappy", "S29a Ding Dong Mic", "S31a Juliet", "S32a Valentines Violin", "S33a Rose Acoustic", "2nd Birthday Cake", "S41a Abs", "S42a The Scratcher",
				"S43a Pro DJ Mixer"
			]


card_types = {
    "people": [
        {
            "name": "1",
            "supply": "9999999",
            "issued": "0",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "5",
            "supply": "200",
            "issued": "200 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "6",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "7",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "8",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "9 Dodgy Manager",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "10 Brit Popster",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "11 Record Producer",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "12 The Ego",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "13 Buster",
            "supply": "35917",
            "issued": "35917 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "14 MC Trapper",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "15 Limey",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "16 Dorris",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "17 Moon Child",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "18 Curtis",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "19 Mr Dependable",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "20 Rob",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "21 Eric",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "22 Arthur",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "23 Jonny",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "24 Slippy",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "25 Dalilah",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "26 Thomas",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "27 Melissa",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "28 Nathan",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "29 Markie",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "30 Jake",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "31 Wayne",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "32 Leaf",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "33 Joel",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "34 Drew",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "35 Keely",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "36 Craig",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "37 Dennis",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "38 Stacey",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "39 Oliver",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "40 Rosanne",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "41 Jerome",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "42 Brodie",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "43 Riley",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "44 Daphne",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "45 Dizz",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "46 Heather",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "47 Dave",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "48 Jack",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "49 Gabe",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "50 Belle",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "51 Jason",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "52 Trisha",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "53 Colin",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "54 Charlie",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "55 Molly",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "56 Sasha",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "57 Richard",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "58 Millie",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "59 Wez",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "60 Jarred",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "61 Bo",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "62 Angie",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "63 Clinton",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "64 Tiana",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "65 Firefly",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "66 Stewie",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "67 Michelle",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "68 Faye",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "69 Claudio",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "70 Trudy",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "71 Tommy",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "72 Tony",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "73 Jeniffer",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "74 Alex",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "75 Nile",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "76 Elise",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "77 Tez",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "78 Dean",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "79 Tilly",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "80 Harry",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "81 Pierre",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "82 Sally",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "83 Nick",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "84 Nina",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "85 Kelly",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "86 Tim",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "87 Donna",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "88 MC Geezer",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "89 Alfie",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "90 Hugh",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "91 Colette",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "92 Susie",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "93 Priya",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "94 Kirk",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "95 Raj",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "96 Sarah",
            "supply": "25000",
            "issued": "6875",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "97 Leyla",
            "supply": "25000",
            "issued": "6573",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "98 Tazz",
            "supply": "25000",
            "issued": "10799",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "99 Brandon",
            "supply": "25000",
            "issued": "7536",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "100 Candy",
            "supply": "25000",
            "issued": "6711",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "f1",
            "supply": "17",
            "issued": "17 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "f2",
            "supply": "14",
            "issued": "14 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "f3",
            "supply": "26",
            "issued": "26 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "f4",
            "supply": "21",
            "issued": "21 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "R1",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R2",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R3 Mod",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R4 Female Rapper",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R5 Male Rapper",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R8 Lead Guitarist",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R9 The Songwriter",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R17 Winston",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R18 Toadie",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R21 MC Pressure",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R22 Derek",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R23 Daisy",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R27 Frankie",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R28 Lolita",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R29 Antonio",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R32 Rose Petal",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R34 Ed",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R37 Bolly Wood",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R38 Kimberly",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R39 Clive",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R41 Storm",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R42 Kris",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R47 Griff",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R48 Jessie",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R49 Bethany",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R50 Ali",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R51 Brad",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R54 Ellie",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R55 Bruce",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R56 Robbie",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R59 Laney",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R61 Vimbo",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R63 Sonny",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R66 Matt",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R67 Febie",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R68 Penny",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R69 Lucy",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R70 Jamie",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R71 Bekky",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R75 Greg",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R76 George",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R77 Rezz",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R79 Katie",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R80 Ian",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R84 Shine",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R85 Carly",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R86 Emma",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R87 Stacy",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R89 Mouse",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R93 Will",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R94 Stig",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R95 Barney",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R96 MC Bruv",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R100 Pixie",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R101 Remy",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R102 Butch",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R103 Sam",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R104 Macy",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R105 Tracy",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R106 Lewis",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R107 Alicia",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R108 Ray",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R109 Trevor",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R110 Jedd",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R111 DJ Chad",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R119 Janine",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R120 Dan",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R121 Benson",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R122 Jeeves",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R123 Carlito",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R124 Garlic",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R125 Rentaw",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R126 Sarge",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R127 Zapf",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R128 Luthien",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R129 Drabs",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R130 Groovy",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R131 Star Child",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R132 Hetty",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R133 James",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R134 Rachael",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R135 Rosetta",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R136 Desmond",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R137 Silent X",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R138 GameBoy Ali",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R139 Bladesong",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R144 Papa The Rapper",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R145 Chaney The Rapper",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R147 Leon",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R148 Phillipa",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R149 Frederico",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R150 Boki",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R151 Mr and Mrs Wolf",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R154 Sharman",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R155 Terrance",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R156 Flash",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R157 Samantha",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R158 Goose",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R159 Stomper",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R160 Melody",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R161 Vicky",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R162 Damien",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R166 Romy",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R167 Diana",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R168 Cliff",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R169 Green",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R170 Kev",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R171 Teddy",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R179 Tiki The Rapper",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R180 Avril",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R181 Brave The Rapper",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R182 Ben",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R183 Gustaf",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R184 Pascal",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R185 Barber Shop Quartet",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R186 Ivan",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R187 Chloe",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R188 Nytehawker",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R189 Roman",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R191 Sneakry",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R194 Encryptid",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R198 Dominic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R199 Harriet",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R201 Maisy",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R203 Sandy",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R204 Abi",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R205 Andy",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R206 Rick",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R207 Jesmel",
            "supply": "8000",
            "issued": "5072",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R208 Emily",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R209 Robot Drummer",
            "supply": "8000",
            "issued": "5339",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R210 Giuseppe",
            "supply": "8000",
            "issued": "5397",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R211 Giovanna",
            "supply": "8000",
            "issued": "6073",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R215 David",
            "supply": "8000",
            "issued": "7005",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R216 Gregory",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R217 Anita",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R218 MC Attitude Rapper",
            "supply": "10000",
            "issued": "2387",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R219 DJ Gumbo",
            "supply": "10000",
            "issued": "2295",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R220 Betty",
            "supply": "10000",
            "issued": "2202",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R222 Rod",
            "supply": "10000",
            "issued": "2336",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "E4 Modern Female Punk",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E5 Headbanging Singer",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E8 Pop Diva",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E9 Debbie",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E10 Pete Wrong",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E14 Bobby Remedy",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E16 Rozzer",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E18 Ashby",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E22 Kayleigh",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E23 Sky",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E24 Flame",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E29 Stanley",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E32 Bizzo",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E33 Grace",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E37 Slither",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E38 Rosie",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E41 MC Spud",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E43 Ziggy",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E44 Amy",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E45 Jackson",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E46 Rush",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E51 Gordie",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E57 Dorrego",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E58 Hamish",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E63 Kinsey",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E64 Valerie",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E65 The Crow",
            "supply": "400",
            "issued": "400 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E72 Tucker",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E73 Gary",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E74 Kitty",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E75 Natalie",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E80 MC Vision",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E81 Spider",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E85 Ceheran",
            "supply": "500",
            "issued": "482",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E86 Austin",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E98 Corey",
            "supply": "750",
            "issued": "199",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E99 Olivia",
            "supply": "750",
            "issued": "192",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "L1",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L2",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L7 John",
            "supply": "75",
            "issued": "75 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L8 Black Eye Butterfly",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L9 Steevc",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L10 Skyline Tigers",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L12 Gribbles",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L14 Billy Korg",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L15 Andrew Music",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L17 Stick Up Boys",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L18 winkandwoo",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L20 Ugochill",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L23 Foxon",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L24 Wagginston",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L25 NewenX",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L27 Jux",
            "supply": "100",
            "issued": "41",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L32 The Turtle Project",
            "supply": "100",
            "issued": "83",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L35 Svart Varg",
            "supply": "100",
            "issued": "15",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "FA1 Supportive Friend",
            "supply": "999999",
            "issued": "6654",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FA2 Casual Fan",
            "supply": "999999",
            "issued": "696",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FA3 Super Fan",
            "supply": "999999",
            "issued": "71",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FA4 Mega Fan",
            "supply": "999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S1 Undead Fred",
            "supply": "577",
            "issued": "577 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S5 Mozart",
            "supply": "1000",
            "issued": "1000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S6 Wizzy",
            "supply": "416",
            "issued": "416 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S9 Beethoven",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S10 Tchaikovsky",
            "supply": "500",
            "issued": "61 <font color=white>Only available on market. Price increases by 0.5 for each one.</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S11 Bach",
            "supply": "500",
            "issued": "92 <font color=white>Only available on market. Price increases by 1000 for each one.</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S12 Brahms",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S13 Chopin",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S14 Romeo",
            "supply": "370",
            "issued": "370 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S17 Jive Bunny",
            "supply": "450",
            "issued": "450 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S20 Father Earth",
            "supply": "397",
            "issued": "397 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S24 Scary Mary",
            "supply": "1338",
            "issued": "1338 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S24a Scary Mary",
            "supply": "133",
            "issued": "133 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S27 Christmas Choir",
            "supply": "994",
            "issued": "994 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S27a Christmas Choir",
            "supply": "99",
            "issued": "99 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S30 Juan Up",
            "supply": "2500",
            "issued": "251",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S31 Juliet",
            "supply": "1308",
            "issued": "1308 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S31a Juliet",
            "supply": "130",
            "issued": "130 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S34 Pascala",
            "supply": "999999",
            "issued": "3019&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>1080</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S34a Pascala",
            "supply": "999999",
            "issued": "108",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S37 Vivaldi",
            "supply": "500",
            "issued": "155 <font color=white>Only available in 24 packs bought with HIVE.</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S38 Video Vic",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S39 Handel",
            "supply": "500",
            "issued": "42 <font color=white>Only available in 12 packs bought with HIVE.</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S40 Douglas",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S41 Abs",
            "supply": "999999",
            "issued": "6549",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S41a Abs",
            "supply": "999999",
            "issued": "208",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB1 Dougie",
            "supply": "999999",
            "issued": "136",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB2 JoJo",
            "supply": "999999",
            "issued": "118",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB3 Gizmo",
            "supply": "999999",
            "issued": "93",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB4 Stephie",
            "supply": "999999",
            "issued": "83",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB5 The Risers",
            "supply": "141",
            "issued": "65&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>53</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FTB6 The Risen",
            "supply": "298",
            "issued": "52",
            "description": "",
            "rarity": "specials"
        }
    ],
    "instruments": [
        {
            "name": "i1 Cheap Guitar",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i2 Cheap Drum Kit",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i3 Cheap Keyboard",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i4 Cheap Bass",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i5 Cheap Mic",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i6 Mid Range Acoustic",
            "supply": "9999999",
            "issued": "40518",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i7 Mid Range Keys",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i8 Mid Range Mic",
            "supply": "9999999",
            "issued": "22564",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i9 Cheap Decks",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i10 Mid Range Bass",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i11 Mid Range Drums",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i12 RS-303 Bass Line",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i13 Cheap Violin",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i14 Cheap Sax",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i15 Cheap Trumpet",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i16 Cheap Cello",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i17 Didgeridoo",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i18 Electric Drums",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i19 Banjo",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i20 French Horn",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i21 Cajon",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i22 Castanets",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i23 Bargain Beater",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i24 Des Appalling",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i25 Cheap Trombone",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i26 Rickencrapper",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i27 Cheap Keyboard V2",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i28 Rusty Trumpet",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i29 Cheap Sax V2",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i30 Cheap Mic V2",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i31 Cheap Decks V2",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i32 Mid Range Guitar",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i33 Drum Machine",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i34 Cheap Kettle Drum",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i35 Kithara",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i36 Tubular Bells",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i37 RS Vulture",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i38 RS Micro Synth",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i39 Cheap Electric Violin",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i40 Cheap Keys V3",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i41 Cheap Mic V3",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i42 Mid Range Decks",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i43 Mid Range Sax",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i44 Old Cello",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i45 5 String Bass",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i46 Mid Range Kit",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i47 Tuba",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i48 Bassoon",
            "supply": "5000",
            "issued": "5000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i49 Djembe",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i50 Star 30",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i51 Head Mic",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i52 Tanpura",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i53 Take RS",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i54 Pink Guitar",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i55 Bongos",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i56 Gran Casa",
            "supply": "6000",
            "issued": "6000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i57 RSX Desktop Mic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i58 RS Lemon 2",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i59 Pearl White Acoustic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i60 RS Pro EQ",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i61 Sunset V Guitar",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i62 Reggae Drum",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i63 Cheap Wireless Mic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i64 Accordion",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i65 Melodica",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i66 Chinese Bamboo Flutes",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i67 Cheap Cello V2",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i68 Kalimba",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i69 Cheap Mixing Deck",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i70 Starshall MG50",
            "supply": "8000",
            "issued": "6660",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i71 Cheap Congas",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i72 Limey Kit",
            "supply": "16000",
            "issued": "6929",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i73 Cherry Viola",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i74 RS YO",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i75 Karaoke Mic",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i76 Talking Drum",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i77 Juicy Orange Guitar",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i78 Starshall RG30",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i79 Carbon Fibre Acoustic",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i80 Triangle",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i81 Busker R10",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i82 RS58 Budget Mic",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i83 Hand Carved Djembe",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i84 SS Eleven",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i85 NP One",
            "supply": "16000",
            "issued": "15379",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i86 Blue Mist Acoustic",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i87 Native American Drum",
            "supply": "16000",
            "issued": "16000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i88 Blood Red Bass",
            "supply": "25000",
            "issued": "7921",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i89 DLG 10",
            "supply": "25000",
            "issued": "8006",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i90 Hand Cymbals",
            "supply": "25000",
            "issued": "8622",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i91 Pink Riser Desk Mic",
            "supply": "25000",
            "issued": "7669",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i92 PK 125",
            "supply": "25000",
            "issued": "11868",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i93 RSX Condenser Mic",
            "supply": "25000",
            "issued": "9058",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i94 Lemon Violin",
            "supply": "25000",
            "issued": "7503",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i95 Bata Drum",
            "supply": "25000",
            "issued": "951",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i96 Harmonica",
            "supply": "25000",
            "issued": "5118",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i97 RSX 50",
            "supply": "25000",
            "issued": "11968",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "i98 RS Bolt",
            "supply": "25000",
            "issued": "1680",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "R6 Congas",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R7 Vintage Synth",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R12 808 Drum Machine",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R13 Pro Studio Mic",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R14 Cowbell",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R15 Retro Groovebox",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R16 MPC500",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R24 The Red One",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R25 Double Bass",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R26 Lute",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R30 80s Mic",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R31 Nykelharpa",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R33 Hang Drum",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R43 String Machine",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R44 Looper",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R45 Mandolin",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R46 Guitar",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R53 Tabla",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R57 Pink Mic",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R58 Swarmandal",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R62 Chubby Subby",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R64 RS 30 Guitar Synth",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R65 Blue Guitar",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R72 Nadaswaram",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R73 Udukai",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R74 Blue Mic",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R81 RS 101",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R82 RS Vocoder",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R83 Lime Acoustic",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R88 Marching Drum",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R91 Bugle",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R92 Desktop Mic",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R97 RS Nanny",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R98 RS 16",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R99 Flame Guitar",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R112 Bodhran",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R113 Clarinet",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R114 Gold Mic",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R116 Harmonium",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R117 Space Delay",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R118 Semi Acoustic",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R141 Dundun",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R142 Oboe",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R143 Diamond Mic",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R146 Omnistar",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R152 RS Bluey",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R153 Sitar",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R163 Vintage Mic RS1",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R164 Pink Violin",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R165 Newens Kit",
            "supply": "4000",
            "issued": "4000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R172 Green Lightning",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R173 Vuvuzela",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R174 RSX Amp",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R175 RSG Waves",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R176 Vintage Mic RS3",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R177 Pink Kit",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R178 Sax A Boom",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R192 RS Pro Condenser Mic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R193 Violin Acoustic",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R195 Midnight Drums",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R196 Star Visionary",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R197 RS Pro Distortion",
            "supply": "8000",
            "issued": "8000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R212 Raven TI Fire",
            "supply": "8000",
            "issued": "6423",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R213 SA Cream Mic",
            "supply": "8000",
            "issued": "6840",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R221 PT 100 Bass Head",
            "supply": "10000",
            "issued": "2272",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R223 Mint Kit",
            "supply": "10000",
            "issued": "2373",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R224 Alphorn",
            "supply": "10000",
            "issued": "2733",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R225 Fretless Guitar",
            "supply": "10000",
            "issued": "3659",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R226 Toy Piano",
            "supply": "10000",
            "issued": "4620",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "E1",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E6 The Pad Of Chaos",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E7 Grand Piano",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E12 Harp",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E13 Unidyne",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E14 High End Drum Kit",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E15 Mellow Tone",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E17 Pro Acoustic",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E20 Studio Laptop",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E25 Pro Kit",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E26 RS7B Dynamic Mic",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E28 Xylophone",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E34 PC Tower",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E35 RSV Synth",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E36 Cherry Acoustic",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E39 RS L Condenser",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E40 Custom Import Kit",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E42 Electric Violin",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E47 Upright Piano",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E48 RS Pro Chorus",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E49 The Purple One",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E52 Aqua Marine Cello",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E53 Ribbon Mic",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E56 Starbox",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E59 Avocado Guitar",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E60 RS2A Compressor",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E61 Keystar 1A",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E66 Antique Viola",
            "supply": "400",
            "issued": "400 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E67 Street Organ",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E68 Vintage Mic RS2",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E69 Antique Snare",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E70 Sky Blue Guitar",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E71 Keystar 2B",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E79 Blue Sax",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E82 RS 62 Live Mixer",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E84 Vintage Mic RS4",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E87 Burnt Orange Sax",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E88 Dulcitone",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E89 Aqua Stripes Guitar",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E90 Vintage Tick",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E91 Retro Violin",
            "supply": "500",
            "issued": "500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E92 Multi Delay",
            "supply": "750",
            "issued": "195",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E93 Tonga Drum",
            "supply": "750",
            "issued": "181",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E94 Celeste",
            "supply": "750",
            "issued": "174",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E95 Antique Trombone",
            "supply": "750",
            "issued": "208",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E96 Twilight Acoustic",
            "supply": "750",
            "issued": "177",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E97 Indie Mic",
            "supply": "750",
            "issued": "207",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "L5 Fab Four Bass",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L13 Fab Four Drums",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L16 RS Modular Synth",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L19 Snake Mic",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L21 3rd Star 8",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L26 Gong",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L29 Stradivarius",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L30 Voxinator",
            "supply": "100",
            "issued": "75",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L34 7 String Guitar",
            "supply": "100",
            "issued": "20",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "S2 Drumkin",
            "supply": "252",
            "issued": "252 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S3 Pumpkin Bass",
            "supply": "229",
            "issued": "229 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S4 Pumpkin Guitar",
            "supply": "230",
            "issued": "230 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S7 Jingle Bells",
            "supply": "107",
            "issued": "107 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S8 Santas Big Organ",
            "supply": "116",
            "issued": "116 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S15 Love Machine",
            "supply": "124",
            "issued": "124 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S16 Heart Beater",
            "supply": "97",
            "issued": "97 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S18 Bunny Bass",
            "supply": "163",
            "issued": "163 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S19 Easter Egg Guitar",
            "supply": "187",
            "issued": "187 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S21 Cow Horn",
            "supply": "173",
            "issued": "173 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S22 Pan Pipes",
            "supply": "187",
            "issued": "187 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S25 Drop Dead Drums",
            "supply": "697",
            "issued": "697 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S25a Drop Dead Drums",
            "supply": "69",
            "issued": "69 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S26 No Face Bass",
            "supply": "668",
            "issued": "668 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S26a No Face Bass",
            "supply": "66",
            "issued": "66 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S28 Happy Lappy",
            "supply": "840",
            "issued": "840 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S28a Happy Lappy",
            "supply": "84",
            "issued": "84 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S29 Ding Dong Mic",
            "supply": "807",
            "issued": "807 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S29a Ding Dong Mic",
            "supply": "80",
            "issued": "80 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S32 Valentines Violin",
            "supply": "623",
            "issued": "623 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S32a Valentines Violin",
            "supply": "62",
            "issued": "62 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S33 Rose Acoustic",
            "supply": "547",
            "issued": "547 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S33a Rose Acoustic",
            "supply": "54",
            "issued": "54 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S35 Chocolate Chimes",
            "supply": "999999",
            "issued": "2025",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S35a Chocolate Chimes",
            "supply": "999999",
            "issued": "89",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S36 Rabbit Radio",
            "supply": "999999",
            "issued": "1915",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S36a Rabbit Radio",
            "supply": "999999",
            "issued": "84",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S42 The Scratcher",
            "supply": "999999",
            "issued": "1631",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S42a The Scratcher",
            "supply": "999999",
            "issued": "64",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S43 Pro DJ Mixer",
            "supply": "999999",
            "issued": "1601",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "S43a Pro DJ Mixer",
            "supply": "999999",
            "issued": "65",
            "description": "",
            "rarity": "specials"
        }
    ],
    "vehicles": [
        {
            "name": "t1",
            "supply": "3500",
            "issued": "3500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "t2 Mid Range Tour Bus",
            "supply": "9999999",
            "issued": "17048",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "t3 Fizzy",
            "supply": "16000",
            "issued": "706",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "t5 Rubber Dinghy",
            "supply": "9999999",
            "issued": "11650",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "t6 Cheap Car",
            "supply": "9999999",
            "issued": "40864",
            "description": "",
            "rarity": "common"
        },
        {
            "name": "R10 Touring Coach",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R11 Range Rover",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R19 Speed Boat",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R20 Touring Coach",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R36 Jaspa",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R40 Touring Coach",
            "supply": "1750",
            "issued": "1750 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R52 Hippy Wagon",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R60 Touring Coach",
            "supply": "2000",
            "issued": "2000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R78 Jet Ski",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R90 Touring Coach",
            "supply": "2500",
            "issued": "2500 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R115 Microlight",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R140 Touring Coach",
            "supply": "3000",
            "issued": "3000 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R190 Beach Buggy",
            "supply": "8000",
            "issued": "3503",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R200 Touring Coach",
            "supply": "8000",
            "issued": "4793",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "R214 Ice Cream Van",
            "supply": "8000",
            "issued": "1697",
            "description": "",
            "rarity": "rare"
        },
        {
            "name": "E2",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E3 Red Lambo",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E11 Chopper",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E19 Trike",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E21 Classic Car",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E27 Hummy",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E30 Low Rider",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E31 Faux Rari",
            "supply": "250",
            "issued": "250 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E50 Couger Groovy",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E54 Pink Low Rider",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E55 Monstar Truck",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E62 Hummy Limo",
            "supply": "300",
            "issued": "300 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E76 The Destroyer",
            "supply": "500",
            "issued": "287",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E77 Range Rover Limo",
            "supply": "500",
            "issued": "357",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E78 Vintage Road Bike",
            "supply": "500",
            "issued": "266",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "E83 The Junk Slayer",
            "supply": "500",
            "issued": "342",
            "description": "",
            "rarity": "epic"
        },
        {
            "name": "L3 Pink Limo",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L4 Pink Lambo",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L6 Private Jet",
            "supply": "75",
            "issued": "75 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L11 Private Yacht",
            "supply": "50",
            "issued": "50 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L22 Buskerminator",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L28 High Roller",
            "supply": "100",
            "issued": "26",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L31 The Sound Machine",
            "supply": "100",
            "issued": "17",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "L33 Pink Cadillac",
            "supply": "100",
            "issued": "3",
            "description": "",
            "rarity": "legendary"
        },
        {
            "name": "S23 Pizza Bike",
            "supply": "2500",
            "issued": "190",
            "description": "",
            "rarity": "specials"
        }
    ],
    "boosters": [
        {
            "name": "1st Birthday Cake",
            "supply": "313",
            "issued": "313 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "2nd Birthday Cake",
            "supply": "2217",
            "issued": "2217 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Coffee Cup",
            "supply": "9999999",
            "issued": "2885",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "EnergyBoost1",
            "supply": "9999999",
            "issued": "22976",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Pizza Box",
            "supply": "9999999",
            "issued": "14544",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Risky Whiskey",
            "supply": "9999999",
            "issued": "3565",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FanBoost1",
            "supply": "9999999",
            "issued": "7898",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FanBoost10",
            "supply": "9999999",
            "issued": "3423",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FanBoost100",
            "supply": "9999999",
            "issued": "239",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FanBoost5",
            "supply": "9999999",
            "issued": "5179",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "FanBoost50",
            "supply": "9999999",
            "issued": "1115",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RU1 Paula",
            "supply": "500",
            "issued": "381",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RU2 Kevin",
            "supply": "500",
            "issued": "77",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE1 Francis",
            "supply": "100",
            "issued": "11",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE2 Jimmy",
            "supply": "100",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE3 Sid",
            "supply": "100",
            "issued": "11",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE4 Joey",
            "supply": "100",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE5 Tess",
            "supply": "100",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "TE6 Tobias",
            "supply": "100",
            "issued": "10",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "SkillBoost1",
            "supply": "9999999",
            "issued": "10032",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "SkillBoost10",
            "supply": "9999999",
            "issued": "1962",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "SkillBoost100",
            "supply": "9999999",
            "issued": "155",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "SkillBoost50",
            "supply": "9999999",
            "issued": "144",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "XPBoost10",
            "supply": "2100",
            "issued": "2100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "XPBoost100",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "XPBoost50",
            "supply": "160",
            "issued": "160 <font color=white>discontinued</font>",
            "description": "",
            "rarity": "specials"
        }
    ],
    "others": [
        {
            "name": "Can Of Petrol",
            "supply": "9999999",
            "issued": "14167",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Cheap Rehearsal Room",
            "supply": "9999999",
            "issued": "1074",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "First Rehearsal Room",
            "supply": "9999999",
            "issued": "1766",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Shipping Container",
            "supply": "9999999",
            "issued": "26",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Storage Trailer",
            "supply": "9999999",
            "issued": "288",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Storage Warehouse",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Backstage Pass",
            "supply": "9999999",
            "issued": "964",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "Starbits Millionaire",
            "supply": "9999999",
            "issued": "1504",
            "description": "<font color=yellow>IMPORTANT: Only Starbits Millionaire cards issued by Rising Star will work with your account. DO NOT BUY THEM OFF THE MARKET if you plan to try and use it to run the Millionaire mission. If you have 1 million STARBITS on Hive Engine and would like a Millionaire card then contact us in Discord. Please read the Terms & Conditions (in the menu) before applying.</font>",
            "rarity": "specials"
        }
    ],
    "crafted": [
        {
            "name": "RSTAR D1111",
            "supply": "9999999",
            "issued": "19",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1113",
            "supply": "9999999",
            "issued": "88",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1121",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1123",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1131",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1133",
            "supply": "9999999",
            "issued": "7",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1311",
            "supply": "9999999",
            "issued": "14",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1313",
            "supply": "9999999",
            "issued": "23",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1321",
            "supply": "9999999",
            "issued": "14",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1323",
            "supply": "9999999",
            "issued": "78",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1331",
            "supply": "9999999",
            "issued": "9",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D1333",
            "supply": "9999999",
            "issued": "87",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2111",
            "supply": "9999999",
            "issued": "7",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2113",
            "supply": "9999999",
            "issued": "9",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2121",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2123",
            "supply": "9999999",
            "issued": "20",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2131",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2133",
            "supply": "9999999",
            "issued": "14",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2311",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2313",
            "supply": "9999999",
            "issued": "34",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2321",
            "supply": "9999999",
            "issued": "16",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2323",
            "supply": "9999999",
            "issued": "443",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2331",
            "supply": "9999999",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D2333",
            "supply": "9999999",
            "issued": "353",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3111",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3113",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3121",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3123",
            "supply": "9999999",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3131",
            "supply": "9999999",
            "issued": "2",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3133",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3311",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3313",
            "supply": "9999999",
            "issued": "21",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3321",
            "supply": "9999999",
            "issued": "11",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3323",
            "supply": "9999999",
            "issued": "299",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3331",
            "supply": "9999999",
            "issued": "14",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR D3333",
            "supply": "9999999",
            "issued": "1011",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1111",
            "supply": "9999999",
            "issued": "16",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1113",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1121",
            "supply": "9999999",
            "issued": "9",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1123",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1131",
            "supply": "9999999",
            "issued": "5",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1133",
            "supply": "9999999",
            "issued": "14",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1311",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1313",
            "supply": "9999999",
            "issued": "29",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1321",
            "supply": "9999999",
            "issued": "13",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1323",
            "supply": "9999999",
            "issued": "119",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1331",
            "supply": "9999999",
            "issued": "7",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G1333",
            "supply": "9999999",
            "issued": "99",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2111",
            "supply": "9999999",
            "issued": "5",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2113",
            "supply": "9999999",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2121",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2123",
            "supply": "9999999",
            "issued": "34",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2131",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2133",
            "supply": "9999999",
            "issued": "20",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2311",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2313",
            "supply": "9999999",
            "issued": "47",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2321",
            "supply": "9999999",
            "issued": "23",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2323",
            "supply": "9999999",
            "issued": "542",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2331",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G2333",
            "supply": "9999999",
            "issued": "543",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3111",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3113",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3121",
            "supply": "9999999",
            "issued": "6",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3123",
            "supply": "9999999",
            "issued": "7",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3131",
            "supply": "9999999",
            "issued": "5",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3133",
            "supply": "9999999",
            "issued": "18",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3311",
            "supply": "9999999",
            "issued": "10",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3313",
            "supply": "9999999",
            "issued": "40",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3321",
            "supply": "9999999",
            "issued": "10",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3323",
            "supply": "9999999",
            "issued": "472",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3331",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR G3333",
            "supply": "9999999",
            "issued": "1160",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1111",
            "supply": "9999999",
            "issued": "17",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1113",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1121",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1123",
            "supply": "9999999",
            "issued": "13",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1131",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1133",
            "supply": "9999999",
            "issued": "7",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1311",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1313",
            "supply": "9999999",
            "issued": "18",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1321",
            "supply": "9999999",
            "issued": "13",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1323",
            "supply": "9999999",
            "issued": "84",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1331",
            "supply": "9999999",
            "issued": "10",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P1333",
            "supply": "9999999",
            "issued": "84",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2111",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2113",
            "supply": "9999999",
            "issued": "9",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2121",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2123",
            "supply": "9999999",
            "issued": "17",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2131",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2133",
            "supply": "9999999",
            "issued": "13",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2311",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2313",
            "supply": "9999999",
            "issued": "23",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2321",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2323",
            "supply": "9999999",
            "issued": "322",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2331",
            "supply": "9999999",
            "issued": "12",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P2333",
            "supply": "9999999",
            "issued": "434",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3111",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3113",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3121",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3123",
            "supply": "9999999",
            "issued": "10",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3131",
            "supply": "9999999",
            "issued": "3",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3133",
            "supply": "9999999",
            "issued": "11",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3311",
            "supply": "9999999",
            "issued": "4",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3313",
            "supply": "9999999",
            "issued": "15",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3321",
            "supply": "9999999",
            "issued": "8",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3323",
            "supply": "9999999",
            "issued": "292",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3331",
            "supply": "9999999",
            "issued": "11",
            "description": "",
            "rarity": "specials"
        },
        {
            "name": "RSTAR P3333",
            "supply": "9999999",
            "issued": "788",
            "description": "",
            "rarity": "specials"
        }
    ],
    "records": [
        {
            "name": "2nd Birthday",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "And We Fall - Mr Downfall",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Andrewmusic - Doge Dream",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "BeaTraxx - Gaming Collection Volume 1",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "BeaTraxx - Synthwave Collection Volume 1",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Crystals",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Kali",
            "supply": "999999",
            "issued": "54",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Manifesto",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Peacemongers feat Winkandwoo",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Signals",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Silver Lining Remix",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - Starbits Millionaire",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg - The Labyrinth",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Billy Korg feat Pixie - Through The Pixie Dust",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Black Eye Butterfly - I Follow You Blindly",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Black Eye Butterfly - Im Right On",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Black Eye Butterfly - Take This Load Away From Me",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Cheri Lyn - Everyone Loves A Secret",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Dirolls Jackson Castillo and Diane - Lets get ready for this",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Double Eagle - COVID 20-20",
            "supply": "20",
            "issued": "20 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "Double Eagle - Thurmans Kitchen",
            "supply": "999999",
            "issued": "2",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Double Eagle - Thurmans Kitchen 7 inch",
            "supply": "20",
            "issued": "20 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "Double Eagle - United Duality-Double Eagle Split 7 Inch",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font><br><br><font color=37A9E1>This NFT comes with an mp3 download of all tracks from the Single. It is also backed by a </font><font color=white>PHYSICAL VINYL RECORD</font><font color=37A9E1>, and may be exchanged for a copy of the vinyl until (March 31, 2023). Shipment of the vinyl may involve some shipping costs.  To exchange your NFT for the vinyl record, or for more information, please email twiceashighrecords@gmail.com.</font>",
            "rarity": "specials"
        },
        {
            "name": "Double Eagle - Whatchu Gonna Do About It",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Downward Spiral Mantra - China Nights",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Downward Spiral Mantra - Golgotha",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Downward Spiral Mantra - Omicron",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "EvM - Alma Mia",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Gribbles - Ask Ken",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Gribbles - Here",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivanc - I Am An Antenna",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - Amatista",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - Con Tu Piel",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - Hasta Vernos Gritar",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - Las  Olas",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - The Dome",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ivo Orellana - Ventana Abierta",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Jason Langvee - New Coat Of Paint",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Jason Langvee - The Heart of Sunday Afternoon",
            "supply": "10",
            "issued": "10 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "Jeffrey Kolkman - In The Mirror",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Junkfeathers - The Vibe",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Juxta - The Music",
            "supply": "999999",
            "issued": "29",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Karrey - Rising Star Dancehall Tribute Theme Song",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Korben Dallas - Inspektor Mosh",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Korben Dallas - Noch am Leben",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Last Ravage Opinion - Rising Star",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Logan Hate - The Shelter",
            "supply": "100",
            "issued": "100 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "MAN - Alien Experimentation",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "MAN - Voyager",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Mr Candy - On The Way",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Nahupuku - Rupinol",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NewenX - Anubis",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NewenX - Desert Dream",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Newenx - Diablo",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NewenX - Let Yo Beast Out",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NewenX - Mother Nature",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NewenX feat Raven - Madness",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "NOHH - Quiero Verte",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Nupulse - Crypto Warriors",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Olos Lindale - Above the Sea of Clouds",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Olos Lindale - Melusina",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "PZZL - Dance",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "PZZL - Face That",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "Raven - Rising Star",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Raven feat Elena K - You Say To Me Matt Nore Remix",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Raven feat Kristin - Dance Directors Cut",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "San Juan - Full Moon",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "San Juan - Rain",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Screaming Stereo - Enough",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Screaming Stereo - Someday",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Steevc - Ikea",
            "supply": "999999",
            "issued": "26",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Bad Boy",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Be Like You",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Dont Stop",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Engine",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Getaway",
            "supply": "999999",
            "issued": "51",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Going Out",
            "supply": "999999",
            "issued": "49",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Going Out James Black Out Out Remix",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - Party In My Backyard",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Stick Up Boys - So Much Wrong",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "stickup boys - Leaving It For You",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Storm ft L Roman - Issa Vibe",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - Beyond what Our Eyes See",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - Imagine",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - In Search of a Vision",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - Tale of a Hermit",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - The Fire in her Eyes",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - The Way of the Wandering Warrior",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Svart Varg - What Hides the Horizon",
            "supply": "999999",
            "issued": "24",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - Gray Smoke",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - Love Time",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - Mr Hypnosis",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - Sex On The Beach",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - Stars From Heaven",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Taylhardat - The Pharaohs",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "TDC Tunes - Travellers Path",
            "supply": "25",
            "issued": "25 <font color=white>discontinued</font>",
            "rarity": "specials"
        },
        {
            "name": "TDC Tunes and the Stick Up Boys - Dust of the street",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "TDC Tunes feat Stick Up Boys - Travellers Path",
            "supply": "999999",
            "issued": "49",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "The Stress Cones - Doin What Im Doin Dub Mix",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "The Stress Cones - The Road",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "The Turtle Project - We Thrive",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - 2 Prince",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - A Voyage Of Funk",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Chickengreaze 3",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Dont Ever Dont Stop",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Funktacular",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Funky Face",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Funkydelic",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Gettin Kooky",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Good Gawd (Bass Remix)",
            "supply": "999999",
            "issued": "51",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Good Gawd 2",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Joy",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Mr Chop Chop",
            "supply": "999999",
            "issued": "51",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Rawness",
            "supply": "999999",
            "issued": "50",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Star Rising",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - The Good Stuff 2",
            "supply": "999999",
            "issued": "51",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Trenton Lundy - Weird",
            "supply": "999999",
            "issued": "51",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ugochill - Livingston",
            "supply": "999999",
            "issued": "100",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        },
        {
            "name": "Ugochill - Reason to Stay",
            "supply": "999999",
            "issued": "25",
            "description": "Purchase to unlock full download.<br>Stake to receive income (see FAQ).<br><br><a href=main.asp?tab=staking><button>Manage Staking</button></a> <font color=37A9E1>Staked:</font> <font color=orange>0</font>",
            "rarity": "specials"
        }
    ],
    "festival": [
        {
            "name": "FT1 United Kingdom",
            "supply": "999999",
            "issued": "302&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT2 Ireland",
            "supply": "999999",
            "issued": "357&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT3 Netherlands",
            "supply": "999999",
            "issued": "309&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT4 Belgium",
            "supply": "999999",
            "issued": "302&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT5 Germany",
            "supply": "999999",
            "issued": "313&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT6 Denmark",
            "supply": "999999",
            "issued": "277&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT7 Poland",
            "supply": "999999",
            "issued": "244&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT8 Czechia",
            "supply": "999999",
            "issued": "230&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT9 Finland",
            "supply": "999999",
            "issued": "246&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT10 Sweden",
            "supply": "999999",
            "issued": "232&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT11 Norway",
            "supply": "999999",
            "issued": "242&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT12 Iceland",
            "supply": "999999",
            "issued": "244&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>137</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT13 France",
            "supply": "999999",
            "issued": "232&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT14 Spain",
            "supply": "999999",
            "issued": "229&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT15 Portugal",
            "supply": "999999",
            "issued": "227&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT16 Italy",
            "supply": "999999",
            "issued": "212&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT17 Switzerland",
            "supply": "999999",
            "issued": "218&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT18 Luxembourg",
            "supply": "999999",
            "issued": "214&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT19 Austria",
            "supply": "999999",
            "issued": "229&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT20 Hungary",
            "supply": "999999",
            "issued": "201&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT21 Romania",
            "supply": "999999",
            "issued": "193&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT22 Ukraine",
            "supply": "999999",
            "issued": "186&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT23 Greece",
            "supply": "999999",
            "issued": "184&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>117</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT24 UAE",
            "supply": "999999",
            "issued": "168&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT25 South Africa",
            "supply": "999999",
            "issued": "179&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT26 Pakistan",
            "supply": "999999",
            "issued": "189&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT27 India",
            "supply": "999999",
            "issued": "179&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT28 Malaysia",
            "supply": "999999",
            "issued": "197&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT29 Thailand",
            "supply": "999999",
            "issued": "195&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT30 Taiwan",
            "supply": "999999",
            "issued": "198&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT31 Philippines",
            "supply": "999999",
            "issued": "179&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT32 Japan",
            "supply": "999999",
            "issued": "184&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT33 Hong Kong",
            "supply": "999999",
            "issued": "146&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT34 China",
            "supply": "999999",
            "issued": "161&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT35 Peace",
            "supply": "999999",
            "issued": "178&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT36 Singapore",
            "supply": "999999",
            "issued": "153&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT37 Australia",
            "supply": "999999",
            "issued": "151&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT38 New Zealand",
            "supply": "999999",
            "issued": "157&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>94</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT39 USA",
            "supply": "999999",
            "issued": "145&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT40 Canada",
            "supply": "999999",
            "issued": "154&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT41 Mexico",
            "supply": "999999",
            "issued": "145&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT42 Brazil",
            "supply": "999999",
            "issued": "151&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT43 Chile",
            "supply": "999999",
            "issued": "144&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT44 Argentina",
            "supply": "999999",
            "issued": "147&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT45 Venezuela",
            "supply": "999999",
            "issued": "143&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT46 Colombia",
            "supply": "999999",
            "issued": "142&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT47 Bolivia",
            "supply": "999999",
            "issued": "153&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT48 Paraguay",
            "supply": "999999",
            "issued": "141&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT49 Uruguay",
            "supply": "999999",
            "issued": "144&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT50 Peru",
            "supply": "999999",
            "issued": "148&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT51 Ecuador",
            "supply": "999999",
            "issued": "147&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        },
        {
            "name": "FT52 Costa Rica",
            "supply": "999999",
            "issued": "144&nbsp;&nbsp;<font color=37A9E1>Blended :</font> <font color=orange>83</font>",
            "description": "Earn wristbands by doing the Festival World Tour missions.",
            "rarity": "specials"
        }
    ],
    "fanclub": [
        {
            "name": "FC1 Membership Card",
            "supply": "999999",
            "issued": "1334",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC2 Dorris",
            "supply": "999999",
            "issued": "1017",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC3 George",
            "supply": "999999",
            "issued": "709",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC4 Dalilah",
            "supply": "999999",
            "issued": "477",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC5 Rose Petal",
            "supply": "999999",
            "issued": "333",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC6 Rosie",
            "supply": "999999",
            "issued": "249",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC7 Stickers",
            "supply": "999999",
            "issued": "170",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC8 Kris",
            "supply": "999999",
            "issued": "150",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC9 Frankie",
            "supply": "999999",
            "issued": "127",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC10 Sky",
            "supply": "999999",
            "issued": "114",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC11 Belle",
            "supply": "999999",
            "issued": "99",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC12 Jonny",
            "supply": "999999",
            "issued": "93",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC13 Rush",
            "supply": "999999",
            "issued": "90",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC14 Pin Badge",
            "supply": "999999",
            "issued": "73",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC15 Shine",
            "supply": "999999",
            "issued": "69",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC16 MC Bruv",
            "supply": "999999",
            "issued": "67",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC17 Arthur",
            "supply": "999999",
            "issued": "62",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC18 Markie",
            "supply": "999999",
            "issued": "58",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC19 Katie",
            "supply": "999999",
            "issued": "51",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC20 Guitar Picks",
            "supply": "999999",
            "issued": "49",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC21 Winston",
            "supply": "999999",
            "issued": "46",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC22 Drew",
            "supply": "999999",
            "issued": "42",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC23 Stanley",
            "supply": "999999",
            "issued": "40",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC24 Heather",
            "supply": "999999",
            "issued": "40",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC25 Drum Sticks",
            "supply": "999999",
            "issued": "36",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC26 Antonio",
            "supply": "999999",
            "issued": "33",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC27 Bo",
            "supply": "999999",
            "issued": "28",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC28 Courtney",
            "supply": "999999",
            "issued": "25",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC29 Silver Member",
            "supply": "999999",
            "issued": "24",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC30 Michelle",
            "supply": "999999",
            "issued": "22",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC31 Vimbo",
            "supply": "999999",
            "issued": "19",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC32 Valerie",
            "supply": "999999",
            "issued": "18",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC33 Alicia",
            "supply": "999999",
            "issued": "18",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC34 Kayleigh",
            "supply": "999999",
            "issued": "16",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC35 Super Poster",
            "supply": "999999",
            "issued": "16",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC36 Griff",
            "supply": "999999",
            "issued": "16",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC37 Matt",
            "supply": "999999",
            "issued": "13",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        },
        {
            "name": "FC38 Natalie",
            "supply": "999999",
            "issued": "8",
            "description": "Use the Fan Club mission to earn these cards.",
            "rarity": "specials"
        }
    ]
}



def get_contract_table(contract, table, query, offset, indices=[]):

    url = 'https://engine.rishipanthee.com/contracts'
    params = {'contract':contract, 'table':table, 'query':query, 'limit':1000, 'offset':offset, 'indexes':[]}
    j = {'jsonrpc':'2.0', 'id':1, 'method':'find', 'params':params}

    with requests.post(url, json=j) as r:
        data = r.json()
        result = data['result']
        if len(result) == 1000:
            result += get_contract_table(contract, table, query, offset+1000)
    

    return result

def get_history(account, symbol, limit, offset):
        """"Get the transaction history for an account and a token"""
        url = "https://accounts.hive-engine.com/accountHistory?account=%s&limit=%s&offset=%s&symbol=%s" % (account, limit, offset, symbol)
        response = []
        with requests.get(url) as r:
            result = r.json()
            for item in result:
                response.append(item)
                if item["to"] == "null":
                    break
                
             
            if len(response) == 500:
                result += get_history(account, symbol, limit, offset+500)
           

        return response

def account_history(account, symbol, limit, offset):
        """"Get the transaction history for an account and a token"""
        url = "https://accounts.hive-engine.com/accountHistory?account=%s&limit=%s&offset=%s&symbol=%s" % (account, limit, offset, symbol)
        with requests.get(url) as r:
            result = r.json()                
             
            if len(result) == 500:
                result += account_history(account, symbol, limit, offset+500)
           
        return result


@app.route('/getallMota')
def getallMota():
    url = "https://hashkings.info/getallMota/"
    with requests.get(url) as r:
        result = r.text
        
        result =  json.loads(result)
    
        
    return jsonify(result)


@app.route('/specialseeds')
def specialseeds():
    url = "https://hashkings.info/specialseeds/"
    with requests.get(url) as r:
        result = r.json()
    
        
    return  result

@app.route('/time')
def time():
    url = "https://hashkings.info/time/"
    with requests.get(url) as r:
        result = r.json()
           
    return  result

@app.route('/raids')
def raids():
    url = "https://hashkings.info/raids"
    with requests.get(url) as r:
        result = r.json()
    return  result

@app.route('/raidinfo/<string:id>')
def raidinfo(id):
    url = "https://hashkings.info/raidinfo/"+id
    with requests.get(url) as r:
        result = r.json()
           
    return  result


@app.route('/utest/<string:username>', methods=['GET'])
def infouser(username):
    url = "https://hashkings.info/utest/"+username
    with requests.get(url) as r:
        result = r.json()   
        
    return result


@app.route('/proyecto1')
def proyecto1():
    balances =  get_contract_table("tokens", "balances", {"symbol":"BUDSX"}, 0)
    
    balance =  get_contract_table("tokens", "balances", {"account": "hk-staking"}, 0)
    
    budsxSupply =  get_contract_table("tokens", "tokens", {"symbol":"BUDSX"}, 0)
    
    poolPrice =  get_contract_table("marketpools", "pools", {"tokenPair": "BUDS:SWAP.HIVE"}, 0)


    for item in balances:
        item["balance"] = float(item["balance"])

    balances.sort(key=lambda x: x["balance"], reverse=True)

    if balances[0]["account"] == "null":
        balances.pop(0)
    

    return jsonify({"balanceStaking":balance, "budsxSupply":budsxSupply, "poolPrice":poolPrice, "holders":balances})


@app.route('/proyecto2')
def proyecto2():

    # @hk-vault   (`paquetes de avatares)
    # @hk-nvault (porros)
    # @hk-forge  (forja)
    # @hk-dev     (shared market fee)
    # @hashkings  (torres de agua)
    # @hk-bang   (paquetes bang!)
    balancevault = []
    balancenvault = []
    balanceforge = []
    balancedev = []
    balancehashkings = []
    balancebang = []
    accounts= {
        "hk-vault":balancevault,
        "hk-nvault":balancenvault,
        "hk-forge":balanceforge,
        "hk-dev":balancedev,
        "hashkings":balancehashkings,
        "hk-bang":balancebang
    }

    for k, v in accounts.items():
        accounts[k] = get_history(k, "BUDS", 500, 0)


    return jsonify(accounts)


@app.route('/proyecto3')
def proyecto3():
    landplots =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "plot"}, 0)

    return jsonify(landplots)


@app.route('/proyecto4')
def proyecto4():
    avatares =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "avatar"}, 0)

    return jsonify(avatares)


@app.route('/proyecto5')
def proyecto5():

    torres =  get_contract_table("nft", "HKFARMinstances", {"properties.TYPE": "water"}, 0)

    txsSWAPHIVE = []
    txsBUDS = []
    txsHIVE = []
    txs= {
        "SWAP.HIVE":txsSWAPHIVE,
        "BUDS":txsBUDS,
        "HIVE":txsHIVE,
    }

    for k, v in txs.items():
        txs[k] = account_history("hashkings", k, 500, 0)

    return jsonify({"hashkings":txs, "holders":torres})



@app.route('/balances/<string:symbol>', methods=['GET'])
def read_tokens(symbol):

    balances =  get_contract_table("tokens", "balances", {"symbol":symbol}, 0)

    for item in balances:
        item["balance"] = float(item["balance"])


    balances.sort(key=lambda x: x["balance"], reverse=True)

    if balances[0]["account"] == "null":
            balances.pop(0)
            

    return jsonify(balances)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/account/<string:account>', methods=['GET'])
def read_account(account):

    total = []
    total_cartas = 0
    cartas_result = []

    cartas_origin =  get_contract_table("nft", "STARinstances", {"account":account}, 0)

    for i in range(len(cartas_origin)):
        if cartas_origin[i]["properties"]["type"] not in total:
            cartas_result.append(cartas_origin[i])
        total.append(cartas_origin[i]["properties"]["type"])
    
    conteo=Counter(total)   
    

    for carta in cartas_result:
        if carta["properties"]["type"] in especiales:
            slug = f'https://www.risingstargame.com/images/cards/{carta["properties"]["type"].replace(" ", "%20")}.gif'
            # img = f'{carta["properties"]["type"]}.gif'
        else:
            slug = f'https://www.risingstargame.com/images/cards/{carta["properties"]["type"].replace(" ", "%20")}.png'
            # img = f'{carta["properties"]["type"]}.png'
        key, value = 'slug', slug
        key2, value2 = 'count', conteo[carta["properties"]["type"]]
        carta.update({key: value, key2: value2})
        # total_cartas = total_cartas + conteo[carta["properties"]["type"]]
     

    total_cartas = len(cartas_origin)
    total_unicas = len(cartas_result)   

    return jsonify({"cartas":cartas_result,"total_cartas":total_cartas, "total_unicas": total_unicas})



@app.route('/market', methods=['GET'])
def read_market():
        
    # market =  get_contract_table("nftmarket", "STARsellBook", {}, 0)
    # market = requests.get(url)

    with requests.get('https://api.nftm.art/cache?nftID=STAR&details=no') as r:
            result = r.json()        

    return jsonify(result)
