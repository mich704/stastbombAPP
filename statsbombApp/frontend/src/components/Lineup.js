import React from 'react'

export default function Lineup(props) {
  return (
    <div class="team">
        <h2>{props.team}</h2>
        <ul>
        {
            props.lineup.map(player =>(
              <li>{player.player}</li>
            ))
        }
        </ul>
    </div>

  )
}
