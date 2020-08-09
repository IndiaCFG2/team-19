import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';


class Chart extends Component{
  constructor(props){
    super(props);

    this.state = {
      chartData:{
        labels: ['Health', 'Defence', 'Agriculture', 'Education', 'Environment', 'Transport'],
        datasets:[
          {
            label:'Feedbacks',
            data:[
              5,6,7,3,4
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
    }
  }

  static defaultProps = {
    displayTitle:true,
    displayLegend: true,
    legendPosition:'right',
    location:'City'
  }

  render(){
    console.log("Hello CHart")
    console.log(this.state.chartData)
    return (
      <div className="chart" style={{padding: "50px"}}>
        <Bar
          style={{ 
            paddingTop: "0",
            paddingLeft: "70",
            paddingRight: "70",
            paddingBottom: "70",}}
          data={this.state.chartData}
          options={{
            title:{
              display:this.props.displayTitle,
              text:'Total Feedbacks per Ministry '+this.props.location,
              fontSize:25
            },
            legend:{
              display:this.props.displayLegend,
              position:this.props.legendPosition
            }
          }}
        />

        <Line
          style={{ paddingTop: "70",
          paddingLeft: "70",
          paddingRight: "70",
          paddingBottom: "70",}}
          data={this.state.chartData}
          options={{
            title:{
              display:this.props.displayTitle,
              text:'Total Feedbacks per Ministry '+this.props.location,
              fontSize:25
            },
            legend:{
              display:this.props.displayLegend,
              position:this.props.legendPosition
            }
          }}
        />

        <Pie
          style={{ paddingTop: "70",
          paddingLeft: "70",
          paddingRight: "70",
          paddingBottom: "70",}}
          data={this.state.chartData}
          options={{
            title:{
              display:this.props.displayTitle,
              text:'Total Feedbacks per Ministry '+this.props.location,
              fontSize:25
            },
            legend:{
              display:this.props.displayLegend,
              position:this.props.legendPosition
            }
          }}
        />
      </div>
    )
  }
}

export default Chart;