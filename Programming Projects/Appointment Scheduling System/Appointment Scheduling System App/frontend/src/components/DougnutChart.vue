<template>
<div>
    <div class="row">
        <div class="w-100 text-center" style="font-size: min(4.5vw, 20px); padding-left: 15px;">
            Most used Services (last month)
        </div>
    </div>
    <div class="row mt-4">
        <canvas ref="myChart"></canvas>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import Chart from 'chart.js/auto'
export default {
  props: {
    label: {
      type: Array,
    },
    chartData: {
      type: Array,
    },
  },
  //  This component defines the structure of the bar chart
  async mounted() {
    const data = await axios.get('http://localhost:3000/dashboard/analytics/DoughnutChart')
    const testChart = new Chart(this.$refs.myChart, {
      type: "doughnut",
      data: {
        labels: [],
        datasets: [{
          data: [],
          backgroundColor: [
            '#cc2f2f',
            '#3f53cf',
            'rgb(255,111,0)',
            '#2bc859',
            '#c45dd0'
          ],
          hoverOffset: 4
        }]
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
    testChart.data.datasets[0].data = data.data.datasets[0].data;
    testChart.data.labels = data.data.labels;
    testChart.update()
  },
};
</script>