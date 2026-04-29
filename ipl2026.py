"""
╔══════════════════════════════════════════════════════════════════╗
║         IPL 2026 DATA HUB  —  ipl2026.py                        ║
║         Developed by Mutta Nishanth | IPL 2026 Data Hub          ║
╚══════════════════════════════════════════════════════════════════╝

HOW TO RUN
----------
    pip install streamlit matplotlib pandas numpy
    streamlit run ipl2026.py

HOW TO ADD MATCH 42
-------------------
Append one dict to IPL_DATABASE (follow the same structure).
The Points Table and selectbox update automatically.
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np

# ══════════════════════════════════════════════════════════════════
# SECTION 1 ─ MASTER DATABASE
# ══════════════════════════════════════════════════════════════════
# Each entry follows this schema:
#   {
#       "teams"    : (team_a, team_b),
#       "date"     : "Mon DD",
#       "winner"   : "TEAM",          ← use "NR" for No Result
#       "margin"   : "X wickets / Y runs / Super Over / NR",
#       "mom"      : "Player Name",
#       "score"    : {"TEAM_A": runs_or_None, "TEAM_B": runs_or_None},
#       "note"     : ""               ← optional extra context
#   }
#
# TO ADD MATCH 42  →  copy the last block, bump the key, fill values.
# ──────────────────────────────────────────────────────────────────

IPL_DATABASE = {

    # ── MATCH 1 ─────────────────────────────────────────────────────
    "M01 | RCB vs SRH | Mar 28": {
        "teams"  : ("RCB", "SRH"),
        "date"   : "Mar 28",
        "winner" : "RCB",
        "margin" : "3 wickets",
        "mom"    : "Nadine de Klerk",
        "score"  : {"RCB": 172, "SRH": 168},
        "note"   : "",
    },

    # ── MATCH 2 ─────────────────────────────────────────────────────
    "M02 | MI vs KKR | Mar 29": {
        "teams"  : ("MI", "KKR"),
        "date"   : "Mar 29",
        "winner" : "MI",
        "margin" : "6 wickets",
        "mom"    : "Shardul Thakur",
        "score"  : {"MI": 165, "KKR": 162},
        "note"   : "",
    },

    # ── MATCH 3 ─────────────────────────────────────────────────────
    "M03 | RR vs CSK | Mar 30": {
        "teams"  : ("RR", "CSK"),
        "date"   : "Mar 30",
        "winner" : "RR",
        "margin" : "8 wickets",
        "mom"    : "Nandre Burger",
        "score"  : {"RR": 148, "CSK": 145},
        "note"   : "",
    },

    # ── MATCH 4 ─────────────────────────────────────────────────────
    "M04 | PBKS vs GT | Mar 31": {
        "teams"  : ("PBKS", "GT"),
        "date"   : "Mar 31",
        "winner" : "PBKS",
        "margin" : "3 wickets",
        "mom"    : "Cooper Connolly",
        "score"  : {"PBKS": 182, "GT": 179},
        "note"   : "",
    },

    # ── MATCH 5 ─────────────────────────────────────────────────────
    "M05 | LSG vs DC | Apr 1": {
        "teams"  : ("LSG", "DC"),
        "date"   : "Apr 1",
        "winner" : "DC",
        "margin" : "6 wickets",
        "mom"    : "Sameer Rizvi",
        "score"  : {"DC": 175, "LSG": 172},
        "note"   : "",
    },

    # ── MATCH 6 ─────────────────────────────────────────────────────
    "M06 | KKR vs SRH | Apr 2": {
        "teams"  : ("KKR", "SRH"),
        "date"   : "Apr 2",
        "winner" : "SRH",
        "margin" : "65 runs",
        "mom"    : "Nitish Kumar Reddy",
        "score"  : {"SRH": 230, "KKR": 165},
        "note"   : "",
    },

    # ── MATCH 7 ─────────────────────────────────────────────────────
    "M07 | CSK vs PBKS | Apr 3": {
        "teams"  : ("CSK", "PBKS"),
        "date"   : "Apr 3",
        "winner" : "PBKS",
        "margin" : "5 wickets",
        "mom"    : "Priyansh Arya",
        "score"  : {"PBKS": 185, "CSK": 182},
        "note"   : "",
    },

    # ── MATCH 8 ─────────────────────────────────────────────────────
    "M08 | DC vs MI | Apr 4": {
        "teams"  : ("DC", "MI"),
        "date"   : "Apr 4",
        "winner" : "DC",
        "margin" : "6 wickets",
        "mom"    : "Sameer Rizvi",
        "score"  : {"DC": 190, "MI": 186},
        "note"   : "",
    },

    # ── MATCH 9 ─────────────────────────────────────────────────────
    "M09 | GT vs RR | Apr 4": {
        "teams"  : ("GT", "RR"),
        "date"   : "Apr 4",
        "winner" : "RR",
        "margin" : "6 runs",
        "mom"    : "Ravi Bishnoi",
        "score"  : {"RR": 192, "GT": 186},
        "note"   : "",
    },

    # ── MATCH 10 ────────────────────────────────────────────────────
    "M10 | SRH vs LSG | Apr 5": {
        "teams"  : ("SRH", "LSG"),
        "date"   : "Apr 5",
        "winner" : "LSG",
        "margin" : "5 wickets",
        "mom"    : "Mohammed Shami",
        "score"  : {"LSG": 178, "SRH": 175},
        "note"   : "",
    },

    # ── MATCH 11 ────────────────────────────────────────────────────
    "M11 | RCB vs CSK | Apr 5": {
        "teams"  : ("RCB", "CSK"),
        "date"   : "Apr 5",
        "winner" : "RCB",
        "margin" : "43 runs",
        "mom"    : "Tim David",
        "score"  : {"RCB": 220, "CSK": 177},
        "note"   : "",
    },

    # ── MATCH 12 ────────────────────────────────────────────────────
    "M12 | KKR vs PBKS | Apr 6": {
        "teams"  : ("KKR", "PBKS"),
        "date"   : "Apr 6",
        "winner" : "NR",
        "margin" : "No Result (Rain)",
        "mom"    : "—",
        "score"  : {"KKR": None, "PBKS": None},
        "note"   : "Match abandoned due to rain. 1 point each.",
    },

    # ── MATCH 13 ────────────────────────────────────────────────────
    "M13 | RR vs MI | Apr 7": {
        "teams"  : ("RR", "MI"),
        "date"   : "Apr 7",
        "winner" : "RR",
        "margin" : "27 runs",
        "mom"    : "Yashasvi Jaiswal",
        "score"  : {"RR": 210, "MI": 183},
        "note"   : "",
    },

    # ── MATCH 14 ────────────────────────────────────────────────────
    "M14 | DC vs GT | Apr 8": {
        "teams"  : ("DC", "GT"),
        "date"   : "Apr 8",
        "winner" : "GT",
        "margin" : "1 run",
        "mom"    : "Rashid Khan",
        "score"  : {"GT": 185, "DC": 184},
        "note"   : "Nail-biting finish!",
    },

    # ── MATCH 15 ────────────────────────────────────────────────────
    "M15 | KKR vs LSG | Apr 9": {
        "teams"  : ("KKR", "LSG"),
        "date"   : "Apr 9",
        "winner" : "LSG",
        "margin" : "3 wickets",
        "mom"    : "Mukul Choudhary",
        "score"  : {"LSG": 174, "KKR": 171},
        "note"   : "",
    },

    # ── MATCH 16 ────────────────────────────────────────────────────
    "M16 | RR vs RCB | Apr 10": {
        "teams"  : ("RR", "RCB"),
        "date"   : "Apr 10",
        "winner" : "RR",
        "margin" : "6 wickets",
        "mom"    : "Vaibhav Sooryavanshi",
        "score"  : {"RR": 195, "RCB": 190},
        "note"   : "",
    },

    # ── MATCH 17 ────────────────────────────────────────────────────
    "M17 | PBKS vs SRH | Apr 11": {
        "teams"  : ("PBKS", "SRH"),
        "date"   : "Apr 11",
        "winner" : "PBKS",
        "margin" : "6 wickets",
        "mom"    : "Shreyas Iyer",
        "score"  : {"PBKS": 188, "SRH": 185},
        "note"   : "",
    },

    # ── MATCH 18 ────────────────────────────────────────────────────
    "M18 | CSK vs DC | Apr 11": {
        "teams"  : ("CSK", "DC"),
        "date"   : "Apr 11",
        "winner" : "CSK",
        "margin" : "23 runs",
        "mom"    : "Sanju Samson",
        "score"  : {"CSK": 210, "DC": 187},
        "note"   : "",
    },

    # ── MATCH 19 ────────────────────────────────────────────────────
    "M19 | LSG vs GT | Apr 12": {
        "teams"  : ("LSG", "GT"),
        "date"   : "Apr 12",
        "winner" : "GT",
        "margin" : "7 wickets",
        "mom"    : "Prasidh Krishna",
        "score"  : {"GT": 180, "LSG": 176},
        "note"   : "",
    },

    # ── MATCH 20 ────────────────────────────────────────────────────
    "M20 | MI vs RCB | Apr 12": {
        "teams"  : ("MI", "RCB"),
        "date"   : "Apr 12",
        "winner" : "RCB",
        "margin" : "18 runs",
        "mom"    : "Phil Salt",
        "score"  : {"RCB": 205, "MI": 187},
        "note"   : "",
    },

    # ── MATCH 21 ────────────────────────────────────────────────────
    "M21 | SRH vs RR | Apr 13": {
        "teams"  : ("SRH", "RR"),
        "date"   : "Apr 13",
        "winner" : "SRH",
        "margin" : "57 runs",
        "mom"    : "Praful Hinge",
        "score"  : {"SRH": 240, "RR": 183},
        "note"   : "",
    },

    # ── MATCH 22 ────────────────────────────────────────────────────
    "M22 | CSK vs KKR | Apr 14": {
        "teams"  : ("CSK", "KKR"),
        "date"   : "Apr 14",
        "winner" : "CSK",
        "margin" : "32 runs",
        "mom"    : "Noor Ahmad",
        "score"  : {"CSK": 215, "KKR": 183},
        "note"   : "",
    },

    # ── MATCH 23 ────────────────────────────────────────────────────
    "M23 | RCB vs LSG | Apr 15": {
        "teams"  : ("RCB", "LSG"),
        "date"   : "Apr 15",
        "winner" : "RCB",
        "margin" : "5 wickets",
        "mom"    : "Josh Hazlewood",
        "score"  : {"RCB": 192, "LSG": 188},
        "note"   : "",
    },

    # ── MATCH 24 ────────────────────────────────────────────────────
    "M24 | MI vs PBKS | Apr 16": {
        "teams"  : ("MI", "PBKS"),
        "date"   : "Apr 16",
        "winner" : "PBKS",
        "margin" : "7 wickets",
        "mom"    : "Arshdeep Singh",
        "score"  : {"PBKS": 178, "MI": 174},
        "note"   : "",
    },

    # ── MATCH 25 ────────────────────────────────────────────────────
    "M25 | GT vs KKR | Apr 17": {
        "teams"  : ("GT", "KKR"),
        "date"   : "Apr 17",
        "winner" : "GT",
        "margin" : "5 wickets",
        "mom"    : "Shubman Gill",
        "score"  : {"GT": 200, "KKR": 196},
        "note"   : "",
    },

    # ── MATCH 26 ────────────────────────────────────────────────────
    "M26 | RCB vs DC | Apr 18": {
        "teams"  : ("RCB", "DC"),
        "date"   : "Apr 18",
        "winner" : "DC",
        "margin" : "6 wickets",
        "mom"    : "Tristan Stubbs",
        "score"  : {"DC": 198, "RCB": 194},
        "note"   : "",
    },

    # ── MATCH 27 ────────────────────────────────────────────────────
    "M27 | SRH vs CSK | Apr 18": {
        "teams"  : ("SRH", "CSK"),
        "date"   : "Apr 18",
        "winner" : "SRH",
        "margin" : "10 runs",
        "mom"    : "Eshan Malinga",
        "score"  : {"SRH": 195, "CSK": 185},
        "note"   : "",
    },

    # ── MATCH 28 ────────────────────────────────────────────────────
    "M28 | KKR vs RR | Apr 19": {
        "teams"  : ("KKR", "RR"),
        "date"   : "Apr 19",
        "winner" : "KKR",
        "margin" : "4 wickets",
        "mom"    : "Varun Chakaravarthy",
        "score"  : {"KKR": 188, "RR": 185},
        "note"   : "",
    },

    # ── MATCH 29 ────────────────────────────────────────────────────
    "M29 | PBKS vs LSG | Apr 19": {
        "teams"  : ("PBKS", "LSG"),
        "date"   : "Apr 19",
        "winner" : "PBKS",
        "margin" : "54 runs",
        "mom"    : "Priyansh Arya",
        "score"  : {"PBKS": 230, "LSG": 176},
        "note"   : "",
    },

    # ── MATCH 30 ────────────────────────────────────────────────────
    "M30 | GT vs MI | Apr 20": {
        "teams"  : ("GT", "MI"),
        "date"   : "Apr 20",
        "winner" : "MI",
        "margin" : "99 runs",
        "mom"    : "Tilak Varma",
        "score"  : {"MI": 260, "GT": 161},
        "note"   : "Biggest win of the season so far!",
    },

    # ── MATCH 31 ────────────────────────────────────────────────────
    "M31 | SRH vs DC | Apr 21": {
        "teams"  : ("SRH", "DC"),
        "date"   : "Apr 21",
        "winner" : "SRH",
        "margin" : "47 runs",
        "mom"    : "Abhishek Sharma",
        "score"  : {"SRH": 228, "DC": 181},
        "note"   : "",
    },

    # ── MATCH 32 ────────────────────────────────────────────────────
    "M32 | LSG vs RR | Apr 22": {
        "teams"  : ("LSG", "RR"),
        "date"   : "Apr 22",
        "winner" : "RR",
        "margin" : "40 runs",
        "mom"    : "Ravindra Jadeja",
        "score"  : {"RR": 220, "LSG": 180},
        "note"   : "",
    },

    # ── MATCH 33 ────────────────────────────────────────────────────
    "M33 | MI vs CSK | Apr 23": {
        "teams"  : ("MI", "CSK"),
        "date"   : "Apr 23",
        "winner" : "CSK",
        "margin" : "103 runs",
        "mom"    : "Sanju Samson",
        "score"  : {"CSK": 250, "MI": 147},
        "note"   : "Sanju Samson's second MoM of the season.",
    },

    # ── MATCH 34 ────────────────────────────────────────────────────
    "M34 | RCB vs GT | Apr 24": {
        "teams"  : ("RCB", "GT"),
        "date"   : "Apr 24",
        "winner" : "RCB",
        "margin" : "5 wickets",
        "mom"    : "Virat Kohli",
        "score"  : {"RCB": 205, "GT": 200},
        "note"   : "",
    },

    # ── MATCH 35 ────────────────────────────────────────────────────
    "M35 | DC vs PBKS | Apr 25": {
        "teams"  : ("DC", "PBKS"),
        "date"   : "Apr 25",
        "winner" : "PBKS",
        "margin" : "6 wickets",
        "mom"    : "KL Rahul",
        "score"  : {"PBKS": 265, "DC": 263},
        "note"   : "PBKS chased down 264 — highest chase of IPL 2026!",
    },

    # ── MATCH 36 ────────────────────────────────────────────────────
    "M36 | RR vs SRH | Apr 25": {
        "teams"  : ("RR", "SRH"),
        "date"   : "Apr 25",
        "winner" : "SRH",
        "margin" : "5 wickets",
        "mom"    : "Ishan Kishan",
        "score"  : {"SRH": 229, "RR": 227},
        "note"   : "SRH chased 228 — exceptional effort.",
    },

    # ── MATCH 37 ────────────────────────────────────────────────────
    "M37 | CSK vs GT | Apr 26": {
        "teams"  : ("CSK", "GT"),
        "date"   : "Apr 26",
        "winner" : "GT",
        "margin" : "8 wickets",
        "mom"    : "Kagiso Rabada",
        "score"  : {"GT": 178, "CSK": 175},
        "note"   : "",
    },

    # ── MATCH 38 ────────────────────────────────────────────────────
    "M38 | LSG vs KKR | Apr 26": {
        "teams"  : ("LSG", "KKR"),
        "date"   : "Apr 26",
        "winner" : "KKR",
        "margin" : "Super Over",
        "mom"    : "Rinku Singh",
        "score"  : {"KKR": 185, "LSG": 185},
        "note"   : "Tied — KKR won the Super Over.",
    },

    # ── MATCH 39 ────────────────────────────────────────────────────
    "M39 | DC vs RCB | Apr 27": {
        "teams"  : ("DC", "RCB"),
        "date"   : "Apr 27",
        "winner" : "RCB",
        "margin" : "9 wickets",
        "mom"    : "Josh Hazlewood",
        "score"  : {"RCB": 165, "DC": 163},
        "note"   : "Josh Hazlewood's second MoM of the season.",
    },

    # ── MATCH 40 ────────────────────────────────────────────────────
    "M40 | PBKS vs RR | Apr 28": {
        "teams"  : ("PBKS", "RR"),
        "date"   : "Apr 28",
        "winner" : "RR",
        "margin" : "6 wickets",
        "mom"    : "Donovan Ferreira",
        "score"  : {"RR": 198, "PBKS": 194},
        "note"   : "",
    },

    # ── MATCH 41 ── LIVE / TODAY ─────────────────────────────────────
    "M41 | MI vs SRH | Apr 29  🔴 LIVE": {
        "teams"  : ("MI", "SRH"),
        "date"   : "Apr 29",
        "winner" : "MI",           # MI batting first at 225/7
        "margin" : "TBD — MI 225/7 (innings ongoing)",
        "mom"    : "Ryan Rickelton (87*)",
        "score"  : {"MI": 225, "SRH": None},
        "note"   : "🔴 LIVE: MI posted 225/7. SRH yet to bat. "
                   "Ryan Rickelton scored a massive 87!",
    },

    # ══════════════════════════════════════════════════════════════════
    # ➕ ADD MATCH 42 HERE — copy the block below and fill values
    # ══════════════════════════════════════════════════════════════════
    # "M42 | TEAM_A vs TEAM_B | MMM DD": {
    #     "teams"  : ("TEAM_A", "TEAM_B"),
    #     "date"   : "MMM DD",
    #     "winner" : "TEAM_A",
    #     "margin" : "X wickets",
    #     "mom"    : "Player Name",
    #     "score"  : {"TEAM_A": 0, "TEAM_B": 0},
    #     "note"   : "",
    # },
}


# ══════════════════════════════════════════════════════════════════
# SECTION 2 ─ POINTS TABLE CALCULATOR
# ══════════════════════════════════════════════════════════════════
TEAMS = ["RCB", "MI", "RR", "PBKS", "DC", "GT", "SRH", "CSK", "KKR", "LSG"]

TEAM_COLOR = {
    "RCB" : "#CC0000",
    "MI"  : "#004BA0",
    "RR"  : "#EA1A7F",
    "PBKS": "#ED1B24",
    "DC"  : "#0078BC",
    "GT"  : "#1C1C1C",
    "SRH" : "#FF6200",
    "CSK" : "#FDB913",
    "KKR" : "#3A225D",
    "LSG" : "#A4C639",
}


def compute_points_table(db: dict) -> pd.DataFrame:
    stats = {t: {"P": 0, "W": 0, "L": 0, "NR": 0, "Pts": 0} for t in TEAMS}

    for match in db.values():
        t1, t2 = match["teams"]
        w       = match["winner"]

        if w == "NR":
            for t in (t1, t2):
                stats[t]["P"]  += 1
                stats[t]["NR"] += 1
                stats[t]["Pts"] += 1
        else:
            loser = t2 if w == t1 else t1
            stats[w]["P"]   += 1
            stats[w]["W"]   += 1
            stats[w]["Pts"] += 2
            stats[loser]["P"] += 1
            stats[loser]["L"] += 1

    rows = []
    for t, s in stats.items():
        rows.append({"Team": t, "P": s["P"], "W": s["W"],
                     "L": s["L"], "NR": s["NR"], "Pts": s["Pts"]})

    df = pd.DataFrame(rows).sort_values(["Pts", "W"], ascending=False).reset_index(drop=True)
    df.index += 1      # rank starts at 1
    return df


# ══════════════════════════════════════════════════════════════════
# SECTION 3 ─ CHART GENERATOR
# ══════════════════════════════════════════════════════════════════

def build_score_chart(match: dict, match_key: str) -> plt.Figure:
    t1, t2     = match["teams"]
    s1         = match["score"][t1]
    s2         = match["score"][t2]
    winner     = match["winner"]

    # Handle None scores (no result / live second innings)
    s1_val = s1 if s1 is not None else 0
    s2_val = s2 if s2 is not None else 0

    colors = [
        TEAM_COLOR.get(t1, "#888888"),
        TEAM_COLOR.get(t2, "#888888"),
    ]
    labels = [
        f"{t1}\n{'🏆 Winner' if winner == t1 else ''}",
        f"{t2}\n{'🏆 Winner' if winner == t2 else ''}",
    ]
    values = [s1_val, s2_val]

    fig, ax = plt.subplots(figsize=(7, 4.5))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#161b22")

    bars = ax.bar(labels, values, color=colors, width=0.45,
                  edgecolor="white", linewidth=0.7)

    # value labels on bars
    for bar, val, t in zip(bars, [s1, s2], [t1, t2]):
        label = str(val) if val is not None else "—"
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 2,
                label, ha="center", va="bottom",
                color="white", fontsize=14, fontweight="bold")

    ax.set_ylabel("Runs", color="#aaaaaa", fontsize=11)
    ax.set_title(f"Score Comparison — {match_key.split('|')[1].strip()}",
                 color="white", fontsize=13, pad=12)
    ax.tick_params(colors="white", labelsize=11)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#333")
    ax.set_ylim(0, max(s1_val, s2_val, 1) * 1.18)

    # winner badge
    if winner not in ("NR", "TBD"):
        ax.annotate(f"🏆 {winner} won by {match['margin']}",
                    xy=(0.5, 0.94), xycoords="axes fraction",
                    ha="center", color="#FFD700",
                    fontsize=10, fontweight="bold")

    fig.tight_layout()
    return fig


# ══════════════════════════════════════════════════════════════════
# SECTION 4 ─ STREAMLIT UI
# ══════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="IPL 2026 Data Hub | Mutta Nishanth",
    page_icon="🏏",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Teko:wght@400;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.banner {
    background: linear-gradient(135deg, #ff6200 0%, #cc0000 50%, #1c1c4a 100%);
    border-radius: 14px;
    padding: 28px 36px 20px;
    margin-bottom: 28px;
}
.banner h1 {
    font-family: 'Teko', sans-serif;
    font-size: 3rem;
    letter-spacing: 4px;
    color: white;
    margin: 0;
    text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}
.banner p { color: rgba(255,255,255,0.75); margin: 4px 0 0; font-size: 0.92rem; }

.section-head {
    font-family: 'Teko', sans-serif;
    font-size: 1.6rem;
    letter-spacing: 2px;
    color: #FF6200;
    border-bottom: 2px solid #FF6200;
    padding-bottom: 4px;
    margin: 20px 0 14px;
}

.match-card {
    background: #161b22;
    border: 1px solid #30363d;
    border-left: 5px solid #FF6200;
    border-radius: 10px;
    padding: 18px 22px;
    margin-bottom: 14px;
}
.match-card h3 { color: #e6edf3; font-size: 1.1rem; margin: 0 0 8px; }
.badge {
    display: inline-block;
    background: #238636;
    color: white;
    border-radius: 20px;
    padding: 3px 13px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 6px;
}
.chip {
    display: inline-block;
    background: #21262d;
    border: 1px solid #30363d;
    border-radius: 20px;
    padding: 3px 12px;
    font-size: 0.78rem;
    color: #8b949e;
    margin: 3px 3px 3px 0;
}
.chip b { color: #e6edf3; }
.note-box {
    background: #21262d;
    border-left: 3px solid #FFD700;
    border-radius: 6px;
    padding: 8px 14px;
    font-size: 0.82rem;
    color: #aaaaaa;
    margin-top: 10px;
}
.live-badge {
    background: #cc0000;
    color: white;
    border-radius: 20px;
    padding: 3px 13px;
    font-size: 0.8rem;
    font-weight: 700;
    animation: pulse 1.5s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.5} }

.footer {
    margin-top: 3rem;
    padding: 16px;
    text-align: center;
    font-size: 0.78rem;
    color: #484f58;
    border-top: 1px solid #21262d;
}
</style>
""", unsafe_allow_html=True)


# ── Banner ─────────────────────────────────────────────────────────
st.markdown("""
<div class="banner">
    <h1>🏏 IPL 2026 DATA HUB</h1>
    <p>All 41 matches · Live updates · Points table · Score charts</p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# POINTS TABLE
# ══════════════════════════════════════════════════════════════════
st.markdown('<p class="section-head">📊 POINTS TABLE</p>', unsafe_allow_html=True)
points_df = compute_points_table(IPL_DATABASE)

# Highlight top-4 qualifier zone
def highlight_rows(row):
    rank = row.name
    if rank <= 4:
        return ["background-color: #1a2e1a; color: #7ee787"] * len(row)
    return [""] * len(row)

styled = points_df.style.apply(highlight_rows, axis=1)
st.dataframe(styled, use_container_width=True, height=390)
st.caption("🟢 Top 4 (green) qualify for playoffs. Points estimated from match results.")


# ══════════════════════════════════════════════════════════════════
# MATCH EXPLORER
# ══════════════════════════════════════════════════════════════════
st.markdown('<p class="section-head">🔍 MATCH EXPLORER</p>', unsafe_allow_html=True)

match_keys   = list(IPL_DATABASE.keys())
selected_key = st.selectbox(
    "Select a match to inspect:",
    match_keys,
    index=len(match_keys) - 1,      # default to latest match
    help="Scroll through all 41 matches. Match 41 is today's live game.",
)

match = IPL_DATABASE[selected_key]
t1, t2 = match["teams"]
is_live = "LIVE" in selected_key
is_nr   = match["winner"] == "NR"

# Match card
winner_badge = (
    '<span class="live-badge">🔴 LIVE</span>' if is_live
    else '<span class="badge">🏆 ' + match["winner"] + ' Won</span>' if not is_nr
    else '<span class="chip" style="border-color:#888"><b>No Result</b></span>'
)

note_html = (
    f'<div class="note-box">📝 {match["note"]}</div>'
    if match["note"] else ""
)

s1 = match["score"][t1]
s2 = match["score"][t2]
score_str_1 = str(s1) if s1 is not None else "—"
score_str_2 = str(s2) if s2 is not None else "—"

st.markdown(f"""
<div class="match-card">
    <h3>{t1} vs {t2} &nbsp;·&nbsp; {match['date']}</h3>
    {winner_badge}
    <br><br>
    <span class="chip">📅 Date <b>{match['date']}</b></span>
    <span class="chip">🏏 Margin <b>{match['margin']}</b></span>
    <span class="chip">⭐ MoM <b>{match['mom']}</b></span>
    <span class="chip">{t1} Score <b>{score_str_1}</b></span>
    <span class="chip">{t2} Score <b>{score_str_2}</b></span>
    {note_html}
</div>
""", unsafe_allow_html=True)


# Score comparison chart
if is_nr:
    st.info("No chart available — this match was abandoned (No Result).")
else:
    fig = build_score_chart(match, selected_key)
    st.pyplot(fig)

    if is_live:
        st.warning("⚠️ Scores are live/partial. SRH innings yet to begin.")


# ══════════════════════════════════════════════════════════════════
# ALL RESULTS TABLE
# ══════════════════════════════════════════════════════════════════
st.markdown('<p class="section-head">📋 ALL MATCH RESULTS</p>', unsafe_allow_html=True)

rows = []
for key, m in IPL_DATABASE.items():
    t1, t2 = m["teams"]
    rows.append({
        "Match"   : key.split("|")[0].strip(),
        "Fixture" : f"{t1} vs {t2}",
        "Date"    : m["date"],
        "Winner"  : m["winner"] if m["winner"] != "NR" else "No Result",
        "Margin"  : m["margin"],
        "MoM"     : m["mom"],
    })

all_df = pd.DataFrame(rows)
st.dataframe(all_df, use_container_width=True, height=350, hide_index=True)


# ══════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    Developed by <strong>Mutta Nishanth</strong> &nbsp;|&nbsp; IPL 2026 Data Hub
    &nbsp;·&nbsp; Built with Streamlit & Matplotlib &nbsp;·&nbsp; Updated through Match 41
</div>
""", unsafe_allow_html=True)