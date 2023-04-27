import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom"
import Lineup from "./Lineup";
import matchInfoStyles from './css/MatchInfo.module.css';



export default function MatchInfo() {
    let params = useParams()

    const [matchInfo, setMatchInfo] = useState([]);
    const [homeLineup, setHomeLineup] = useState([]);
    const [awayLineup, setAwayLineup] = useState([]);
      
        //{ "pk": null,
        // "match_id": null,
        // "competition": {},
        // "home_team": "",
        // "away_team":"",
        // "home_score": null,
        // "away_score": null,
        // "home_lineup": {},
        // "away_lineup": {}}

  useEffect(function effectFunction(){
    async function fetchMatchInfo(){
      const data = await (
        await fetch(
          `http://127.0.0.1:8000/api/matches/${params.id}/`
        )
      ).json();
      console.log('data', data)
      setAwayLineup(data.away_lineup.players)
      setHomeLineup(data.home_lineup.players)
      setMatchInfo(data)
    }
      fetchMatchInfo()
  }, []);
    
  return (
    <div className={matchInfoStyles.wrapper}>
      <div className={matchInfoStyles.team}>
        <Lineup team={matchInfo.home_team} lineup={homeLineup}/>  
      </div>      
      
      <div className={matchInfoStyles.team}>
        <Lineup team={matchInfo.away_team} lineup={awayLineup}/>
      </div>
      
    </div>
  );
}
