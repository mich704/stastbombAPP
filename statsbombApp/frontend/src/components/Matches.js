import React from 'react'
import Match from "./Match";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';


export default function Matches(props) {
  return (
    <React.Fragment>
      {props.matches.length > 0 && <TableContainer component={Paper} style={{ width: "50%", alignContent:'self' }}>
        <Table  size="small" aria-label="a dense table" >
          <TableHead>
            <TableRow>
              <TableCell align="right">Home team</TableCell>
              <TableCell align="center">Home score</TableCell>
              <TableCell align="center">Away score</TableCell>
              <TableCell align="right">Away team</TableCell>
              <TableCell align="right"></TableCell>
            </TableRow>
          </TableHead>
          
            {  props.matches.map((match) => (
                  <Match
                      key={match.match_id}
                      match_id= {match.match_id}
                      home_team = {match.home_team}
                      home_score =  {match.home_score}
                      away_score = {match.away_score}
                      away_team = {match.away_team}
                  />
              ))
            }
        
        </Table>
      </TableContainer>
      }
        
    </React.Fragment>
  )
}
