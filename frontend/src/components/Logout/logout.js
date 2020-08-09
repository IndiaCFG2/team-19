import React, { Component } from 'react'
import {Link, Redirect} from 'react-router-dom';
import NavBar from '../NavBar/NavBar'

const logout = () => {

    localStorage.clear()
    return(
        <>
        <NavBar/>
            <Redirect to = '/'/>                           // Redirect To Dashboard
        </>
    )
}

export default logout