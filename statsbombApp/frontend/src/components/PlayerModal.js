import React, { useState } from 'react';
import Lightbox from "react-image-lightbox";
import "react-image-lightbox/style.css";
import {Button} from '@material-ui/core/';

export default function PlayerModal(props) {
const [isOpen, setIsOpen] = useState(false);
  return (
    <React.Fragment>
        <Button variant="contained" color="primary" onClick={() => setIsOpen(true)}>Preview Passmap</Button>
                {isOpen && <Lightbox
                  mainSrc={`/media/match_${props.id}/passmaps/player_${props.player_id}.png`}
                  onCloseRequest={() => setIsOpen(false)}
                />}
    </React.Fragment>
  )
}
