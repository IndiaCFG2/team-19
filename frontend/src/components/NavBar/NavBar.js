import React, {useState} from 'react'
import "./NavBar.css"
import {Link} from 'react-router-dom'
import NavLogo from '../../assets/navlogo.png'

function NavBar() {
    return (
        <div className = "NavBar">
            <div className = "NavBar__left">
                <Link to = "/admin_login" >
                    <img className = "NavBar__logo" 
                    src = {NavLogo} />
                </Link>
            </div>
            
            <div className = "NavBar__right">
                <div className = "NavBar__right__content">
                    <span className = "NavBar__right__option__1"> Hello, Anonymous</span>
                    <Link to = "private_feedback">
                        <span className = "NavBar__right__option__2"> Private Feedback </span>
                    </Link>
                </div>

                <div className = "NavBar__right__content">
                    <span className = "NavBar__right__option__1"> Hello,  </span>
                    <Link to = "submit_feedback">
                        <span className = "NavBar__right__option__2"> Submit Feedback </span>
                    </Link>
                    
                </div>

                <div className = "NavBar__right__content">
                
                    <span className = "NavBar__right__option__1"> Admin </span>
                    <Link to = "admin_login">
                        <span className = "NavBar__right__option__2"> Login </span>
                    </Link>
                </div>
            </div>
        </div>
    )
}

export default NavBar
