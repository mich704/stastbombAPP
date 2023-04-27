import React, { useState, useEffect } from 'react';
import { useParams } from "react-router-dom";
import Lightbox from "react-image-lightbox";
import "react-image-lightbox/style.css";
import {Button} from '@material-ui/core/';

export default function PlayerModal(props) {
  let params = useParams();
  const [passmap, setPassmap] = useState({});
  useEffect(function effectFunction(){
    async function fetchPlayerMatchRaportInfo(){
      const data = await (
        await fetch(
          `http://127.0.0.1:8000/api/matches/${params.id}/${props.player_id}/passmap`
        )
      ).json();
      
      setPassmap((Object.keys(data).length > 0) ? data: null); 
      console.log('data', data, Object.keys(data))
    }
    fetchPlayerMatchRaportInfo()
  }, []);


  const [isOpen, setIsOpen] = useState(false);
  return (
    <>
        {passmap && 
          <>
            <li>{props.player}</li>
              <Button variant="contained" color="primary" onClick={() => setIsOpen(true)}>Preview Passmap</Button>
          </>
        }

        {isOpen && passmap  && 
          <Lightbox
            mainSrc={`/media/match_${props.id}/passmaps/player_${props.player_id}.png`}
            onCloseRequest={() => setIsOpen(false)}
          />
        }
                  
    </>
  )
}
