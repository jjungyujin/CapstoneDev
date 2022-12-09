<template>
  <div class="card-body">
    <table class="inputTable">
      <thead>
        <tr>
          <th>코일의 평균 입측 두께</th>
          <th>upper 롤 이동값</th>
          <th>lower 롤 이동값</th>
          <th>밴딩 DS</th>
          <th>LH tension</th>
          <th>RH tension</th>
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
          <th>POR tension</th>
          <th>POR tension (N/mm<sup>2</sup>)</th>
          <th>롤 힘</th>
          <th>롤 속도</th>
          <th>좌 냉각수 유량</th>
          <th>우 냉각수 유량</th>
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
