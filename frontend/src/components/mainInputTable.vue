<template>
  <div class="card-body">
    <table class="inputTable">
      <thead>
        <tr>
          <th>Feature 1</th>
          <th>Feature 2</th>
          <th>Feature 3</th>
          <th>Feature 4</th>
          <th>Feature 5</th>
          <th>Feature 6</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <input
              v-model="feature1"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature2"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature3"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature4"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature5"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature6"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
        </tr>
      </tbody>
    </table>
    <table class="inputTable">
      <thead>
        <tr>
          <th>Feature 7</th>
          <th>Feature 8</th>
          <th>Feature 9</th>
          <th>Feature 10</th>
          <th>Feature 11</th>
          <th>Feature 12</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <input
              v-model="feature7"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature8"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature9"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature10"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature11"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
          <td>
            <input
              v-model="feature12"
              type="text"
              placeholder="값을 입력해주세요"
              class="main-searchbox"
            />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  methods: {},
  data() {
    return {
      feature1: "",
      feature2: "",
      feature3: "",
      feature4: "",
      feature5: "",
      feature6: "",
      feature7: "",
      feature8: "",
      feature9: "",
      feature10: "",
      feature11: "",
      feature12: ""
    };
  },
  components: {}
};
</script>
