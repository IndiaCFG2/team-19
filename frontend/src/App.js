import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.min.css";
import {BrowserRouter as Router, Route, Link, Switch} from 'react-router-dom';
import './App.css';
import DashBoard from './components/DashBoard/Dashboard'
import AdminLogin from './components/FeedBack/AdminLogin'
import CitizenLogin from './components/FeedBack/CitizenLogin'
import PrivateFeedback from './components/FeedBack/PrivateFeedBack'
import ErrorPage from './components/ErrorPage/ErrorPage'
import LogOut from './components/Logout/logout'

class App extends Component {
  render(){
    return (
     <>
      <Router>
        <Switch>
          <Route exact path = "/dashboard" component = {DashBoard} />
          <Route exact path = "/admin_login" component = {AdminLogin} />
          <Route exact path = "/submit_feedback" component = {CitizenLogin} />
          <Route exact path = "/private_feedback" component = {PrivateFeedback} />
          <Route exact path = "/logout" component = {LogOut} />
          <Route path = "/" component = {ErrorPage} />
         </Switch> 
      </Router>
     </>
    );
  }
}

export default App;
