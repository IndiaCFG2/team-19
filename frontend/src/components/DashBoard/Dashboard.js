import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import NavBar from '../NavBar/NavBar'
import Banner from '../Banner/Banner'
import Row from '../Rows/Row'
import axios from 'axios'

const baseUrl = "https://civis19.herokuapp.com/";
class DashBoard extends Component {
  

  constructor(props){
    super(props);

    this.setFeedBackFormsforMinistries = this.setFeedBackFormsforMinistries.bind(this)

    this.state = {
      feedBackForms: [],
      financeMinistry: [],
      healthMinistry: [],
      agriculturalMinistry: [],
      defenceMinistry: [],
      environmentalMinistry:[],
      educationMinistry: []      
    }
  }

  setFeedBackFormsforMinistries(){
    console.log("FEEDSJKAJSKL")
      this.state.feedBackForms.map(res => {
        const m_assigned = res.ministry_assigned;
        if(m_assigned == "1"){
            this.state.financeMinistry = [...this.state.financeMinistry, res]
        }else if(m_assigned == "2"){
            this.state.healthMinistry= [...this.state.healthMinistry, res]
        }else if(m_assigned == "3"){
            this.state.agriculturalMinistry= [...this.state.agriculturalMinistry, res]
        }else if(m_assigned == "4"){
            this.state.defenceMinistry= [...this.state.defenceMinistry, res]
        }else if(m_assigned == "5"){
            this.state.environmentalMinistry= [...this.state.environmentalMinistry, res]
        }else{
            this.state.educationMinistry= [...this.state.educationMinistry, res]
        }
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
            feedBackForms: response.data
        })
          
      })
      .catch(function(error){
        console.log(error)
      },
      this.props.history.push('/'))
  }

  render(){
    console.log("FeedBack Forms")
    console.log(this.state.feedBackForms)
    console.log(this.state.financeMinistry)

    return (
     <> 
        <NavBar />
        <Banner />
        
        
        <Row title = "Financial Ministry" feeds = {this.state.financeMinistry}/>
        <Row title = "Health Ministry" feeds = {this.state.healthMinistry}/>
        <Row title = "Agricultural Ministry" feeds = {this.state.agriculturalMinistry} />
        <Row title = "Defence Ministry" feeds = {this.state.defenceMinistry} />
        <Row title = "Environmental Ministry"  feeds = {this.state.environmentalMinistry}/>
        <Row title = "Education Ministry" feeds = {this.state.educationMinistry}/>
     </>
    );
  }
}

export default DashBoard;
