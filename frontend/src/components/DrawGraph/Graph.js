import React, { Component } from 'react';
import Doc from '../PDF/DocService';
import PdfContainer from '../PDF/PdfContainer';
import Chart from './Chart';
import NavBar from '../NavBar/NavBar';

class Graph extends Component {
  constructor(){
    super();
    this.state = {
      chartData:{}
    }
  }

  componentWillMount(){
    this.getChartData();
  }

  getChartData(){
    // Ajax calls here
    this.setState({
      chartData:{
        labels: ['Health', 'Defence', 'Agriculture', 'Education', 'Environment', 'Transport'],
        datasets:[
          {
            label:'Feedbacks',
            data:[
              617594,
              181045,
              153060,
              106519,
              105162,
              95072
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
  }
  createPdf = (html) => Doc.createPdf(html);
  render() {
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