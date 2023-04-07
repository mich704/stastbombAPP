import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {Button} from '@material-ui/core/';



const Match = (props) => {

  const fetchMatchData = (match_id) => () =>{
    console.log('match ', match_id)
  }
  
  return (
        <TableBody>
            <TableRow
              key={props.match_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell align="right">{props.home_team}</TableCell>
              <TableCell align="right">{props.home_score}</TableCell>
              <TableCell align="right">{props.away_score}</TableCell>
              <TableCell align="right">{props.away_team}</TableCell>
              <TableCell align="right">
                  <Button variant="contained" size="small" href={`/matches/${props.match_id}`} onClick={fetchMatchData(props.match_id)}>
                    Match Info
                  </Button>
              </TableCell>
            </TableRow>
        </TableBody>
  )
}

export default Match
