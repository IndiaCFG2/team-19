import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';
import './App.css';
import DashBoard from './components/DashBoard/Dashboard'
import AdminLogin from './components/FeedBack and Login/AdminLogin'
import CitizenLogin from './components/FeedBack and Login/CitizenLogin'
import PrivateFeedback from './components/FeedBack and Login/PrivateFeedBack'
import ErrorPage from './components/ErrorPage/ErrorPage'
import LogOut from './components/Logout/logout'
import CitizenAccessPage from './components/FeedBack and Login/CitizenAccessPage';

class App extends Component {
  render(){
    return (
     <>
      <Router>
        <Switch>
          <Route exact path = "/" component = {DashBoard} />                              // Base Landing Page
          <Route exact path = "/admin_login" component = {AdminLogin} />                  // Shift to Admin Login Page
          <Route exact path = "/submit_feedback" component = {CitizenLogin} />            // Submit FeedBack
          <Route exact path = "/citizen_access_page" component = {CitizenAccessPage}/>    // Citizen Lands on this Page
          <Route exact path = "/private_feedback" component = {PrivateFeedback} />        // Submit Private FeedBack
          <Route exact path = "/logout" component = {LogOut} />                           // LogOut
          <Route path = "/" component = {ErrorPage} />                                    // Default Error Page
         </Switch> 
      </Router>
     </>
    );
  }
}

export default App;
