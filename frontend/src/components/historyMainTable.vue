<template>
  <div>
    <TabulatorComponent v-model="data_main_table" :options="options_main_table" @row-click="showFeatures()" ref="mainTable"/>
  </div>
</template>

<script>
import { TabulatorComponent } from 'vue-tabulator';
import axios from 'axios';

export default {
  data() {
    return {
      data_main_table: [],
      options_main_table: {
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
      history_data: {}
    };
  },
  components: {
    TabulatorComponent
  },
  methods: {
    showFeatures() {
      let clicked_row_num = this.$refs.mainTable.getInstance().getSelectedData()[0].id - 1;
      let clicked_row = this.history_data[clicked_row_num];
      let FEATURE_values = [];
      FEATURE_values.push(clicked_row.FEATURE_1);
      FEATURE_values.push(clicked_row.FEATURE_2);
      FEATURE_values.push(clicked_row.FEATURE_3);
      FEATURE_values.push(clicked_row.FEATURE_4);
      FEATURE_values.push(clicked_row.FEATURE_5);
      FEATURE_values.push(clicked_row.FEATURE_6);
      FEATURE_values.push(clicked_row.FEATURE_7);
      FEATURE_values.push(clicked_row.FEATURE_8);
      FEATURE_values.push(clicked_row.FEATURE_9);
      FEATURE_values.push(clicked_row.FEATURE_10);
      FEATURE_values.push(clicked_row.FEATURE_11);
      FEATURE_values.push(clicked_row.FEATURE_12);

      this.$emit('clicked_features', FEATURE_values);
    },
    formatDate(date_str) {
      let date_ = new Date(date_str);
      return date_.toLocaleString('ko-KR');
    }
  },
  created() {
    let path = "http://localhost:8000/show_history";
    axios.get(path).then((res) => {
      this.history_data = res.data;
      let hd = this.history_data;
      for (let i=0;i<hd.length;i++){
        let row = {
                    id: hd[i].HISTORY_ID,
                    날짜: this.formatDate(hd[i].DATE), 
                    작업자명: hd[i].WORKER_NAME, 
                    코일번호: hd[i].COIL_ID, 
                    압연기번호: hd[i].CRM_ID, 
                    '예측 두께': hd[i].THICKNESS_PRED
                  };
        this.data_main_table.push(row);
      }
    })
  }
};
</script>
