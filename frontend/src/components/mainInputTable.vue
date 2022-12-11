<template>
  <div class="card-body">
    <table class="inputTable">
      <thead>
        <tr>
          <th v-for="(column, index) in fstRow" :key="index">
            {{ column.name }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td v-for="(column, index) in fstRow" :key="index">
            <input
              type="number"
              step="0.001"
              v-bind:id="column.id"
              placeholder="값을 입력해주세요"
              class="main-input"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <table class="inputTable">
      <thead>
        <tr>
          <th v-for="(column, index) in scdRow" :key="index">
            {{ column.name }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td v-for="(column, index) in scdRow" :key="index">
            <input
              type="number"
              step="0.001"
              v-bind:id="column.id"
              placeholder="값을 입력해주세요"
              class="main-input"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <div class="main-input-table-button">
      <div id="reset-button" v-on:click="resetInputValues()">
        초기화
      </div>
      <div id="predict-button" v-on:click="getInputValues()">
        예측
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "mainInputTable",
  methods: {
    resetInputValues() {
      const inputList = document.getElementsByClassName("main-input");
      for (let i = 0; i < inputList.length; i++) {
        inputList[i].value = null;
      }
    },
    getInputValues() {
      const inputList = document.getElementsByClassName("main-input");
      let path = "http://localhost:8000/predict";
      let inputValueObj = {};
      for (let i = 0; i < inputList.length; i++) {
        if (inputList[i].value === "") {
          break;
        } else {
          inputValueObj[inputList[i].id] = inputList[i].value;
        }
      }
      axios.post(path, inputValueObj).then(res => {
        this.result = res.data.result;
      });
      console.log(this.result);
    }
  },
  data() {
    return {
      fstRow: [
        {
          name: "코일의 평균 입측 두께",
          id: "FEATURE_1"
        },
        {
          name: "upper 롤 이동값",
          id: "FEATURE_2"
        },
        {
          name: "lower 롤 이동값",
          id: "FEATURE_3"
        },
        {
          name: "밴딩 DS",
          id: "FEATURE_4"
        },
        {
          name: "LH tension",
          id: "FEATURE_5"
        },
        {
          name: "RH tension",
          id: "FEATURE_6"
        }
      ],
      scdRow: [
        {
          name: "POR tension",
          id: "FEATURE_7"
        },
        {
          name: "POR tension (N/mm2)",
          id: "FEATURE_8"
        },
        {
          name: "롤 힘",
          id: "FEATURE_9"
        },
        {
          name: "롤 속도",
          id: "FEATURE_10"
        },
        {
          name: "좌 냉각수 유량",
          id: "FEATURE_11"
        },
        {
          name: "우 냉각수 유량",
          id: "FEATURE_12"
        }
      ],
      result: ""
    };
  }
};
</script>
