import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import NavBar from '../NavBar/NavBar'
import Banner from '../Banner/Banner'
import Row from '../Rows/Row'

class App extends Component {
  render(){
    return (
     <> 
        <NavBar />
        <Banner />
        <Row title = "Ministry _ 1" />
        <Row title = "Ministry _ 2" />
        <Row title = "Ministry _ 3" />
        <Row title = "Ministry _ 4" />
        <Row title = "Ministry _ 5" />
     </>
    );
  }
}

export default App;
