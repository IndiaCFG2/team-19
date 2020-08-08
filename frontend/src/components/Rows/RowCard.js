import React, { Component } from 'react'
import './RowCard.css'
import ArrowUpwardRoundedIcon from '@material-ui/icons/ArrowUpwardRounded';
import ArrowDownwardRoundedIcon from '@material-ui/icons/ArrowDownwardRounded';
import { IconButton } from '@material-ui/core';


export default class RowCard extends Component {

    constructor(props){
        super(props);

        this.state = {
            id: props.key,
            title: props.card_data.title,
            name: props.card_data.name,
            upvotes: props.card_data.upvotes,
            downvotes: props.card_data.downvotes,
            text: props.card_data.text
        }
    }


    render() {
        return (
        <div className = "RowCard">
            <div className = "RowCard__title">
                {this.state.title}
            </div>
            <div className = "RowCard__text">
                {this.state.text}  
            </div>

            <div className = "RowCard__name">
                {this.state.name}  
            </div>

            <div className = "RowCard__bottom">
                <div className = "RowCard__bottom__content">
                    <IconButton style = {{marginTop: "-7px"}}>
                        <ArrowUpwardRoundedIcon />
                    </IconButton>
                    {this.state.upvotes}
                </div>

                <div className = "RowCard__bottom__content">
                    <IconButton style = {{marginTop: "-7px"}}>
                        <ArrowDownwardRoundedIcon />
                    </IconButton>
                    {this.state.downvotes}
                </div>
            </div>
        </div>
        )
    }
}
