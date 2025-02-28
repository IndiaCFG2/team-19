import React, { Component } from 'react'
import './PrivateFeedBack.css'
import SendIcon from '@material-ui/icons/Send';
import NavBar from '../NavBar/NavBar'
import axios from 'axios';


export default class PrivateFeedBack extends Component {
  constructor(props){
    super(props);

    this.state  = {
        id: 0,                            // User Id      This will be 0 always, we will be dealing with this at backend
        email: '',                        // User Email   This will be null always as we are dealing with anonymuos user
        title: '',                        // Policy Name
        name: "Anonymuos",                // User Name
        text: "",                         // FeedBack
        upvotes: 0,                       // Upvotes
        downvotes:0,                      // Downvotes
        ministry_assigned: "1",           // Ministry Assigned
        userSentiment: "-1",              // User Sentiment regarding the policy (Yes = 1, No = -1, Neutral = 0)
        rating: "5",                      // Rating for the Policy
        policy: "0",              // Decision regarding Policy    0-> scrap it,, 1-> Can be implemented better
        language: "0",                     // Language Hindi / English
        userPincode: 0,
        userAge: 0,

      }

    this.onChangeUserSentiment = this.onChangeUserSentiment.bind(this)
    this.onChangeRating = this.onChangeRating.bind(this)
    this.onChangePolicyDecision = this.onChangePolicyDecision.bind(this)
    this.onChangeText = this.onChangeText.bind(this);
    this.onChangeMinistryAssigned = this.onChangeMinistryAssigned.bind(this);
    this.onChangeTitle = this.onChangeTitle.bind(this)
    this.onChangeLanguage = this.onChangeLanguage.bind(this)
    this.onSubmit = this.onSubmit.bind(this);
  }

  onChangeLanguage(event){
    this.setState({
        language: event.target.value
    })
  }

  onChangeUserSentiment(event){
    this.setState({
        userSentiment: event.target.value
    })
  }

  onChangeRating(event){
    this.setState({
      rating: event.target.value
    })
  }

  onChangePolicyDecision(event){
    this.setState({
      policy: event.target.value
    })
  }

  onChangeText(event) {
    this.setState({
      text: event.target.value
    });
  }

  onChangeMinistryAssigned(event){
    this.setState({
      ministry_assigned: event.target.value
    })
  }

  onChangeTitle(event){
    this.setState({
      title: event.target.value
    })
  }

  onSubmit(event){
    event.preventDefault();
     alert("FeedBack Submitted Successfully")

     const user_feedback = {
          id: this.state.id,
          email: this.state.email,
          text: this.state.text,
          title: this.state.title,
          name: this.state.name,
          upvotes: this.state.upvotes,
          downvotes: this.state.downvotes,
          ministry_assigned: this.state.ministry_assigned,
          userSentiment: this.state.userSentiment,
          rating: this.state.rating,
          policy: this.state.policy,
          language: this.state.language,
          userPincode: this.state.userPincode,
          userAge: this.state.userAge
     }

     console.log("API Called")
     axios.post('/feedback', user_feedback) 
      .then(res => console.log(res.data))
      .catch(function(error){
        console.log(error)
      },
      this.props.history.push('/'))

  
     console.log(user_feedback)
     this.setState({
        id: 0,
        email: '',
        text: '',
        title: '',
        name: "Anonymous",
        upvotes: 0,
        downvotes: 0,
        ministry_assigned: "1",
        userSentiment: "-1",
        rating: "5",
        policy: "0"
     })
  }



  render() {
    return (
      <>
      <NavBar />
      <div className = "PrivateFeedBack">
        <form onSubmit = {this.onSubmit}>

          {/* Add Title Field */}

          <div className = 'form-group'>
            <label>Policy Title :</label>
            <input type = "text" 
              className = "form-control"
              value = {this.state.title}
              onChange = {this.onChangeTitle}
            />
          </div>
          
          {/* Enter Your FeedBack here */}

          <div className = 'form-group'>
            <label>Enter Your Feedback here :</label>
            <textarea type = "text" 
              placeholder = "Enter"
              className = "form-control"
              value = {this.state.text}
              onChange = {this.onChangeText}
              style = {{height: "150px", marginTop: "10px", resize: "none"}}
            />
          </div>

          {/* Language Selected by the user */}

          <div className = 'form-group'>
                <label>Please select the Language :</label>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "LanguageSelectedByUser"
                      id = "hindi"
                      value = "0"
                      checked = {this.state.language === '0'}
                      onChange = {this.onChangeLanguage}
                  />

                  <label className = "form-check-label">Hindi</label>
                </div>


                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "LanguageSelectedByUser"
                      id = "english"
                      value = "1"
                      checked = {this.state.language === '1'}
                      onChange = {this.onChangeLanguage}
                  />

                  <label className = "form-check-label">English</label>
                </div>
          </div>

          {/* Are You Happy with this Policy */}

          <div className = 'form-group'>
                <label>Are You Happy with this Policy :</label>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "userSentiment"
                      id = "Positive"
                      value = "1"
                      checked = {this.state.userSentiment === '1'}
                      onChange = {this.onChangeUserSentiment}
                  />

                  <label className = "form-check-label">Yes</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "userSentiment"
                      id = "Negative"
                      value = "-1"
                      checked = {this.state.userSentiment === '-1'}
                      onChange = {this.onChangeUserSentiment}
                  />

                  <label className = "form-check-label">No</label>
                </div>
                <br />
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "userSentiment"
                      id = "Neutral"
                      value = "0"
                      checked = {this.state.userSentiment === '0'}
                      onChange = {this.onChangeUserSentiment}
                  />

                  <label className = "form-check-label">Neutral</label>
                </div>

            </div> 

            {/* What do you feel about this policy */}

            <div className = 'form-group'>
                <label>What do you feel about this policy :</label>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserFeelingAboutPolicy"
                      id = "ScrapIt"
                      value = "0"
                      checked = {this.state.policy === '0'}
                      onChange = {this.onChangePolicyDecision}
                  />

                  <label className = "form-check-label">Scrap It !!!</label>
                </div>
                <br/>


                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserFeelingAboutPolicy"
                      id = "CanBeImplementedBetter"
                      value = "1"
                      checked = {this.state.policy === '1'}
                      onChange = {this.onChangePolicyDecision}
                  />

                  <label className = "form-check-label">Can Be Implemented Better</label>
                </div>
          </div>

          {/* Ministry Assigning Your Feedback to */}

          <div className = 'form-group'>
                <label>Ministry Assigning Your FeedBack to :</label>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityLow"
                      value = "1"
                      checked = {this.state.ministry_assigned === '1'}
                      onChange = {this.onChangeMinistryAssigned}
                  />

                  <label className = "form-check-label">Financial Ministry</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityMedium"
                      value = "2"
                      checked = {this.state.ministry_assigned === '2'}
                      onChange = {this.onChangeMinistryAssigned}
                  />

                  <label className = "form-check-label">Health Ministry</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityHigh"
                      value = "3"
                      checked = {this.state.ministry_assigned === '3'}
                      onChange = {this.onChangeMinistryAssigned}
                  />
                  <label className = "form-check-label">Agricultural Ministry</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityHigh"
                      value = "4"
                      checked = {this.state.ministry_assigned === '4'}
                      onChange = {this.onChangeMinistryAssigned}
                  />
                  <label className = "form-check-label">Defence Ministry</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityHigh"
                      value = "5"
                      checked = {this.state.ministry_assigned === '5'}
                      onChange = {this.onChangeMinistryAssigned}
                  />
                  <label className = "form-check-label">Environmental Ministry</label>
                </div>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "priorityOptions"
                      id = "priorityHigh"
                      value = "6"
                      checked = {this.state.ministry_assigned === '6'}
                      onChange = {this.onChangeMinistryAssigned}
                  />
                  <label className = "form-check-label">Education Ministry</label>
                </div>
          </div>

          {/* Policy Rating */}

          <div className = 'form-group'>
                <label>Rating :</label>
                <br/>
                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserRating"
                      id = "rating_1"
                      value = "1"
                      checked = {this.state.rating === '1'}
                      onChange = {this.onChangeRating}
                  />
                </div>


                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserRating"
                      id = "rating_2"
                      value = "2"
                      checked = {this.state.rating === '2'}
                      onChange = {this.onChangeRating}
                  />
                </div>

                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserRating"
                      id = "rating_3"
                      value = "3"
                      checked = {this.state.rating === '3'}
                      onChange = {this.onChangeRating}
                  />

                  
                </div>

                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserRating"
                      id = "rating_4"
                      value = "4"
                      checked = {this.state.rating === '4'}
                      onChange = {this.onChangeRating}
                  />

                  
                </div>

                <div className = "form-check form-check-inline">
                  <input className = "form-check-input"
                      type = "radio"
                      name = "UserRating"
                      id = "rating_5"
                      value = "5"
                      checked = {this.state.rating === '5'}
                      onChange = {this.onChangeRating}
                  />
                </div>
          </div>



          {/* Submit Button */}
          <div className = 'form-group'>
            <input 
              type = "submit" 
              value = "Submit Your Feedback" 
              className = "btn btn-primary"
              disabled = {this.state.text && this.state.title? false : true}
              style = {{fontSize : "15px"}} 
            /> 
          </div>
        </form>   
      </div>
      </>
    )
  }
}
