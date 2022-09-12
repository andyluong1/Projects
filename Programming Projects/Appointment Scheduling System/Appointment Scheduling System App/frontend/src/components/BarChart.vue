<template>
<div>
    <div class="row">
        <div class="w-100 text-center" style="font-size: min(4.5vw, 20px); padding-left: 15px;">
            Appointment Frequency (last month)
        </div>
    </div>
    <div class="row mt-4">
        <canvas ref="myChart" style="height: 400px; width: 450px;"></canvas>
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
  data() {
    return {
      testChart: null
    }
  },
  async mounted() {
    const data = await axios.get('http://localhost:3000/dashboard/analytics/BarChart')
    const testChart = new Chart(this.$refs.myChart, {
      type: "line",
      data: {
        labels: [
          'Monday',
          'Tuesday',
          'Thursday',
          'Friday',
          'Saturday'
        ],
        datasets: [{
          data: [300, 50, 100, 0, 0],
          pointBackgroundColor: '#292b2c;',
          backgroundColor: [
            'rgb(91,80,212, .5)'
          ],
          hoverOffset: 4
        }]
      },
      options: {
        plugins:{   
          legend: {
            display: false
          }
        },
        spanGaps: true,
        fill: true,
        tension: 0.4,
        maintainAspectRatio: false,
        responsive: true,
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
    })
    testChart.data.datasets[0].data = data.data.datasets[0].data;
    testChart.update()
  }
};

</script>