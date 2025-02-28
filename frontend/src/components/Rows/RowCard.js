import React, { Component } from 'react'
import './RowCard.css'
import ArrowUpwardRoundedIcon from '@material-ui/icons/ArrowUpwardRounded';
import ArrowDownwardRoundedIcon from '@material-ui/icons/ArrowDownwardRounded';
import { IconButton } from '@material-ui/core';


export default class RowCard extends Component {

    constructor(props){
        super(props);

        this.state = {
            id: props.card_data.id,                                // Id assigned to User
            title: props.card_data.title,                          // Policy Name
            name: props.card_data.name,                            // User Name
            upvotes: props.card_data.upvotes,                      // Upvotes
            downvotes: props.card_data.downvotes,                  // Downvotes
            text: props.card_data.text,                            // FeedBack
            ministry_assigned:"1",                                 // Ministry Assigned
            userSentiment:"-1",                                    // User Sentiment regarding the policy (Yes, No, Neutral)
            rating: "5",                                           // Rating for the Policy
            policyDecision: "0",                                   // Decision regarding the policy
        }
    }

    upVote = (id) => {
        alert("UpVoted")
        console.log(id, this.state.upvotes)
        this.setState({
            upvotes : this.state.upvotes + 1
        })
    }

    downVote = (id) => {
        alert("DownVoted")
        console.log(id, this.state.upvotes)
        this.setState({
            downvotes : this.state.downvotes - 1
        })
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
                    <IconButton onClick = {() => {this.upVote(this.state.id)}} 
                        className = "RowCard__bottom__content__Icon_1"
                    >
                        <ArrowUpwardRoundedIcon  />
                    </IconButton>
                    {this.state.upvotes}
                </div>

                <div className = "RowCard__bottom__content">
                    <IconButton onClick = {() => {this.downVote(this.state.id)}} 
                        className = "RowCard__bottom__content__Icon_2"
                    >
                        <ArrowDownwardRoundedIcon  />
                    </IconButton>
                    {this.state.downvotes}
                </div>
            </div>
        </div>
        )
    }
}
