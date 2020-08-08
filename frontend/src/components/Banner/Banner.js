import React, {useState, useEffect} from 'react';
import './Banner.css'

export default function Banner() {
    const imageUrl = "https://wallpapercave.com/wp/s0H9E3Z.jpg"
  return (
    <header className = "Banner"
        style = {{
            backgroundSize: "cover",
            backgroundImage: `url(
                ${imageUrl}
            )`,
            backgroundPosition: "center center"
        }}
    >
        <div className = "Banner__contents">
            <h1 className = "Banner__title">
                Title
            </h1>
            
            <h1 className = "Banner__description">
                Description
            </h1>
        {/* title */}
        {/* div */}
        {/* description */}
        <div className = "Banner__fadeBottom" />
        </div>
        
    </header>
  );
}
