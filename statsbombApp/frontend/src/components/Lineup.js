import React, { useState } from 'react';
import { useParams } from 'react-router-dom';


import PlayerModal from './PlayerModal';


export default function Lineup(props) {
  let params = useParams();
 

  return (
    <div >
        <h2>{props.team}</h2>
        
        <ul>
        {
            props.lineup.map(player =>(
              <React.Fragment key={player.player_id}>
                <li>{player.player}</li>
              
                

                <PlayerModal id = {params.id} player_id = {player.player_id} />
                
                
              </React.Fragment>
              
            ))
        }
        </ul>
    </div>

  )
}
