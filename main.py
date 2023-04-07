from statsbombpy import sb
import os.path 
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch

def drawPitch():
    fig1, ax = plt.subplots(figsize=(13.5,8))
    fig1.set_facecolor('#22312b')
    ax.patch.set_facecolor('#22312b')

    pitch = Pitch(pitch_type='statsbomb', orientation='horizontal', pitch_color='#22312b',  line_color='white',
                figsize=(16,11), constrained_layout=True, tight_layout=False)  # optional stripes
    pitch.draw(ax=ax)
    plt.gca().invert_yaxis()


def createPassmaps(players, path, events, teams):
    for p in players:
        passCoords = events[events['player']== p]
        
        if len(passCoords)>0:
            drawPitch()
            title = plt.title("{} vs. {}\n {} passmap: ".format(teams[0], teams[1], p),
                fontsize=12,
                pad='2.0',
                fontstyle='italic' )
            for (start_location, end_location, outcome) in zip(passCoords.location, passCoords.pass_end_location, passCoords.pass_outcome):
            
                if(isinstance(start_location, list)):
                    if outcome != 'Incomplete':
                        if(isinstance(end_location, list)):
                            plt.plot((start_location[0], end_location[0]),(start_location[1], end_location[1]), color = 'green')
                            plt.scatter(start_location[0], start_location[1], color='green')
                    else:
                        plt.plot((start_location[0], end_location[0]),(start_location[1], end_location[1]), color = 'red')
                        plt.scatter(start_location[0], start_location[1], color='red')
                    
        
            #plt.savefig(path+"/"+str(p))
            #print(path+"/"+str(p))
            plt.close()
        #print(p)
    #events.head(40)
#print(sb.competitions())


def main():
    plt.ioff()
    matches = sb.matches(competition_id=55, season_id=43)
    events = sb.events(match_id = 3794692)

    teams = list(set(events.team))
    print(teams)

    events = events[['player','type','location', 'pass_end_location', 'pass_outcome']]
    players = events['player'].unique()

    directory = teams[0]+"_"+teams[1]
    
    # Parent Directory path
    parent_dir = "Passmaps/"
    
    # Path
    path = os.path.join(parent_dir, directory)
    
    # Create the directory
    # 'GeeksForGeeks' in
    # '/home / User / Documents'
    if os.path.isdir(path) == False:
        os.mkdir(path)
    createPassmaps(players, path, events, teams)


if __name__ == '__main__': main()
