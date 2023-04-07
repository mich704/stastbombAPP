import React, {Component} from "react";
import { createRoot } from 'react-dom/client';
import CompetitionForm from "./components/CompetitionForm";
import {  BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import MatchInfo from "./components/MatchInfo";

const App = props =>{
    return(
        <Router>
            <Routes>
                <Route path="/" element={<CompetitionForm></CompetitionForm>}></Route>
                <Route path="/matches/:id" element={<MatchInfo />}></Route>
            </Routes>
        </Router>
        
    )  
}



export default App
