import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import NavBar from '../NavBar/NavBar'
import Banner from '../Banner/Banner'
import Row from '../Rows/Row'

class DashBoard extends Component {
  render(){
    return (
     <> 
        <NavBar />
        <Banner />
        <Row title = "Financial Ministry" />
        <Row title = "Health Ministry" />
        <Row title = "Agricultural Ministry" />
        <Row title = "Defence Ministry" />
        <Row title = "Environmental Ministry" />
        <Row title = "Education Ministry" />
     </>
    );
  }
}

export default DashBoard;
