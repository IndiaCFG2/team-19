import React, { Component } from 'react';
import Doc from '../PDF/DocService';
import PdfContainer from '../PDF/PdfContainer';
import Chart from './Chart';
import NavBar from '../NavBar/NavBar';
import axios from 'axios'


class Graph extends Component {
  constructor(){
    super();
    this.state = {
      chartData:{},
      feedBackForms: [],
      finanMin: 0,
      healMin: 0,
      agriMin: 0,
      defMin: 0,
      envirMin:0,
      eduMin: 0
    }
  }

  componentDidMount(){
    axios.get("/feedback",{
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      }
    })
    .then(response => {
      console.log("Response from API")
      console.log(response.data)
        this.setState({
          feedBackForms: response.data
        })

        this.genearateFrequency();

        this.setState({
          chartData:{
            labels: ['Health', 'Defence', 'Agriculture', 'Education', 'Environment', 'Transport'],
            datasets:[
              {
                label:'Feedbacks',
                data:[
                  this.state.finanMin,
                  this.state.healMin,
                  this.state.agriMin,
                  this.state.defMin,
                  this.state.envirMin,
                  this.state.eduMin
                ],
                backgroundColor:[
                  'rgba(255, 99, 132, 0.6)',
                  'rgba(54, 162, 235, 0.6)',
                  'rgba(255, 206, 86, 0.6)',
                  'rgba(75, 192, 192, 0.6)',
                  'rgba(153, 102, 255, 0.6)',
                  'rgba(255, 159, 64, 0.6)',
                  'rgba(255, 99, 132, 0.6)'
                ]
              }
            ]
          }
        });
    
        
    })
    .catch(function(error){
      console.log(error)
    })
    
  }

  genearateFrequency(){
      this.state.feedBackForms.map(res => {
        const m_assigned = res.ministry_assigned;
        if(m_assigned == "1"){
            this.state.finanMin = this.state.finanMin + 1
        }else if(m_assigned == "2"){
            this.state.healMin= this.state.healMin + 1
        }else if(m_assigned == "3"){
            this.state.agriMin = this.state.agriMin + 1
        }else if(m_assigned == "4"){
            this.state.defMin= this.state.defMin + 1
        }else if(m_assigned == "5"){
            this.state.envirMin= this.state.envirMin + 1
        }else{
            this.state.eduMin= this.state.eduMin + 1
        }
      })
  }

  // getChartData(){
  //   // Ajax calls here
  //   this.setState({
  //     chartData:{
  //       labels: ['Health', 'Defence', 'Agriculture', 'Education', 'Environment', 'Transport'],
  //       datasets:[
  //         {
  //           label:'Feedbacks',
  //           data:[
  //             617594,
  //             181045,
  //             153060,
  //             106519,
  //             105162,
  //             95072
  //           ],
  //           backgroundColor:[
  //             'rgba(255, 99, 132, 0.6)',
  //             'rgba(54, 162, 235, 0.6)',
  //             'rgba(255, 206, 86, 0.6)',
  //             'rgba(75, 192, 192, 0.6)',
  //             'rgba(153, 102, 255, 0.6)',
  //             'rgba(255, 159, 64, 0.6)',
  //             'rgba(255, 99, 132, 0.6)'
  //           ]
  //         }
  //       ]
  //     }
  //   });
  // }

  createPdf = (html) => Doc.createPdf(html);
  render() {
    // this.genearateFrequency();
    console.log("Hi Graph")
    console.log(this.state.finanMin)
    console.log(this.state.feedBackForms)
    console.log(this.state.chartData)

    // this.getChartData();
    return (
      <div className="App">
        <NavBar></NavBar>
        <div className="App-header">
          <h2 style={{ paddingTop: "40px"}}>Feedback Analytics</h2>
        </div>
        <PdfContainer createPdf={this.createPdf}>
        <Chart chartData={this.state.chartData} location="" legendPosition="bottom"/>
        </PdfContainer>
      </div>
    );
  }
}

export default Graph;