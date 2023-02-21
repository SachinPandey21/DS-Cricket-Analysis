from flask import Flask, request
from bs4 import BeautifulSoup 
import urllib.request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method = "post">
        <header style="background-color: #2ecc71;box-shadow: 2px 2px 20px 23px #7fecad;padding: 10px;
      border-radius: 4px;"><center><h2>Welcome to CricViewSP </h2></center></header>
        <div style="font-family: cursive, sans-serif; 
        background-color: #f1f1f1;
        justify-content: center;">
        <p><center><br>
        Here you can compare the performances of the players.
        <br>Here it goes....
        </center></p><br>
        </div>
        
        <section style="background-color: #f1f1f1;">
        
        
        <div style=" background-color: #f1f1f1; ">
          <center><div style="width: 15em;
            border: 1px solid #333;
            box-shadow: 8px 8px 5px #444;
            padding: 8px 12px;
            background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);">
           <label for="name">Your Team: </label>
           <input type="text" id="name" name="name"><br><br>
           
           <label for="name">Opponent's team: </label>
           <input type="text" id="o_name" name="o_name">
           <br>
          </center></div>
        </div>
        <br>
        <hr>
        <marquee style="font-family: cursive, sans-serif; font-style: italic; "><strong style ="color: red">Cricket News:</strong> {}</marquee>
        <hr>  
        <div><strong style="color:blue">Disclaimer<sup>**</sup>:</strong> Enter 0 in case of player Did Not Bat(DNB)</div>
        <br>
        <br>
        
        <center><div style=" width: 15em;
        border: 1px solid #333;
        box-shadow: 8px 8px 5px #444;
        padding: 8px 12px;
        background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);">
        <p>Enter the respective runs made by the batsman of your team :-</p>
        
        <label for="Plater1"></label>
        Player1:<input type="text" id="Player1" name="Player1"><br><br>
        <label for="Plater2"></label>
        Player2:<input type="text" id="Player2" name="Player2"><br><br>
        <label for="Plater3"></label>
        Player3:<input type="text" id="Player3" name="Player3"><br><br>
        <label for="Plater4"></label>
        Player4:<input type="text" id="Player4" name="Player4"><br><br>
        <label for="Plater5"></label>
        Player5:<input type="text" id="Player5" name="Player5"><br><br>
        <label for="Plater6"></label>
        Player6:<input type="text" id="Player6" name="Player6"><br><br>
        <label for="Plater7"></label>
        Player7:<input type="text" id="Player7" name="Player7"><br><br>
        <label for="Plater8"></label>
        Player8:<input type="text" id="Player8" name="Player8"><br><br>
        <label for="Plater9"></label>
        Player9:<input type="text" id="Player9" name="Player9"><br><br>
        <label for="Plater10"></label>
        Player10:<input type="text" id="Player10" name="Player10"><br><br>
        <label for="Plater11"></label>
        Player11:<input type="text" id="Player11" name="Player11"><br><br>

        </div></center>
        <br><br>
        
        <center><div style="width: 15em;
        border: 1px solid #333;
        box-shadow: 8px 8px 5px #444;
        padding: 8px 12px;
        background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);">
        <p>Enter the respective runs made by the batsman of opponent's team:- </p>
        
        <label for="plater1"></label>
        Player1:<input type="text" id="player1" name="player1"><br><br>
        <label for="plater2"></label>
        Player2:<input type="text" id="player2" name="player2"><br><br>
        <label for="plater3"></label>
        Player3:<input type="text" id="player3" name="player3"><br><br>
        <label for="plater4"></label>
        Player4:<input type="text" id="player4" name="player4"><br><br>
        <label for="plater5"></label>
        Player5:<input type="text" id="player5" name="player5"><br><br>
        <label for="plater6"></label>
        Player6:<input type="text" id="player6" name="player6"><br><br>
        <label for="plater7"></label>
        Player7:<input type="text" id="player7" name="player7"><br><br>
        <label for="plater8"></label>
        Player8:<input type="text" id="player8" name="player8"><br><br>
        <label for="plater9"></label>
        Player9:<input type="text" id="player9" name="player9"><br><br>
        <label for="plater10"></label>
        Player10:<input type="text" id="player10" name="player10"><br><br>
        <label for="plater11"></label>
        Player11:<input type="text" id="player11" name="player11"><br><br>
        <br>
        
        </div></center>
        <br>
        <br>
        <div style="
         background-color:#0a0a23;
         color: #fff;
         border:none;
         border-radius:10px;
         box-shadow: 0px 0px 2px 2px rgb(0,0,0);"><center>
        <input type="submit" value="Submit">
        </center></div>
        <br>
        <hr><center> @copyright Sachin Pandey</center><hr>
        </section>
        </form>
    '''.format( web_scraping_in_action() )
    

@app.route('/', methods=['POST'])
def show_runs():
    name = request.form['name']
    o_name = request.form['o_name']

    # getting runs made by players
    Player1 = int(request.form['Player1'])
    Player2 = int(request.form['Player2'])
    Player3 = int(request.form['Player3'])
    Player4 = int(request.form['Player4'])
    Player5 = int(request.form['Player5'])
    Player6 = int(request.form['Player6'])
    Player7 = int(request.form['Player7'])
    Player8 = int(request.form['Player8'])
    Player9 = int(request.form['Player9'])
    Player10 = int(request.form['Player10'])
    Player11 = int(request.form['Player11'])

    player1 = int(request.form['player1'])
    player2 = int(request.form['player2'])
    player3 = int(request.form['player3'])
    player4 = int(request.form['player4'])
    player5 = int(request.form['player5'])
    player6 = int(request.form['player6'])
    player7 = int(request.form['player7'])
    player8 = int(request.form['player8'])
    player9 = int(request.form['player9'])
    player10 = int(request.form['player10'])
    player11 = int(request.form['player11'])

    return'''
    <section style="background-color: #f1f1f1;">
    <div><h2><center><br>{} VS {}</center></h2></div>
    <center><strong style="color:green">|----------FINAL SCORES----------|</strong></center>
    <br>
        <hr>
        <marquee style="font-family: cursive, sans-serif; font-style: italic; "><strong style ="color: red">Cricket News:</strong> {}</marquee>
        <hr>  
    <br>
    
    <center>
        <div>
            <div style="width: 15em;
            border: 1px solid #333;
            box-shadow: 8px 8px 5px #444;
            padding: 8px 12px;
            background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);">
            
            <p>Your Team <h4>{}</h4><p>
            <p>
            Player1 : {}<br><br>
            Player2 : {}<br><br>
            Player3 : {}<br><br>
            Player4 : {}<br><br>
            Player5 : {}<br><br>
            Player6 : {}<br><br>
            Player7 : {}<br><br>
            Player8 : {}<br><br>
            Player9 : {}<br><br>
            Player10: {}<br><br>
            Player11: {}<br><br>
            </p></div>
            
            <br><br>
            
            <div style="width: 15em;
            border: 1px solid #333;
            box-shadow: 8px 8px 5px #444;
            padding: 8px 12px;
            background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc);">
            <p>Opponent's Team <h4>{}</h4></p>
            <p>
            Player1 : {}<br><br>
            Player2 : {}<br><br>
            Player3 : {}<br><br>
            Player4 : {}<br><br>
            Player5 : {}<br><br>
            Player6 : {}<br><br>
            Player7 : {}<br><br>
            Player8 : {}<br><br>
            Player9 : {}<br><br>
            Player10: {}<br><br>
            Player11: {}<br><br>
            </p></div>
        </div>
        <div>
            <br><hr><hr><br>
            <h2><p>Winner: {}</p></h2><br>
        </div>
        <hr><center> @copyright Sachin Pandey</center><hr>
    </center></section>
    '''.format(name, o_name,web_scraping_in_action(), name, Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8, Player9, Player10, Player11, o_name, player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, win_show(), show_graphs())

@app.route('/', methods=['POST'])
def show_graphs():
    # getting runs made by players
    Player1 = int(request.form['Player1'])
    Player2 = int(request.form['Player2'])
    Player3 = int(request.form['Player3'])
    Player4 = int(request.form['Player4'])
    Player5 = int(request.form['Player5'])
    Player6 = int(request.form['Player6'])
    Player7 = int(request.form['Player7'])
    Player8 = int(request.form['Player8'])
    Player9 = int(request.form['Player9'])
    Player10 = int(request.form['Player10'])
    Player11 = int(request.form['Player11'])

    player1 = int(request.form['player1'])
    player2 = int(request.form['player2'])
    player3 = int(request.form['player3'])
    player4 = int(request.form['player4'])
    player5 = int(request.form['player5'])
    player6 = int(request.form['player6'])
    player7 = int(request.form['player7'])
    player8 = int(request.form['player8'])
    player9 = int(request.form['player9'])
    player10 = int(request.form['player10'])
    player11 = int(request.form['player11'])
    
    team1 = [Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11]
    
    team2 = [player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]

# showing through line graphs (combine)
    fig = plt.figure(1)
    ypoints = np.array([Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11])
    plt.plot(ypoints, linestyle='dashed')
    plt.xlabel("Players")
    plt.ylabel("Runs")
    
    ypoints = np.array([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])
    plt.plot(ypoints, linestyle='dashed')
    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.show()
    
# showing through line graphs (separated)
    fig = plt.figure(2)
    ypoints = np.array([Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11])
    plt.subplot(1, 2, 1)
    plt.plot(ypoints, linestyle='dashed')
    plt.xlabel("Players")
    plt.ylabel("Runs")
    
    ypoints = np.array([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])
    plt.subplot(1, 2, 2)
    plt.plot(ypoints, linestyle='dashed', color = "red")
    plt.xlabel("Players")
    plt.ylabel("Runs")
    plt.show() 

# showing through scatter bars (separated)
    fig = plt.figure(3)
    x_axis1 = np.array(['Player1','Player2','Player3','Player4','Player5','Player6','Player7','Player8','Player9','Player10','Player11'])
    x_axis = np.array(['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11'])
    
    ypoints = np.array([Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11])
    plt.subplot(1,2,1)
    plt.bar(x_axis, ypoints, width=0.1)
    
    ypoints = np.array([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])
    plt.subplot(1,2,2)
    plt.bar(x_axis, ypoints, color="red", width=0.1)
    plt.show()
    
# showing through pie charts (separated)
    fig = plt.figure(5)
    ypoints = np.array([Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11])
    plt.title("team1")
    plt.pie(ypoints, labels=x_axis1)
    plt.show()
    
    ypoints = np.array([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])
    plt.title("team2")
    plt.pie(ypoints, labels=x_axis1)
    plt.show()
    
# showing through pie charts (combined)
    fig = plt.figure(4)
    ypoints = np.array([Player1,Player2,Player3,Player4,Player5,Player6,Player7,Player8,Player9,Player10,Player11])
    plt.subplot(1,2,1)
    plt.pie(ypoints, labels=x_axis)
    
    ypoints = np.array([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])
    plt.subplot(1,2,2)
    plt.pie(ypoints, labels=x_axis)
    plt.show()
    
    
    
def win_show():
    
    name = request.form['name']
    o_name = request.form['o_name']
    
    # getting runs made by players
    Player1 = int(request.form['Player1'])
    Player2 = int(request.form['Player2'])
    Player3 = int(request.form['Player3'])
    Player4 = int(request.form['Player4'])
    Player5 = int(request.form['Player5'])
    Player6 = int(request.form['Player6'])
    Player7 = int(request.form['Player7'])
    Player8 = int(request.form['Player8'])
    Player9 = int(request.form['Player9'])
    Player10 = int(request.form['Player10'])
    Player11 = int(request.form['Player11'])

    player1 = int(request.form['player1'])
    player2 = int(request.form['player2'])
    player3 = int(request.form['player3'])
    player4 = int(request.form['player4'])
    player5 = int(request.form['player5'])
    player6 = int(request.form['player6'])
    player7 = int(request.form['player7'])
    player8 = int(request.form['player8'])
    player9 = int(request.form['player9'])
    player10 = int(request.form['player10'])
    player11 = int(request.form['player11'])
    
    team1 = Player1 + Player2 + Player3 + Player4 + Player5 + Player6 + Player7 + Player8 + Player9 + Player10 + Player11
    team2 = player1 + player2 + player3 + player4 + player5 + player6 + player7 + player8 + player9 + player10 + player11
    
    if team1 > team2:
        return '''{}||    {}:{}||   {}:{}'''.format(name,name,team1,o_name, team2)
    
    elif team1 == team2:
        return '''Match Draw||   {}:{}||   {}:{}'''.format(name,team1,o_name, team2)
    
    else:
        return '''{}||    {}:{}||   {}:{}'''.format(o_name,name,team1,o_name, team2)
    

def web_scraping_in_action():
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    while True:
        page = urllib.request.urlopen(score_page)
        soup = BeautifulSoup(page, "html.parser")
        result = soup.find_all("description")
        return result

if __name__ == '__main__':
    app.run()
    
    