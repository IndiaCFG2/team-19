import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';
import './App.css';
import DashBoard from './components/DashBoard/Dashboard'
import CitizenFeedback from './components/FeedBack and Login/CitizenFeedback'
import PrivateFeedback from './components/FeedBack and Login/PrivateFeedBack'
import ErrorPage from './components/ErrorPage/ErrorPage'
import LogOut from './components/Logout/logout'
import CitizenAccessPage from './components/FeedBack and Login/CitizenAccessPage';
import Do_register from './components/Register_or_login/Do_register'
import Admin_register from './components/Admin_Login/Admin_register'
import Graph from './components/DrawGraph/Graph'

class App extends Component {
  render(){
    return (
     <>
      <Router>
        <Switch>
          <Route exact path = "/" component = {DashBoard} />                              // Base Landing Page
          <Route exact path = "/admin_login" component = {Admin_register} />              // Shift to Admin Login Page
          <Route exact path = "/submit_feedback" component = {CitizenFeedback} />         // Submit FeedBack
          <Route exact path = "/citizen_access_page" component = {CitizenAccessPage}/>    // Citizen Lands on this Page
          <Route exact path = "/private_feedback" component = {PrivateFeedback} />        // Submit Private FeedBack
          <Route exact path = "/user_login" component = {Do_register} />
          <Route exact path = "/graph" component = {Graph} />
          <Route exact path = "/logout" component = {LogOut} />                           // LogOut
          <Route path = "/" component = {ErrorPage} />                                    // Default Error Page
         </Switch> 
      </Router>
     </>
    );
  }
}

export default App;
