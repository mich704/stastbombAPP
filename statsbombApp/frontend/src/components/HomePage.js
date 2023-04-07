import React, {Component} from "react";
import CompetitionForm from "./CompetitionForm";
import {
    BrowserRouter as Router,
    Routes ,
    Link,
    Route,
    Redirect
} from 'react-router-dom';

const HomePage = props =>{
    return(
        <Router>
            <Routes>
               
                <Route path='competitionForm' element={<CompetitionForm/>}/>
            </Routes>
        </Router>   
    )
}

export default HomePage