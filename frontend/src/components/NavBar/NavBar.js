import React, {useState, useEffect} from 'react'
import "./NavBar.css"
import {Link} from 'react-router-dom'
import NavLogo from '../../assets/navlogo.png'



function NavBar() {
     
    const [userLoggedIn, setuserLoggedIn] = useState(true)                            //Initialising Variables
    const [adminLoggedIn, setadminLoggedIn] = useState(true)                          //Initialising Variables

    useEffect(() => {                                                                 // Used to SetUserLoginStatus
        {
            localStorage.getItem('userLogin') ?
            setuserLoggedIn(true)
            :
            setuserLoggedIn(false)
        }
      }, [])

    useEffect(() => {                                                                 //Used to SetAdminLoginStatus
        {
            localStorage.getItem('adminLogin') ?
            setadminLoggedIn(true)
            :
            setadminLoggedIn(false)
        }
    }, [])

    return (
        <div className = "NavBar">
            <div className = "NavBar__left">
                <Link to = "/" >
                    <img className = "NavBar__logo" 
                    src = {NavLogo} />
                </Link>
            </div>

            <div className = "NavBar__IVR">
                <div className = "NavBar__IVR__Message">
                    24 X 7 HelpLine
                </div>

                <div className = "NavBar__IVR__Call">
                    12054489824
                </div>

            </div>
            
            <div className = "NavBar__right">
                <div className = "NavBar__right__content">
                    <span className = "NavBar__right__option__1"> Hello, Anonymous</span>
                    <Link to = "/private_feedback">
                        <span className = "NavBar__right__option__2"> Private Feedback </span>
                    </Link>
                </div>

                <div className = "NavBar__right__content">
                    <span className = "NavBar__right__option__1"> Hello,  </span>
                    <Link to = "/submit_feedback">
                        <span className = "NavBar__right__option__2"> Submit Feedback </span>
                    </Link>
                    
                </div>

                <div className = "NavBar__right__content">
                    {
                        userLoggedIn ? 
                        <>
                            <span className = "NavBar__right__option__1"> User </span>
                             <Link to = "/logout">
                                <span className = "NavBar__right__option__2"> LogOut </span>
                            </Link>
                        </>

                        :

                        <>
                            <span className = "NavBar__right__option__1"> User </span>
                             <Link to = "/citizen_access_page">
                                <span className = "NavBar__right__option__2"> Login </span>
                            </Link>   
                        </>
                    }
                </div>


                <div className = "NavBar__right__content">
                    {
                        adminLoggedIn ?
                        <>
                            <span className = "NavBar__right__option__1"> AdminName </span>
                            <Link to = "/logout">
                                <span className = "NavBar__right__option__2"> LogOut </span>
                            </Link>
                        </>
                            :
                        <>
                            <span className = "NavBar__right__option__1"> Admin </span>
                                <Link to = "/graph">
                                    <span className = "NavBar__right__option__2"> Login </span>
                                </Link>
                        </>
                    }
                </div>
            </div>
        </div>
    )
}

export default NavBar
