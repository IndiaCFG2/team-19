import React, {Component} from 'react';
import {Bar, Line, Pie} from 'react-chartjs-2';

class Chart extends Component{
  constructor(props){
    super(props);
    this.state = {
      chartData:props.chartData
    }
  }

  static defaultProps = {
    displayTitle:true,
    displayLegend: true,
    legendPosition:'right',
    location:'City'
  }

  render(){
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