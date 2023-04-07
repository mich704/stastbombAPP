import React from 'react'
import { useParams } from "react-router-dom"

export default function MatchInfo() {
    let params = useParams()
    
  return (
    <div>
      {params.id}
    </div>
  )
}
