import React, { Component } from 'react'
import { recomposeColor } from '@material-ui/core';
import './Row.css';
import RowCard from './RowCard'

export default class Row extends Component {
    constructor(props){
        super(props);

        this.state = {
            title : props.title,
            tile_data: [
                {   id: 1,
                    title: "Hello",
                    text : "JPdsaudgsadjhaskdhskhdshdshdklhdkshdklshdkslhdkl Morgans we are coming",
                    upvotes: 10 ,
                    downvotes: 5,
                    name: "Team - 19",
                    ministry_assigned: 1,
                },
                {
                  id: 2,
                  title: "Hello",
                  text : "JP Morgans we are coming",
                  upvotes: 10 ,
                  downvotes: 5,
                  name: "Team - 19",
                  ministry_assigned: 1,
                },
                {
                  id: 3,
                  title: "Hello",
                  text : "JP Morgans we are coming",
                  upvotes: 10 ,
                  downvotes: 5,
                  name: "Team - 19",
                  ministry_assigned: 1,
                }
            ]
        }  
    }

    // <img key = {tileData.id} 
    //                    className = {`Row__img ${isLargeRow && "Row__img__large"}`} 
    //                    src = {`${base_url}${isLargeRow ? movie.poster_path : movie.backdrop_path}`} 
    //                    alt = {movie.name}
    //                    onClick = {() => handleClick(movie)} />

  render() {
    return (
      <>
        <div className = "Row">
            <h2>{this.state.title}</h2>
            <div className = "Row__cards">
               {
                   this.state.tile_data.map(tileData => {
                       return <RowCard key = {tileData.id} card_data = {tileData} />
                   })
                
               }
           </div>
           {/* container -> posters */ }
        </div>
      </>
    )
  }
}
