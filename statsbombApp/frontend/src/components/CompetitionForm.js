import React, { useEffect, useState } from "react";
import {Button, TextField, FormControl, Select, InputLabel, MenuItem, Grid   } from '@material-ui/core/';

import Matches from "./Matches";
import matchesStyles from './Matches.module.css';


const CompetitionForm = props =>{

    const [competitionName, setCompetitionName] = useState('')
    const [competitionSeason, setCompetitionSeason] = useState('')
    const [competitions, setCompetitions] = useState([])
    const [availableCompetitions, setAvailableCompetitions] = useState([])
    const [matches, setMatches] = useState([])

    const fetchCompetitions = async()=>{
        let response = await fetch("http://127.0.0.1:8000/api/competitions");
        let data = await response.json();
       
        setCompetitions(data)
        setAvailableCompetitions(data)
        console.log('FETCC')
    }

    useEffect(()=>{
        fetchCompetitions()  
    },[])    

    const competitionNameChangeHandler = (event) => {
        setCompetitionName(event.target.value)
        let avComps = []
        for(let i = 0 ; i< competitions.length ; i++){
            //console.log(competitions[i])
            if(competitions[i].competition_name === event.target.value){
                avComps.push(competitions[i])
            }
        }
        //console.log(avComps)
        setAvailableCompetitions(avComps)
       
        //const avSeasons = availableSeasons.map(season => )
    }

    const seasonClickHandler = event =>{
        //setAvailableCompetitions(competitions)
    }

    const nameClickHandler = event =>{
        //setAvailableCompetitions(competitions)
    }

    const competitionSeasonChangeHandler = (event) => {
        setCompetitionSeason(event.target.value)
        let avComps = []
        for(let i = 0 ; i< competitions.length ; i++){
            //console.log(competitions[i])
            if(competitions[i].season_name === event.target.value){
                avComps.push(competitions[i])
            }
        }
        setAvailableCompetitions(avComps)
      
    }

    
    const submitHandler = event =>{
       
        event.preventDefault();

        let formCompetition = competitions.filter(competition => (
            competition.season_name === competitionSeason && competition.competition_name === competitionName
        ))[0]
        
        const fetchMatches = async()=>{
            console.log(formCompetition.pk)
            let response = await fetch(`http://127.0.0.1:8000/api/competitions/${formCompetition.pk}/matches`);
            let matchesData = await response.json();
            console.log(matchesData)

            setMatches(matchesData)
        }
        
        fetchMatches()
        //setAvailableCompetitions(competitions)
        setCompetitionName('')
        setCompetitionSeason('')
    }

    return(
        <>
            
            <form onSubmit={submitHandler}>
                <Grid container direction="row" justifyContent="flex-start" alignItems="flex-start" spacing={1}>
                    <Grid container >
                        <Grid item sm={3}>
                            <FormControl style={{minWidth: 200}}>
                                <InputLabel  id="competition-name"  label="Name">Competition Name</InputLabel>
                                <Select
                                    id="competition-name"  
                                    label="Competition Name"
                                    variant="outlined"
                                    value={competitionName}
                                    onChange={competitionNameChangeHandler}
                                    onClick={nameClickHandler}
                                    required>
                                        <MenuItem value=""><em>----</em></MenuItem>
                                        {
                                            availableCompetitions.map(competition =>(
                                                <MenuItem 
                                                    key={competition.pk}
                                                    value={competition.competition_name}
                                                >
                                                    {competition.competition_name}
                                                </MenuItem >
                                            ))
                                        }
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item sm={3} width="auto">
                            <FormControl style={{minWidth: 200}}>
                                <InputLabel  id="competition-season"  label="Season">Competition Season</InputLabel>
                                <Select
                                    id="competition-season"  
                                    label="Season"
                                    variant="outlined"
                                    value={competitionSeason}
                                    onChange={competitionSeasonChangeHandler}
                                    onClick={seasonClickHandler}
                                    required>
                                        <MenuItem value=""><em>----</em></MenuItem>
                                    {
                                        availableCompetitions.map(competition =>(
                                            <MenuItem  
                                                key={competition.pk}  
                                                value={competition.season_name}
                                            >
                                                {competition.season_name}
                                            </MenuItem >
                                        ))
                                    }
                                </Select>
                            </FormControl>
                        </Grid>
                        
                        <Button variant="contained" color="primary" type="submit">
                            Submit
                        </Button>
                        
                        
                    </Grid>
                </Grid>
            </form>
            <br></br>
                <Matches matches={matches}/>
        </>
    ) 
}


export default CompetitionForm;
