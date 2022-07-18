<!-- canvas element placed in template tag because this is what is wanted to display -->
<template>
  <!-- canvas is a chart.js component to draw the graph after the data is gathered. -->
  <canvas ref="myChart"></canvas>
</template>

<script>
//using chart.js library
import Chart from "chart.js/auto";
export default {
  props: {
    label: {
      type: Array,
    },
    chartData: {
      type: Array,
    },
  },
  //allows asynchronous promises, once data is retrieved properly updates are added to the DOM
  async mounted() {
    //retrieves chart data
    console.log(this.chartData);
    //await function is used to populate Chart after data is loaded.
    await new Chart(this.$refs.myChart, {
      //type is an element to choose which type of chart the data will be displayed as
      type: 'bar',
      data: {
        labels: this.label,
        datasets: [
          {
            label: "total",
            backgroundColor: ["yellow", "blue", "green", "red"],
            data: this.chartData,
          },
        ],
      },
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
      },
    });
  },
};
</script>
