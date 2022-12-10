<template>
  <div>
    <TabulatorComponent v-model="data" :options="options" @row-click="myMethod()" ref="mainTable"/>
  </div>
</template>

<script>
import { TabulatorComponent } from 'vue-tabulator';
import axios from 'axios';

export default {
  methods: {},
  data() {
    return {
      data: [
        {id: 0, 날짜: '22/11/07 09:30', 작업자명: '서용득', 코일번호: '2HM36111', 압연기번호: '2CRM', '예측 두께': 0.3911},
        {id: 1, 날짜: '22/11/08 09:30', 작업자명: '조성우', 코일번호: '2HM36111', 압연기번호: '2CRM', '예측 두께': 1.7825},
        {id: 2, 날짜: '22/11/09 09:30', 작업자명: '정유진', 코일번호: '2HM36111', 압연기번호: '2CRM', '예측 두께': 0.9981},
      ],
      options: {
        resizableColumns:false,
        height:"50vh",
        movableRows: true,
        selectable: 1,
        columns: [
          {
            title: '날짜',
            field: '날짜',
            width: `20%`,
          },
          {
            title: '작업자명',
            field: '작업자명',
            width: `20%`,
          },
          {
            title: '코일번호',
            field: '코일번호',
            width: `20%`,
          },
          {
            title: '압연기번호',
            field: '압연기번호',
            width: `20%`,
          },
          {
            title: '예측 두께',
            field: '예측 두께',
            width: `20%`,
          }
        ],
      },
      FEATURE_values: [
        11,
        22,
        33,
        44,
        55,
        66,
        77,
        88,
        99,
        1010,
        1111,
        1212
      ],
    };
  },
  components: {
    TabulatorComponent
  },
  methods: {
    myMethod() {
      console.log(this.$refs.mainTable.getInstance().getSelectedData());
      this.$emit('example_data', this.FEATURE_values);
    }
  },
  mounted() {
    let path = "http://localhost:8000/show_history";
    axios.get(path).then((res) => {
      console.log(res.data)
    })
  }
};
</script>
