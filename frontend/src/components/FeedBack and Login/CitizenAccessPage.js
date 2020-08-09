import React, { Component } from 'react'
import NavBar from '../NavBar/NavBar'
import Banner from '../Banner/Banner'
import Row from '../Rows/Row'
import axios from 'axios'

const id = 2
export default class CitizenAccessPage extends Component {

  constructor(props){
      super(props);

      this.state = {
        feedbackForm:[],
        trending_feeds : [
          // {   id: 1,
          //   title: "Hello",
          //   text : "JPdsaudgsadjhaskdhskhdshdshdklhdddddddddddddddddddddddddddddddddddddddddddddjjjjjjjjjjjjjjjjjjjjjdddddddddddddddddddddddddddddddddjjjjjjjjjjjjjjdddddddddkshdklshdkslhdkl Morgans we are coming",
          //   upvotes: 10,
          //   downvotes: 5,
          //   name: "Team - 19",
          //   ministry_assigned: 1,
          //   userSentiment: "-1",              // User Sentiment regarding the policy (Yes, No, Neutral)
          //   rating: "5",                      // Rating for the Policy
          //   policyDecision: "0",               // Decision regarding Policy
          //   language: "0"
          // },
          // {
          //   id: 2,
          //   title: "Hello",
          //   text : "JP Morgans we are coming",
          //   upvotes: 10,
          //   downvotes: 5,
          //   name: "Team - 19",
          //   ministry_assigned: 1,
          //   userSentiment: "-1",              // User Sentiment regarding the policy (Yes, No, Neutral)
          //   rating: "5",                      // Rating for the Policy
          //   policyDecision: "0",               // Decision regarding Policy
          //   language: "0"
          // }
        ],


        personal_feeds : [
          // {
          //   id: 3,
          //   title: "Hello",
          //   text : "JP Morgans we are coming",
          //   upvotes: 10,
          //   downvotes: 5,
          //   name: "Team - 19",
          //   ministry_assigned: 1,
          //   userSentiment: "-1",              // User Sentiment regarding the policy (Yes, No, Neutral)
          //   rating: "5",                      // Rating for the Policy
          //   policyDecision: "0",               // Decision regarding Policy,
          //   language: "0"
            
          // },
          // {
          //   id: 4,
          //   title: "Hello",
          //   text : "JP Morgans we are coming",
          //   upvotes: 10,
          //   downvotes: 5,
          //   name: "Team - 19",
          //   ministry_assigned: 1,
          //   userSentiment: "-1",              // User Sentiment regarding the policy (Yes, No, Neutral)
          //   rating: "5",                      // Rating for the Policy
          //   policyDecision: "0",               // Decision regarding Policy
          //   language: "0"
          // }
        ]
      }
  }

  setFeedBackForms(){
      this.state.feedbackForm.map(res => {
           if(res.upvotes >= 2){
            this.state.trending_feeds= [...this.state.trending_feeds, res]
           }
               
           if(res.id === id)
              this.state.personal_feeds= [...this.state.personal_feeds, res]
      })
  }

  componentDidMount(){
    axios.get("/feedback",{
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      }
    })
    .then(response => {
      console.log("Response from API")
      console.log(response.data)
        this.setState({
          feedbackForm: response.data
        })
        
    })
    .catch(function(error){
      console.log(error)
    })
}



  render() {
    this.setFeedBackForms()
    console.log("Personal")
    console.log(this.state.personal_feeds)
    return (
      <>
        <NavBar />
        <Banner />
        <Row title = "Trending Feeds" feeds = {this.state.trending_feeds}/>
        <Row title = "Your Submitted Feeds" feeds = {this.state.personal_feeds} />
      </>
    )
  }
}
